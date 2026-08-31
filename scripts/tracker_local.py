"""Read local Markdown tracker tickets without contacting a remote service."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
from pathlib import Path


ALLOWED_STATUSES = frozenset(
    {
        "needs-triage",
        "needs-info",
        "ready-for-agent",
        "ready-for-human",
        "wontfix",
        "claimed",
        "done",
    }
)
FILENAME = re.compile(r"^(?P<number>\d+)-[^/\\]+\.md$")
HEADING = re.compile(r"^#\s+(?P<number>\d+):\s*(?P<title>.+?)\s*$")
METADATA = re.compile(r"^(Status|Claimed by|Claimed at|Blocked by):\s*(.*?)\s*$")
REQUIRED_METADATA = ("Status", "Claimed by", "Claimed at", "Blocked by")
UNCLAIMED = {"", "—", "-"}
FENCE_OPEN = re.compile(r"^\s{0,3}(?P<marker>`{3,}|~{3,})")


@dataclass(frozen=True)
class Ticket:
    number: int
    title: str
    status: str
    claimed_by: str | None
    claimed_at: str | None
    blockers: tuple[int, ...]
    path: Path
    evidence: str = ""


def parse_ticket(path: Path) -> Ticket:
    """Parse one local Markdown ticket with required tracker metadata."""
    filename_match = FILENAME.fullmatch(path.name)
    if not filename_match:
        raise ValueError(f"malformed ticket filename: {path.name}")

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"missing ticket heading: {path}")
    heading_match = HEADING.fullmatch(lines[0])
    if not heading_match:
        raise ValueError(f"malformed ticket heading: {path}")

    number = int(filename_match["number"])
    if number != int(heading_match["number"]):
        raise ValueError(f"ticket number does not match filename: {path}")

    metadata: dict[str, str] = {}
    for line in lines[1:21]:
        match = METADATA.fullmatch(line)
        if not match:
            continue
        field, value = match.groups()
        if field in metadata:
            raise ValueError(f"duplicate {field} metadata: {path}")
        metadata[field] = value

    for field in REQUIRED_METADATA:
        if field not in metadata:
            raise ValueError(f"missing {field} metadata: {path}")

    status = metadata["Status"]
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"unsupported status: {status}")

    claimed_by, claimed_at = _parse_claim(
        metadata["Claimed by"], metadata["Claimed at"]
    )
    if status == "claimed" and claimed_by is None:
        raise ValueError("claimed status requires claim metadata")
    blockers = _parse_blockers(metadata["Blocked by"])
    evidence = _parse_evidence(lines)
    if status == "done" and not evidence:
        raise ValueError("done status requires evidence")
    return Ticket(
        number=number,
        title=heading_match["title"],
        status=status,
        claimed_by=claimed_by,
        claimed_at=claimed_at,
        blockers=blockers,
        path=path,
        evidence=evidence,
    )


def load_tickets(directory: Path) -> dict[int, Ticket]:
    """Load every ticket in a directory and validate its blocker references."""
    tickets: dict[int, Ticket] = {}
    for path in sorted(directory.glob("*.md")):
        ticket = parse_ticket(path)
        if ticket.number in tickets:
            raise ValueError(f"duplicate ticket number: {ticket.number}")
        tickets[ticket.number] = ticket

    for ticket in tickets.values():
        for blocker in ticket.blockers:
            if blocker not in tickets:
                raise ValueError(
                    f"unknown blocker {blocker} referenced by ticket {ticket.number}"
                )
    return tickets


def frontier(tickets: dict[int, Ticket]) -> list[Ticket]:
    """Return ready tickets that are unclaimed and have only done blockers."""
    return sorted(
        (
            ticket
            for ticket in tickets.values()
            if ticket.status == "ready-for-agent"
            and ticket.claimed_by is None
            and all(
                tickets[blocker].status == "done"
                and bool(tickets[blocker].evidence.strip())
                for blocker in ticket.blockers
            )
        ),
        key=lambda ticket: ticket.number,
    )


def _parse_claim(claimed_by: str, claimed_at: str) -> tuple[str | None, str | None]:
    if claimed_by in UNCLAIMED and claimed_at in UNCLAIMED:
        return None, None
    if claimed_by in UNCLAIMED or claimed_at in UNCLAIMED:
        raise ValueError("claim actor and timestamp must be paired")
    if not claimed_at.endswith("Z"):
        raise ValueError("claim timestamp must be UTC and end in Z")
    if "T" not in claimed_at:
        raise ValueError("claim timestamp must be an ISO-8601 UTC date-time")
    try:
        timestamp = datetime.fromisoformat(f"{claimed_at[:-1]}+00:00")
    except ValueError as error:
        raise ValueError("claim timestamp must be ISO-8601 UTC") from error
    if timestamp.tzinfo != timezone.utc:
        raise ValueError("claim timestamp must be UTC")
    return claimed_by, claimed_at


def _parse_blockers(value: str) -> tuple[int, ...]:
    if value in {"", "—", "-", "None"}:
        return ()
    try:
        blockers = tuple(int(item.strip()) for item in value.split(","))
    except ValueError as error:
        raise ValueError(f"malformed blocker list: {value}") from error
    if any(blocker < 1 for blocker in blockers) or len(set(blockers)) != len(blockers):
        raise ValueError(f"malformed blocker list: {value}")
    return blockers


def _parse_evidence(lines: list[str]) -> str:
    fence_character: str | None = None
    fence_length = 0
    evidence: list[str] | None = None
    for line in lines:
        opening = FENCE_OPEN.match(line)
        if fence_character is not None:
            if evidence is not None:
                evidence.append(line)
            if (
                opening is not None
                and opening["marker"][0] == fence_character
                and len(opening["marker"]) >= fence_length
                and not line[opening.end() :].strip()
            ):
                fence_character = None
                fence_length = 0
            continue
        if opening is not None:
            if evidence is not None:
                evidence.append(line)
            fence_character = opening["marker"][0]
            fence_length = len(opening["marker"])
            continue
        if evidence is None and re.fullmatch(r"##\s+Evidence\s*", line):
            evidence = []
            continue
        if evidence is not None:
            if re.match(r"##\s+", line):
                break
            evidence.append(line)
    if evidence is not None:
        return "\n".join(evidence).strip()
    return ""
