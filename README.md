## To reproduce

```shell
git clone git@github.com:eguiraud/python-import-error-repro.git
cd python-import-error-repro
env PYTHONPATH=. pytest
# ...but for some reason this works:
env PYTHONPATH=. python repro/io/some_test.py

# possibly more interestingly, renaming the module from io to
# something else also fixes it
mv repro/io repro/bar
sed -i 's/repro.io/repro.bar/' repro/bar/some_test.py
env PYTHONPATH=. pytest
```

### To fix

```shell
touch repro/__init__.py
```
