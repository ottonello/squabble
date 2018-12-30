import pglast

import squabble.rule
from squabble.rules import BaseRule


class DisallowRenameEnumValue(BaseRule):
    """
    Prevent renaming existing enum value.

    Configuration:

    .. code-block:: json

        { "DisallowChangeEnumValue": {} }

    Tags: backwards-compatibility
    """

    MESSAGES = {
        'rename_not_allowed': 'cannot rename existing enum value "{value}"'
    }

    def explain_rename_not_allowed():
        """
        Renaming an existing enum value may be backwards compatible
        with code that is live in production.
        """

    def enable(self, ctx, _config):
        ctx.register('AlterEnumStmt', self._check_enum())

    @squabble.rule.node_visitor
    def _check_enum(self, ctx, node):
        """
        Node is an 'AlterEnumStmt' value

        {
            'AlterEnumStmt': {
                'newVal': 'bar',
                'oldVal': 'foo',   # present if we're renaming
            }
        }
        """

        # Nothing to do if this isn't a rename
        if node.oldVal == pglast.Missing:
            return

        renamed = node.oldVal.value

        ctx.report(self, 'rename_not_allowed', params={'value': renamed})
