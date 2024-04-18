from repro.io import foo


def test_something():
    assert foo() == 42

if __name__ == "__main__":
    print("running test!")
    test_something()
