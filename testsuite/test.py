from subprocess import call
import os

cwd = os.getcwd()
call(["python",
      cwd + "/listSorting.py",
      cwd + "/testsuite/input/list.txt",
      cwd + "/testsuite/expected_output/result.txt"])
