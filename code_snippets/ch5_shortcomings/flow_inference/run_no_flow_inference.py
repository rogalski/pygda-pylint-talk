import astroid

with open('flow_inference.py') as fh:
    node = astroid.extract_node(fh.read())

for value in node.infer():
    print(value)

# Const.NoneType(value=None)
# Const.int(value=6)
