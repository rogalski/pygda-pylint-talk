# Pylint Deep-Dive
Łukasz Rogalski
- - - -
## Agenda
1. Static analysis
2. Pylint as static analysis tool
3. Checkers
4. Inference engine
5. Known issues
6. Alternatives
7. Summary
8. Q&A
- - - -
## Static analysis
### Definition
> Static program analysis is the **analysis** of computer software that is performed **without actually executing programs**. In most cases the analysis is **performed on some version of the source code**, and in the other cases, some form of the object code.  
> The term is usually applied to the analysis performed by an **automated tool**, with human analysis being called program understanding, program comprehension, or code review. Software inspections and software walkthroughs are also used in the latter case.  
- - - -
### Let’s emphasise once again:
- analysis **without executing code**
- automated tool (often part of CI build)
- Ideally - is able to pick up common mistakes and does no emit false-positives
[List of tools for static code analysis - Wikipedia](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)
[TODO: picture]
- - - -
## Pylint as static analysis tool
[GitHub - PyCQA/pylint: A Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells](https://github.com/PyCQA/pylint)
- Dated back as far as 2001 (Python 2.2), originally authored by Logilab
- First commit in Git: [forget the past. · PyCQA/pylint@4becf6f · GitHub](https://github.com/PyCQA/pylint/commit/4becf6f9e596b45401680c4947e2d92c953d5e08)
- I wasn’t able to find old SVN repo copy :(
- - - -
### Quite popular:
[Search · pylint · GitHub](https://github.com/search?q=pylint&type=Code&utf8=%E2%9C%93)
[TODO: PICTURE]
- - - -
### How to install:
```bash
$ pip3 install pylint
```
### How to run:
```bash
$ pylint my_package
```
- - - -
### Sample output:
```shell
No config file found, using default configuration
************* Module flow.graph
C: 64, 0: Line too long (102/100) (line-too-long)
C:164, 0: Wrong continued indentation (add 1 space).
                                    isinstance(node.statement, ImplicitReturnStmt)), None)
                                    ^| (bad-continuation)
C:  1, 0: Missing module docstring (missing-docstring)
C:  9, 0: Missing class docstring (missing-docstring)
W: 21, 4: Useless super delegation in method '__init__' (useless-super-delegation)
R: 20, 0: Too few public methods (0/2) (too-few-public-methods)
W: 46, 0: Dangerous default value [] as argument (dangerous-default-value)
W: 46,24: Unused argument 'ast_node' (unused-argument)
R: 76, 4: Unnecessary "else" after "return" (no-else-return)
W:132, 0: Dangerous default value [] as argument (dangerous-default-value)
R:296, 4: Too many return statements (7/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 7.06/10 (previous run: 7.06/10, +0.00)
```
- - - -
## Checkers
### Checker
#### Definition
[TODO]
#### Two groups of checkers:
- token-based checkers
- AST-based checkers
- - - -
### Token-based checkers
#### Tokens
[TODO]
#### Tokens in Python
`tokenize` module in standard library allows to generate tokens based on module source.
##### simple_module.py:
```python
import sys

if len(sys.argv) <= 1:
    raise RuntimeError

print('\n'.join(sys.argv[1:]))
```
**run_tokenize.py:**
```python
import tokenize

module_name = "simple_module.py"
with open(module_name) as fh:
    for token in tokenize.generate_tokens(fh.readline):
        print(token)
```
- - - -
##### Sample line from output:
```
TokenInfo(type=53 (OP), string='(', start=(4, 6), 
          end=(4, 7), line='if len(sys.argv) <= 1:\n')
```
Each token has some some basic data associated with themselves:
- token type
- string value
- row and column indices for beginning and end of token
- actual line token comes from

Typically checks implemented by this kind of checker are:
- whitespace violations
- mixed indentation (tabs/spaces)
- etc.
Essentially, those checks rely on information which are missing from abstract syntax tree.
- - - -
### AST-based checkers
#### Abstract syntax tree
> In computer science, an abstract syntax tree (AST), or just syntax tree, is a tree representation of the abstract syntactic structure of source code written in a programming language. Each node of the tree denotes a construct occurring in the source code. The syntax is "abstract" in not representing every detail appearing in the real syntax.   
[Abstract syntax tree - Wikipedia](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- - - -
#### Python ASTs
`ast` module in standard library allows to generate syntax tree based on module source.
##### simple_module.py
```python
import sys

if len(sys.argv) <= 1:
    raise RuntimeError

print('\n'.join(sys.argv[1:]))
```
##### run_ast.py
```python
import ast

module_name = "simple_module.py"
with open(module_name) as fh:
    ast_root = ast.parse(fh.read(), filename=module_name)
```
- - - -
[TODO] Sample AST graph
- - - -
#### AST-based checker
- is fed with AST tree 
- walks over inputted tree
- acts accordingly based on visited nodes
#### Example
[TODO]
- - - -
## Inference engine
- both token-based and AST-based checkers knows only about structure of the source code
- it’s desirable to have actual knowledge about execution rules in static analysis tool (*without* actually running the code)
- Solution: astroid (AST on steroids) - [GitHub - PyCQA/astroid: A common base representation of python source code for pylint and other projects](https://github.com/PyCQA/astroid)
- - - -
> It provides a compatible representation which comes from the `_ast` module. It **rebuilds the tree** generated by the builtin `_ast` module by recursively walking down the AST and building an extended AST. The new node classes have **additional methods and attributes for different usages**. They include some support for **static inference** and **local name scopes**. Furthermore, `astroid` builds partial trees by **inspecting living objects**.  
- - - -
## Known problems
### Flow analysis
TODO
### Dynamic code constructs
TODO
- - - -
## Alternatives
### pycodestyle (formerly known as PEP8)
> `pycodestyle` is a tool to check your Python code against some of the style conventions in PEP 8.  

- No-AST policy (as lightweight as possible)
- Mostly limited to style-based checks
- [TODO] Sample messages?

[GitHub - PyCQA/pycodestyle: Simple Python style checker in one Python file](https://github.com/PyCQA/pycodestyle)
- - - -
### pyflakes
> A simple program which checks Python source files for errors.  
> Pyflakes analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It’s also much faster.  
> Pyflakes is also faster than Pylint or Pychecker. This is largely because Pyflakes only examines the syntax tree of each file individually. As a consequence, Pyflakes is more limited in the types of things it can check.  
- Simpler
- With AST-based checks, without inference engine

[GitHub - PyCQA/pyflakes: A simple program which checks Python source files for errors.](https://github.com/PyCQA/pyflakes)
- - - -
## Summary
- Lorem
- Ipsum
- Dolor
- Sit
- Amet
- - - -
### We still have a lot of issues unresolved
[TODO: Pic]
**Pull requests are welcome!**
- - - -
# Thanks!
- Slides: https://github.com/rogalski/pygda-pylint-talk
- My LinkedIn: https://www.linkedin.com/in/lukasz-rogalski/
- - - -
# Q&A