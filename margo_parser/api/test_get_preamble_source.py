from .get_preamble_source import get_preamble_source, get_markdown_preamble_source

def test_gets_empty_preamble():
    assert get_preamble_source("def say_hello():") == ""

def test_gets_preamble_with_comments():
    preamble_source = get_preamble_source("""
    # :: ignore-cell ::
    # :: view-cell ::
    # COMMENT
    # :: invalid-syntax ::
    """)

    assert len(preamble_source.split("\n")) == 3

def test_get_markdown_preamble_source():

    preamble_source = get_markdown_preamble_source("""
    ```margo # 0
    # 0
    # :: 1
    # 0
    # :: 2
    # :: 3```
    
    # Markdown Cell""")

    assert len(preamble_source.split("\n")) == 6

def test_get_markdown_preamble():
    preamble_source = get_preamble_source("""
    ```margo # 0
    # 0
    # :: 1
    # 0
    # :: 2
    # :: 3```
    
    # Markdown Cell""", cell_type="markdown")

    assert len(preamble_source.split("\n")) == 3