from botteryext.binput.patterns import HangUserPattern


def test_inputhandler():
    def view():
        return 'Hello'
    pattern = HangUserPattern(view)

    assert pattern.check(None) == 'Empty message'

    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'project', 'user': user})
    assert pattern.check(message) is False
    pattern.activate_hang(message)
    assert pattern.check(message) == view
    message.text = 'other'
    assert pattern.check(message) == view
    message.user.id = 2
    assert pattern.check(message) is False
    message.user.id = 1
    assert pattern.check(message) == view
    pattern.deactivate_hang(message)
    assert pattern.check(message) is False
