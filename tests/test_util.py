from squabble.util import format_type_name


def test_format_type_name():
    import pglast
    sql = 'CREATE TABLE _ (y time with time zone);'
    node = pglast.parse_sql(sql)
    col_def = node[0].stmt.tableElts[0]
    assert format_type_name(col_def.typeName) == 'pg_catalog.timetz'