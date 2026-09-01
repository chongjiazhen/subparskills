# TDD Under Pressure

Excuses and mid-stream violations. Catching yourself in either table means stop and restart the cycle, not adapt in place.

## Rationalizations

| Excuse | Reality |
| --- | --- |
| "Too simple to test" | Simple code still regresses; the test costs a minute. |
| "I'll write the test after" | A test shaped by existing code proves the code, not the behavior. |
| "Already manually tested" | Manual runs leave no regression guard and no evidence. |
| "Keep the old code as reference" | Reference code leaks into the rewrite; delete means delete. |
| "Need to explore first" | Explore in a throwaway spike, then delete it and start from a test. |
| "Already spent hours on this" | Sunk cost does not convert untested code into tested code. |

## Red flags - stop and restart

- Production code exists and its test does not.
- The new test passed on its first run.
- You cannot say why the test failed before the fix.
- "It's about the spirit, not the ritual."
