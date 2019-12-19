import wsgi


def test_handler():
    assert 'hello from bootcamp' == wsgi.handler()
