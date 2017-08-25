import os


def test_imports():
    print os.environ["PYTHONPATH"]
    __import__("lucidity")
    __import__("tgbvfx_environment")
