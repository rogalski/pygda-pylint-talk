import astroid

with open('mcs_demo.py') as fh:
    nodes = astroid.extract_node(fh.read())

meta_clsdef, a_clsdef, b_clsdef = nodes
assert a_clsdef.metaclass() is None
assert b_clsdef.metaclass() is meta_clsdef
