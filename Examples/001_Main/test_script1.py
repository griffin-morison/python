import script1

from io import StringIO
import sys

def test_script1_output(monkeypatch):
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    script1.function1()
    output = captured_output.getvalue().strip()
    assert output == "this is function 1 from script 1."

def test_script1_x():
    assert script1.x == 20