# Lessons learned

Durable scars. Prefer **short rules** over novels.

## Grok multi-session

- **Parallel sessions use worktrees (2026-08-25).** Concurrent and long-running tasks **must** use a dedicated worktree + unique branch. **Never** edit the main working tree while another session is active. Isolation is the worktree, not the branch name.
- **VS Code Grok Build has no `--worktree` launch switch.** Before the first edit, purple-pick the worktree (same shape as the old branch pick). After **New worktree**, create it from `main`, copy gitignored locals, and **stop editing the primary tree** — the human opens that folder to continue. CLI/TUI may still use `grok --worktree=<name> --ref main`.
- **Missing locals.** `git worktree add` copies the commit, not `.env` / tokens / caches. Copy those from the primary checkout before asking them to run the app.
- **Always pass `main`.** `git worktree add PATH -b wip/topic` with no start-point inherits this folder’s HEAD.
- **Two independently opened chats cannot DM each other.** The human is the bus. Durable handoff is git.
- **`checkout -b` still moves this folder.** Two chats here share one branch. Do not `checkout -b` in the primary tree to “make room.”
- **One-folder lock (2026-08-17) is superseded.** That lock (stay in one folder, `checkout -b` here, worktree only if asked) is **reversed**. Do not follow it.
- **Database changes are single-threaded.** Copied `.env` points every worktree at the same database. Before DDL / migrations: `git worktree list` — this session must be the only topic worktree. If another exists, stop.

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
