from lark import Lark, Transformer
import os


def load_parser(file=os.path.join(os.path.split(__file__)[0], "nbd.lark")):
    return Lark(open(file).read(), start="module")


def parse(code_block):
    parser = load_parser()
    tree = parser.parse(code_block)
    return NBDTransformer().transform(tree)


class NBDTransformer(Transformer):

    def empty_module(self, v):
        return ["NO_CODE"]

    def ignore_cell(self, v):
        return "IGNORE_CELL"

    def split_cell(self, s):
        return "SPLIT_CELL"

    def endblock(self, e):
        return "END_BLOCK"

    def expression(self, e):
        (e, ) = e
        return e

    def data_type(self, d):
        (d, ) = d
        return d

    def number(self, n):
        (n, ) = n
        try:
            return int(n.value)
        except BaseException:
            pass
        try:
            return float(n.value)
        except BaseException:
            pass
        raise Exception(f"Invalid number: {n.value}")

    def string(self, s):
        """
            Remove quote chars from string
        """
        (s,) = s
        return s[1:-1]
        return s.value

    def key(self, k):
        """
        Unwrap and get string. It won't have
        quote chars because it conforms to
        symbol regex: alphanums, . and _
        """
        (k, ) = k
        return k.value

    # A module is a list of expressions
    # separated by endblocks
    module = list

    def named_list(self, k):
        """
            Unpack the values into an array
            so it's always a two-element tuple
        """
        (k, *vals) = k
        return (k, vals)

    # directly convert to Python values
    def null(self, _): return None
    def true(self, _): return True
    def false(self, _): return False
