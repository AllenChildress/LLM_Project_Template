# Lessons learned

Durable scars. Prefer **short rules** over novels.

## Grok multi-session

- **One folder. Do not add sibling worktrees** unless the human asks. Extra checkouts (missing locals, two chats, rebase soup) were worse than sharing one checkout. New session = `checkout -b` **here**.
- **Two independently opened chats cannot DM each other.** The human is the bus. Durable handoff is git.
- **`checkout -b` still moves this folder.** Two chats here share one branch. Prefer one editing session at a time. After a topic-branch session, `git checkout main`.

## General (portable)

- Incomplete renames across UI stacks thrash more than file renames on disk — finish one vocabulary (e.g. page_key) in one series.
- Wide Markdown tables can break Preview; prefer vertical entries for long logs.
- Agent context: open only the docs the task needs, not the whole tree.
- SQL as app string literals ages badly (one-liners too) — put statements in `.sql` files the database lane owns; load by name (Coding_Standards).
- Prefer names that match the job (`db_report`, inventory). “Health” and similar borrowed words confuse readers when the domain is not medical.
- **Why Coding_Standards is long:** many entries exist because **Grok Build did not do them by default**, and other LLMs often will not either. Treat the standards file as the forced checklist for agents — do not assume the model already “knows” Rule of Three, SQL-in-files, 500-line caps, or cohesion pairs.

## Domain / product

_(Move product- or domain-specific lessons here or into the app repo — keep this kit portable.)_

## Environment

_(OS, Qt, conda, path traps, etc.)_
