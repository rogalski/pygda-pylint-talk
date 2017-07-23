import astroid

with open('dunders_demo.py') as fh:
    my_module = astroid.parse(fh.read(),
                              module_name='dunders')

a3_node = my_module.locals['a3'][0]
inferred_node = next(a3_node.infer())
print('a3:', inferred_node)
# a3: Instance of dunders.A

obj_node = my_module.locals['obj'][0]
inferred_node = next(obj_node.infer())
print('obj:', inferred_node)
# obj: Instance of dunders.CtxMgr
