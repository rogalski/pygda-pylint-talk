import astroid

with open('parent_children_demo.py') as fh:
    nodes = astroid.extract_node(fh.read())
    assign_node, function_node, return_node = nodes

print(assign_node)
# Assign(targets=[<AssignName.SOME_GLOBAL l.1 at 0x0>],
#      value=<Const.int l.1 at 0x0>)
print(assign_node.parent)
# Module(name='',
#        doc=None,
#        file='<?>',
#        path='<?>',
#        package=False,
#        pure_python=True,
#        future_imports=set(),
#        body=[<Assign l.1 at 0x0>, <FunctionDef.func l.4 at 0x0>])
print(function_node)
# FunctionDef.func(name='func',
#                  doc=None,
#                  decorators=None,
#                  args=<Arguments l.4 at 0x0>,
#                  returns=None,
#                  body=[<Assign l.5 at 0x0>, <Return l.6 at 0x0>])
children = list(function_node.get_children())
print(children)
# [<Arguments l.4 at 0x0>, <Assign l.5 at 0x0>, <Return l.6 at 0x0>]
print(return_node in children)
# True
