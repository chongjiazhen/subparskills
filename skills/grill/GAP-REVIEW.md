# Gap Review

Use this when the user already has a written proposal, brief, design, or deck and wants a hole-punch pass instead of a fresh interview.

## Procedure

1. Read the artifact and extract its stated goal, constraints, and success condition.
2. Identify omissions, contradictions, unowned decisions, claims with no operational proof, and perspectives or stakeholders absent from it.
3. Cite each gap to the exact section or sentence that made it visible. A gap interrogates the requirement's wording, not the implementation: "is 'prominent' quantified?" is a gap; "verify the button renders prominently" is a test and belongs to `plan`.
4. Group findings by severity and reversal cost. Distinguish blocking gaps from deferred nice-to-haves.
5. End with the gap list only - no proposed fixes or rewrites. Diagnosis and treatment are separate jobs; a proposed patch lets the author accept it instead of seeing the hole. Name each gap class checked - a silently skipped class reads the same as a clean one.
