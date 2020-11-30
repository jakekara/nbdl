from .MargoBlock import MargoBlock
from ..utils.get_preamble_source import get_markdown_preamble_source


class MargoMarkdownPreambleBlock(MargoBlock):
    def __init__(self, source: str):
        """A helper to process just the Margo preamble (if any) of a Markdown
        cell
        :param source: The entire source of a Markdown cell
        """

        preamble_source = get_markdown_preamble_source(source)
        super().__init__(preamble_source)
