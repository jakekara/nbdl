from margo_parser.api.utils.get_preamble_block import get_preamble_block
from margo_parser.api import MargoStatementTypes


def gets_empty_preamble():
    block = get_preamble_block(
        """

    """
    )

    assert len(block.statements) == 0


def gets_preamble_with_comments():
    block = get_preamble_block(
        """
    # :: get-this ::
    # don't get this
    # :: but-do-get-this ::
    # :: key-word_1: "value"
    #
    # def say_hello():
    #   invalid-python-code()
    """
    )

    assert len(block.statements) == 2
    assert block.statements[1].type == MargoStatementTypes.DECLARATION
    assert block.statements[1].name == "key-word_1"


def test_gets_preamble_from_markdown_cell():
    block = get_preamble_block(
        """
    ```margo # :: ignore-cell :: ignore-cell ::
    # :: do-not-ignore-cell ::
    3```

    # Markdown Cell""",
        cell_type="markdown",
    )

    assert len(block.statements) == 3


def test_only_gets_markdown_preamble_if_cell_starts_with_code():
    block = get_preamble_block(
        """
    # Markdown Cell
    This cell has no preamble sine it does not begin with fenced code
    ```margo # :: ignore-cell :: ignore-cell ::
    # :: do-not-ignore-cell ::
    3```

    # Markdown Cell""",
        cell_type="markdown",
    )

    assert len(block.statements) == 0
