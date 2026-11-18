# 0x07. Python - Test-driven development

Functions written with their tests first:

- `0-add_integer.py`: add two integers (`tests/0-add_integer.txt`).
- `2-matrix_divided.py`: divide a matrix (`tests/2-matrix_divided.txt`).
- `3-say_my_name.py`: print a name (`tests/3-say_my_name.txt`).
- `4-print_square.py`: print a square (`tests/4-print_square.txt`).
- `5-text_indentation.py`: indent a text (`tests/5-text_indentation.txt`).
- `6-max_integer.py`: max of a list, tested with `unittest`
  (`tests/6-max_integer_test.py`).
- `100-matrix_mul.py`: multiply two matrices (`tests/100-matrix_mul.txt`).
- `101-lazy_matrix_mul.py`: multiply two matrices with NumPy
  (`tests/101-lazy_matrix_mul.txt`).

Run the doctests with `python3 -m doctest ./tests/*.txt` and the unittests
with `python3 -m unittest tests.6-max_integer_test`.
