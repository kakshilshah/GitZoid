import ast
from pathlib import Path


def test_fetch_activity_docstring_names_the_module():
    source_path = Path(__file__).resolve().parents[2] / "fetch_activity.py"
    module = ast.parse(source_path.read_text(encoding="utf-8"))
    docstring = ast.get_docstring(module)
    assert docstring is not None
    first_line = docstring.splitlines()[0]
    assert first_line.startswith("fetch_activity.py — ")
