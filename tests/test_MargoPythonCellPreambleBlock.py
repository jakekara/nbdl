from margo_parser.api import MargoPythonCellPreambleBlock


def test_parses_preamble():
    cell_source = """
    # :: ignore-cell ::
    # :: do-something ::
    # A comment

    some_code()
    """

    block = MargoPythonCellPreambleBlock(cell_source)
    assert len(block.statements) == 2
    assert block.statements[0].type == "DIRECTIVE"
    assert block.statements[0].name == "ignore-cell"
    assert block.statements[1].type == "DIRECTIVE"
    assert block.statements[1].name == "do-something"
