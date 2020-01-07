import wsgi


def test_handler():
    assert wsgi.handler() == 'hello from bootcamp'
