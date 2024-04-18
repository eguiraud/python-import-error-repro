## To reproduce

```shell
git clone git@github.com:eguiraud/python-import-error-repro.git
cd python-import-error-repro
env PYTHONPATH=. pytest  # fails!
# ...but for some reason this works:
env PYTHONPATH=. python repro/io/some_test.py

# I am not sure why, but adding a top-level __init__.py
# makes pytest work:
touch repro/__init__.py
env PYTHONPATH=. pytest  # now passes!

# even more interestingly, renaming the module from io to
# something else also fixes it:
rm repro/__init__.py  # in case you just added it
mv repro/io repro/bar
sed -i 's/repro.io/repro.bar/' repro/bar/some_test.py
env PYTHONPATH=. pytest  # also passes!
```
