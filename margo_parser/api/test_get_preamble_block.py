from .get_preamble_block import get_preamble_block
from .MargoStatement import MargoStatementTypes

def gets_empty_preamble():

    block = get_preamble_block("""

    """)

    assert len(block.statements) == 0

def gets_preamble_with_comments():
    block = get_preamble_block("""
    # :: get-this ::
    # don't get this
    # :: but-do-get-this ::
    # :: key-word_1: "value"
    # 
    # def say_hello():
    #   invalid-python-code()
    """)

    assert len(block.statements) == 2
    assert block.statements[1].type == MargoStatementTypes.DECLARATION
    assert block.statements[1].name == "key-word_1"
    