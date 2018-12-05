from modules.Generator.start import Generator


def test_start():
    start = Generator()
    assert start.hello() == "hello"
