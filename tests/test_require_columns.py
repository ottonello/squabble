import pglast
from squabble.rules.require_columns import (
    _normalize_columns,
    get_required_columns,
    parse_column_type,
)


def test_parse_column_type():
    assert parse_column_type("integer") == "integer"
    assert parse_column_type("custom(type)") == "custom(type)"


def test_normalize_columns():
    create_table = pglast.parse_sql(
        "CREATE TABLE _(COL1 foo.bar(baz,123), Col2 integer);"
    )
    table_elts = create_table[0].stmt.tableElts
    print(table_elts)
    assert _normalize_columns(table_elts) == [
        ("col1", "foo.bar(baz, 123)"),
        ("col2", "integer"),
    ]


def test_get_required_columns():
    assert get_required_columns(["foo,int", "Bar"]) == {"foo": "integer", "bar": None}
