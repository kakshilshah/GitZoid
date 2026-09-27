# GitZoid review checklist

1. Nodes are flat scripts that run top to bottom. Never add an `if __name__ == "__main__"` guard or
   wrap a node in `main()` to make it testable. Test nodes with `runpy.run_path(..., run_name="__main__")`
   as in `tests/unit/test_generate_technical_report.py`.
2. No sibling-node imports and no shared helper modules. Helpers are duplicated across nodes on
   purpose so each node runs alone.
3. `waveassist.init()` comes before any data access. Booleans in the store are the strings "0"/"1".
4. Fall through on empty, soft-fail per item (log and skip one repo or PR, never sink the batch);
   raise only for real failures.
5. Tests are hermetic: patch the waveassist SDK (including `mark_run_idle`) and `requests`. No network.
6. Inline test fixtures. `.gitignore` ignores `*.json` and `*.csv`, so fixture files of those types
   never reach the commit.
7. Assert behaviour and content, not CSS or HTML literals.
8. When a change closes an item in CLAUDE.md "Known issues" or "Test gap", update that line.

Do not flag duplicated helpers across node files. Do not suggest shared modules, `__main__` guards,
or type-annotation or formatting sweeps of untouched code.
