## To reproduce

```shell
git clone git@github.com:eguiraud/python-import-error-repro.git
cd python-import-error-repro
env PYTHONPATH=. pytest
# ...but for some reason this works:
env PYTHONPATH=. python repro/io/some_test.py
```

### To fix

```shell
touch repro/__init__.py
```
