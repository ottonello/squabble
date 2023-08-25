from squabble.lint import _parse_string, Context
from pglast.ast import RawStmt

def test_parse_string():
    assert len(_parse_string("SELECT 1")) == 1
    assert _parse_string("-- just a comment") == None
