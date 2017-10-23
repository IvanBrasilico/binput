from unittest import mock

from views import input_example


@mock.patch('inputapp.InputHandler.hang_in')
@mock.patch('inputapp.InputHandler.hang_out')
def test_input_example(hang_in, hang_out):
    ''''''
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'project', 'user': user})
    prompt = input_example(message)
    assert prompt.find('Enter Project Name:') == 0
    message.text = 'aname'
    prompt = input_example(message)
    assert prompt.find('Enter Project Language:') == 0
    message.text = 'invalid'
    prompt = input_example(message)  # invalid enter
    assert prompt.find('Enter a Valid Value:') == 0
    message.text = 'python3'
    prompt = input_example(message)  # valid enter
    assert prompt.find('Enter Project site:') == 0
    message.text = 'asite'
    prompt = input_example(message)
    assert prompt.find('Enter Project priority:') == 0
    message.text = 'insane'
    prompt = input_example(message)
    assert prompt.find('Project created') == 0
