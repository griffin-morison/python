import script2

from io import StringIO
import sys

def test_script2_output(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    script2.function2()
    output = captured_output.getvalue().strip()
    assert output == "this is function 2 from script 2."