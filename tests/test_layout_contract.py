from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_workbench_layout_has_responsive_wrapping_and_priority():
    css = (ROOT / "src" / "styles" / "main.css").read_text(encoding="utf-8")
    assert "min-width:320px" in css
    assert ".controls{display:flex;align-items:flex-end;flex-wrap:wrap" in css
    assert ".result-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))" in css
    assert ".ua-card{grid-column:1/-1" in css
    assert "@media(max-width:760px)" in css
    assert ".result-grid{grid-template-columns:minmax(0,1fr)}" in css
    assert ".controls>div{flex-basis:100%;min-width:0}" in css


def test_small_phone_layout_does_not_overflow_status_or_coverage():
    css = (ROOT / "src" / "styles" / "main.css").read_text(encoding="utf-8")
    assert "@media(max-width:420px)" in css
    assert ".status{max-width:48%}" in css
    assert ".coverage-summary{grid-template-columns:1fr}" in css
