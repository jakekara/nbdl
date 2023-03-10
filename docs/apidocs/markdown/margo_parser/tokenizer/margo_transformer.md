Module margo_parser.tokenizer.margo_transformer
===============================================

Classes
-------

`MargoTransformer(visit_tokens=True)`
:   Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    
    Calls its methods (provided by user via inheritance) according to ``tree.data``.
    The returned value replaces the old one in the structure.
    
    They work bottom-up (or depth-first), starting with the leaves and ending at the root of the tree.
    Transformers can be used to implement map & reduce patterns. Because nodes are reduced from leaf to root,
    at any point the callbacks may assume the children have already been transformed (if applicable).
    
    ``Transformer`` can do anything ``Visitor`` can do, but because it reconstructs the tree,
    it is slightly less efficient. It can be used to implement map or reduce patterns.
    
    All these classes implement the transformer interface:
    
    - ``Transformer`` - Recursively transforms the tree. This is the one you probably want.
    - ``Transformer_InPlace`` - Non-recursive. Changes the tree in-place instead of returning new instances
    - ``Transformer_InPlaceRecursive`` - Recursive. Changes the tree in-place instead of returning new instances
    
    Parameters:
        visit_tokens: By default, transformers only visit rules.
            visit_tokens=True will tell ``Transformer`` to visit tokens
            as well. This is a slightly slower alternative to lexer_callbacks
            but it's easier to maintain and works for all algorithms
            (even when there isn't a lexer).

    ### Ancestors (in MRO)

    * lark.visitors.Transformer
    * lark.visitors._Decoratable

    ### Methods

    `ENDBLOCK(self, eb)`
    :

    `IGNORE_CELL(self, _)`
    :

    `KEY(self, k)`
    :

    `QSTRING(self, s)`
    :

    `argument_list(self, al)`
    :

    `block(self, b)`
    :

    `builtin(self, s)`
    :

    `directive(self, d)`
    :

    `evf_assignment(self, c)`
    :

    `expression(self, e: lark.tree.Tree)`
    :

    `false(self, _)`
    :

    `function(self, f)`
    :

    `function_name(self, fn)`
    :

    `mvf_assignment(self, kvp)`
    :

    `null(self, _)`
    :

    `number(self, n)`
    :

    `statement(self, s: lark.tree.Tree)`
    :

    `string(self, s)`
    :

    `true(self, _)`
    :

    `value(self, v)`
    :