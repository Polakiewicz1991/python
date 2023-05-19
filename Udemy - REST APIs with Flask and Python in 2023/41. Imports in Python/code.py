import sys
print("path: ",sys.path)
# from mymodule import divide
from mymodule import divide # '.' przed plikiem jeżeli FOLDER(nie plik.py) znajduje się w tym samym folderze
# import ImportsInPythonMyModule41

print(divide(10,2))
print("mymodule.py: ", __name__)


# print("modules: ",sys.modules)
# set PYTHONPATH=/Users komenda w terminalu "export - maca"/"set - windows
# https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html