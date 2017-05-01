import tokenize

module_name = "simple_module.py"
with open(module_name) as fh:
    for token in tokenize.generate_tokens(fh.readline):
        print(token)
