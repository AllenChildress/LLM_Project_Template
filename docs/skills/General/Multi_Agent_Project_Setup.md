# Multi-agent project setup (portable)

Bootstrap **focused multi-agent context** so agents load only relevant rules.

## Goals

1. Nested `AGENTS.md` by directory  
2. Specialist agents (dba, ui, tester, domain, integration, security, docs)  
3. Short rule files — **point** to docs; never dump the full set  

## Spawn bar

| Situation | Action |
|-----------|--------|
| Tiny fix / one narrative | Main only |
| Large exclusive trees (schema + UI + tests) | Spawn 2–3 specialists |
| Unclear product judgment | Ask the human |

## Agent identity

First line of every user-visible reply: `main:` / `ui:` / `dba:` / …

## Depth limit

Specialists **do not** spawn other specialists. They return a Handoff; main routes next.

## Verify

```text
grok inspect
```

Adjust agent definitions under `.grok/agents/` when you add a real app.
