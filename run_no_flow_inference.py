import astroid

with open('inference_flow.py') as fh:
    node = astroid.extract_node(fh.read())

for value in node.infer():
    print(value)
