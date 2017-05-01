import ast

module_name = "simple_module.py"
with open(module_name) as fh:
    ast_root = ast.parse(fh.read(), filename=module_name)
