export PYTHONPATH="$(realpath .):$PYTHONPATH"
echo $PYTHONPATH
python3 -m pytest -vv $(find -name 'tests.py')
