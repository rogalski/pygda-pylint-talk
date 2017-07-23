import astroid

with open('mro_demo.py') as fh:
    my_module = astroid.parse(fh.read())

e_class = my_module.locals['E'][0]
print(e_class.mro())
# [<ClassDef.E l.6 at 0x1073db668>, <ClassDef.D l.5 at 0x1073db588>, <ClassDef.C l.4 at 0x1073db518>,
#  <ClassDef.A l.2 at 0x1073db470>, <ClassDef.B l.3 at 0x1073db4a8>, <ClassDef.object l.0 at 0x106b2e3c8>]
