import astroid

with open('slicing_demo.py') as fh:
    seq_node, seq2_node = astroid.extract_node(fh.read())

inferred_seq1 = next(seq_node.infer())
inferred_seq2 = next(seq2_node.infer())
print(inferred_seq1)
print([v.value for v in inferred_seq1.elts])
print(inferred_seq2)
print([v.value for v in inferred_seq2.elts])
