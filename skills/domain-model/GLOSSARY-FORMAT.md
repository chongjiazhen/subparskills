# GLOSSARY.md Format

## Structure

```md
# <Context name>

One or two sentences on what this context is and why it exists.

## Language

**Order**:
A customer's request for goods, from placement to fulfilment.
_Avoid_: purchase, transaction

**Customer**:
A person or organization that places orders.
_Avoid_: client, buyer, account
```

## Rules

- One word per concept. When several exist, pick the best and list the rest under `_Avoid_` - the Avoid line is what stops synonym drift in code and tickets.
- Define what a term is in one or two sentences, not what it does.
- Only terms specific to this context. General programming concepts (timeout, retry, handler) stay out however often the project uses them.
- Group under subheadings only when clusters emerge; a flat list is fine.

## Decision records

A decision record from step 5 goes to `docs/adr/NNNN-<slug>.md`: context, decision, alternatives rejected and why. Readers of `GLOSSARY.md` check that directory for the area they touch.
