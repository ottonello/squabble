from squabble.rules.disallow_float_types import _parse_column_type


def test_parse_column_type():
    assert _parse_column_type('real') == 'pg_catalog.float4'
    assert _parse_column_type('double precision') == 'pg_catalog.float8'