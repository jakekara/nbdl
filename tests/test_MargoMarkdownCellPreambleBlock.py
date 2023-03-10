from margo_parser.api import MargoMarkdownCellPreambleBlock


def test_parses_preamble():
    source = """

    ```margo
    ignore-cell ::
    do-something ::
    ```

    # Hello, world

    This cell is a description of the Hello, world program....

    Note that in the margo preamble we don't need the `# ::` prefix
    """

    block = MargoMarkdownCellPreambleBlock(source)

    assert len(block.statements) == 2
    assert block.statements[0].type == "DIRECTIVE"
    assert block.statements[0].name == "ignore-cell"
    assert block.statements[1].type == "DIRECTIVE"
    assert block.statements[1].name == "do-something"
