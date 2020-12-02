margo-parser API documentation
==============================

by Jake Kara

MargoStatement
--------------

A Margo directive or declaration

.. autoclass:: margo_parser.api.MargoStatement
    :members:

.. autoclass:: margo_parser.api.MargoStatementTypes
    :members:

MargoBlock
----------

A collection of statements

.. autoclass:: margo_parser.api.MargoBlock
    :members:

MargoMarkdownPreambleBlock
--------------------------------------

MargoBlock generated from the contents of a Markdown cell

.. autoclass:: margo_parser.api.MargoMarkdownPreambleBlock
    :inherited-members:

MargoPythonCellPreambleBlock
----------------------------

MargoBlock generated from the contents of a Python cell

.. autoclass:: margo_parser.api.MargoPythonCellPreambleBlock
    :inherited-members:

Exceptions
----------

.. autoclass:: margo_parser.api.MargoParseException


.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
