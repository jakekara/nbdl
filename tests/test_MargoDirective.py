from margo_parser.api import MargoDirective, MargoStatementTypes

def test_directive_type():
    directive = MargoDirective("ignore-cell")
    assert directive.type == MargoStatementTypes.DIRECTIVE

def test_directive_value_always_null():
    directive = MargoDirective("ignore-this")
    assert directive.value is None

def test_directive_name():
    directive = MargoDirective("ignore-this-cell")
    assert directive.name == "ignore-this-cell"