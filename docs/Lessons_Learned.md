# Lessons learned

Durable scars. Prefer **short rules** over novels.

## Grok multi-session

- **A branch is not a folder.** `git checkout -b wip/other` in the project directory **moves that folder** onto the new branch. A second Grok chat in the same directory is now on `wip/other` too; uncommitted files mix. Isolation = sibling worktree (`git worktree add ..\<RepoName>_<topic> -b wip/<topic> main`) **and** open the new chat **in that folder**. Always pass **`main`** — omit it and the new branch starts at this folder’s HEAD. Default is folder + branch; same-folder checkout is an explicit exception. See PROCESS § New Grok session → branch + folder. Official: [git-worktree](https://git-scm.com/docs/git-worktree).
- **Pushing does not move any folder.** After a **This folder** session, `git checkout main` so the next chat here is not still on `wip/<topic>`. Checkout ≠ merge.
- **Two independently opened chats cannot DM each other.** No mailbox. The human is the bus. `/dashboard` peek/reply only reaches agents in the **same pager**. Durable handoff is git (commits, Change_Log) — not scratch files slid between folders unless asked.
- **A “harmless” docs or analysis session can steal the other chat’s folder.** `checkout -b` in the same directory mixes uncommitted work and can block a push. New sibling folder first; open the new chat **there**. When done: merge, then `git worktree remove <folder>` (the branch is the work; the folder is disposable).

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
