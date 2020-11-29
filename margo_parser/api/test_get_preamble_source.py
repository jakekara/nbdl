from .get_preamble_source import get_preamble_source

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

