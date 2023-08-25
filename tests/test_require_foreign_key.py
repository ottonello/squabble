import re

import pglast
from squabble.rules.require_foreign_key import _column_needs_foreign_key


def test_column_needs_foreign_key():
    fk_regex = re.compile(".*_id$")
    # name doesn't match regex
    assert (
        _column_needs_foreign_key(fk_regex, pglast.ast.ColumnDef(colname="email"))
        == False
    )
    # name matches regex, but no foreign key
    assert (
        _column_needs_foreign_key(fk_regex, pglast.ast.ColumnDef(colname="users_id"))
        == True
    )
    # name matches regex, but has foreign key (contype == 8)
    assert (
        _column_needs_foreign_key(
            fk_regex,
            pglast.ast.ColumnDef(
                colname="post_id",
                constraints=[
                    pglast.ast.Constraint(
                        contype=pglast.enums.parsenodes.ConstrType.CONSTR_FOREIGN
                    )
                ],
            ),
        )
        == False
    )
