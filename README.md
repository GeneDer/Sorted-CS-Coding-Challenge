# Sorted-CS-Coding-Challenge
## Description
Given a input file contained spaced words and integers, sort words and integers and place them in their corrosponding type indices. Each word and integers might contain none letter and digit characters. Remove them as well. 

Example: `20 cat bi?rd 12 do@g`  >> should read >>  `12 bird cat 20 dog`

## How to run
1. Clone my repository and cd to the root of the project.
2. In terminal, type `python listSorting.py <path-to-input-file> <path-to-output-file>`. Where `<path-to-input-file> ` is the directory contained your input file and `<path-to-output-file>` is the firectory contained your output file. 
3. An example input is stored in `/input/list.txt` and example output is stored in `/output/result.txt`. Enter `python listSorting.py input/list.txt output/result.txt` to see it in action.
4. A test suite is perpared in `testsuite`. In the root of project directory, enter `python testsuite/test.py` to execute.
5. You can add more test by added input file in `testsuite/input` and output file in `testsuite/expected_output` with the same name.
