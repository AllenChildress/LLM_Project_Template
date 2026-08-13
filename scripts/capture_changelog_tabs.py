"""Stub: boot YOUR_APP, grab each modified view, promote Change_Log thumbs.

This kit is not an application. Copy this file into the app repo and bind it
to your window (Qt, web, or other). Stock_Data has a worked PyQt6 example.

Typical flow:

1. Bypass single-instance if a live window may already be open.
2. Show the window; wait until paint is real.
3. For each tab slug the change touched: switch view, wait, grab, promote.
4. Restore user prefs (filters, overlays) if you temporarily changed them.
5. Quit.

Do not commit error_* dumps. Sensitive views need --allow-sensitive on promote.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print(
        "STUB: bind scripts/capture_changelog_tabs.py to your UI, then grab "
        "each modified view and call scripts/promote_changelog_shot.py.\n"
        f"Kit root: {ROOT}"
    )
    print("See docs/PROCESS.md § Change_Log screenshots.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
