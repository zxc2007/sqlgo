from sqlmap.lib.core.convert import getOrds
from sqlmap.plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar") == "SELECT CHAR(97,98,99,100,101,102,103,104) FROM foobar"
        True
        """

        def escaper(value):
            return "CHAR(%s)" % ','.join("%d" % _ for _ in getOrds(value))

        return Syntax._escape(expression, quote, escaper)
