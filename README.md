Github Actions

Running Tests
For a successfull tests run always save the test file as test_.py because pytesat searches for files named like test_*.py or *test.py and test functions (starting with test) present.

By default, pytest searches the current directory. If your tests are in a specific folder (like tests/), add cd tests before running pytest or specify the path explicitly:

- name: Run tests
  run: |
    coverage run -m pytest tests/ -v -s

or 

- name: Run tests
  run: |
    cd tests
    coverage run -m pytest -v -s 
