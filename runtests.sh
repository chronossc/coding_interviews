export PYTHONPATH="$(realpath .):$PYTHONPATH"
echo $PYTHONPATH

if [ $# -eq 0 ];then
  args="$(find -name 'tests.py')"
else
  args="$@"
fi
python3 -m pytest -v $args
