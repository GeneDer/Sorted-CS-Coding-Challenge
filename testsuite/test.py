from subprocess import call
import os

cwd = os.getcwd()
for i in os.listdir(cwd + "/testsuite/input"):
    file_name = i.split('.')
    if len(file_name) == 2 and file_name[1] == "txt":
        call(["python",
              cwd + "/listSorting.py",
              cwd + "/testsuite/input/" + i,
              cwd + "/testsuite/expected_output/" + file_name[0] + ".txt"])

