from botteryext.binput.inputhandler import InputHandler


def test_inputhandler():
    ih = InputHandler(None)

    class HangUser():
        def activate_hang(self, message):
            pass

        def deactivate_hang(self, message):
            pass
    ih.set_hang(HangUser(), 'project')
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'project', 'user': user})
    ih.hang_in(message)
    ih.input(message, 'name', 'Enter Project Name:')
    ih.input(message, 'language', 'Enter Project Language: ',
             ['python2', 'python3'])
    ih.input(message, 'site', 'Enter Project site:')
    ih.input(message, 'priority', 'Enter Project priority:',
             ['insane', 'medium', 'dontmatter'])
    prompt = ih.print_next_input(message)
    assert prompt.find('Enter Project Name:') == 0
    message.text = 'aname'
    stay, prompt = ih.next_input_queue(message)
    assert stay is True
    assert prompt.find('Enter Project Language:') == 0
    message.text = 'invalid'
    stay, prompt = ih.next_input_queue(message)  # invalid enter
    assert stay is True
    assert prompt.find('Enter a Valid Value:') == 0
    message.text = 'python3'
    stay, prompt = ih.next_input_queue(message)  # valid enter
    assert stay is True
    assert prompt.find('Enter Project site:') == 0
    message.text = 'asite'
    stay, prompt = ih.next_input_queue(message)
    assert stay is True
    assert prompt.find('Enter Project priority:') == 0
    message.text = 'insane'
    stay, inputs = ih.next_input_queue(message)
    assert stay is False
    assert inputs['name'] == 'aname'
    assert inputs['language'] == 'python3'
    assert inputs['site'] == 'asite'
    assert inputs['priority'] == 'insane'
