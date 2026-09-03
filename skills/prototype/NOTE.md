# Prototype note

Written at step 7, even when the prototype is abandoned - an abandoned prototype with a note is worth more than one without, because the note is the value. Half a page, past tense.

```md
---
question: <the design question this prototype existed to answer>
spec: <path to the spec or plan it feeds, or none>
outcome: settled | abandoned | inconclusive
date: YYYY-MM-DD
---

## Tried

What was built and against which cases - the hard-to-reason inputs, the
variants switched, the state that was surfaced.

## Learned

The verdict, and the evidence for it. What surprised. What the real code must
do differently from the prototype.

## Decision

The choice folded into the real code, or why no choice was made. Link the
commit that carried it.
```

Store it where the project keeps design notes, beside the spec it feeds; the prototype itself stays off the main branch with a pointer here.
