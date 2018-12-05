from modules.Generator.start import Generator


def test_start():
    start = Generator()
    print("running")
    assert start.hello() == "hello"
