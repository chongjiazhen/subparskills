from __future__ import annotations

import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from tracker_local import frontier, load_tickets, parse_ticket


class TrackerLocalTests(unittest.TestCase):
    def write_ticket(
        self,
        directory: Path,
        number: int,
        *,
        title: str = "Example",
        status: str = "ready-for-agent",
        claimed_by: str = "—",
        claimed_at: str = "—",
        blocked_by: str = "None",
    ) -> Path:
        path = directory / f"{number:03d}-ticket.md"
        path.write_text(
            f"# {number:03d}: {title}\n\n"
            f"Status: {status}\n"
            f"Claimed by: {claimed_by}\n"
            f"Claimed at: {claimed_at}\n"
            f"Blocked by: {blocked_by}\n",
            encoding="utf-8",
        )
        return path

    def test_parse_ticket_reads_metadata(self) -> None:
        with self.subTest("valid ticket"):
            from tempfile import TemporaryDirectory

            with TemporaryDirectory() as temp:
                path = self.write_ticket(
                    Path(temp), 14, title="Login", blocked_by="011, 012"
                )
                ticket = parse_ticket(path)

        self.assertEqual(14, ticket.number)
        self.assertEqual("Login", ticket.title)
        self.assertEqual("ready-for-agent", ticket.status)
        self.assertIsNone(ticket.claimed_by)
        self.assertIsNone(ticket.claimed_at)
        self.assertEqual((11, 12), ticket.blockers)
        self.assertEqual(path, ticket.path)

    def test_frontier_selects_only_ready_unclaimed_unblocked_tickets(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            directory = Path(temp)
            self.write_ticket(directory, 1)
            self.write_ticket(directory, 2, status="done")
            self.write_ticket(directory, 3, blocked_by="002")
            self.write_ticket(directory, 4, blocked_by="005")
            self.write_ticket(
                directory,
                5,
                claimed_by="Riley",
                claimed_at="2026-08-31T13:28:07Z",
            )
            tickets = load_tickets(directory)

        self.assertEqual([1, 3], [ticket.number for ticket in frontier(tickets)])

    def test_parse_ticket_rejects_malformed_filename(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            original = self.write_ticket(Path(temp), 1)
            path = original.with_name("ticket.md")
            original.rename(path)
            with self.assertRaisesRegex(ValueError, "filename"):
                parse_ticket(path)

    def test_parse_ticket_rejects_missing_metadata(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            path = Path(temp) / "001-ticket.md"
            path.write_text("# 001: Example\n\nStatus: ready-for-agent\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Claimed by"):
                parse_ticket(path)

    def test_load_tickets_rejects_duplicate_numbers(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            directory = Path(temp)
            self.write_ticket(directory, 1)
            duplicate = directory / "001-copy.md"
            duplicate.write_text(
                "# 001: Copy\n\n"
                "Status: ready-for-agent\n"
                "Claimed by: —\n"
                "Claimed at: —\n"
                "Blocked by: None\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate"):
                load_tickets(directory)

    def test_load_tickets_rejects_unknown_blocker(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            directory = Path(temp)
            self.write_ticket(directory, 1, blocked_by="999")
            with self.assertRaisesRegex(ValueError, "unknown blocker"):
                load_tickets(directory)

    def test_parse_ticket_rejects_unsupported_status(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            path = self.write_ticket(Path(temp), 1, status="in-progress")
            with self.assertRaisesRegex(ValueError, "status"):
                parse_ticket(path)

    def test_parse_ticket_rejects_unpaired_or_non_utc_claim(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp:
            directory = Path(temp)
            missing_timestamp = self.write_ticket(
                directory, 1, claimed_by="Riley", claimed_at="—"
            )
            non_utc_timestamp = self.write_ticket(
                directory,
                2,
                claimed_by="Riley",
                claimed_at="2026-08-31T13:28:07+08:00",
            )
            with self.assertRaisesRegex(ValueError, "claim"):
                parse_ticket(missing_timestamp)
            with self.assertRaisesRegex(ValueError, "UTC"):
                parse_ticket(non_utc_timestamp)


if __name__ == "__main__":
    unittest.main()
