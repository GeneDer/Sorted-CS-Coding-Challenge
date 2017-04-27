from subprocess import call
import os

cwd = os.getcwd()
for i in os.listdir(cwd + "/testsuite/input"):
    if i[-3:] == "txt":
        call(["python",
              cwd + "/listSorting.py",
              cwd + "/testsuite/input/" + i,
              cwd + "/testsuite/actual_output/" + i])
        with open(cwd + "/testsuite/expected_output/" + i, "r") as eo,\
             open(cwd + "/testsuite/actual_output/" + i, "r") as ao:
            test_case = i.split('.')[0]
            if eo.readline() == ao.readline():
                print test_case, "Passed! :)"
            else:
                print test_case, "Failed! :("
