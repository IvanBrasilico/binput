'''InputHandler is an extension to add "Input commands" to bottery views
Usage:

On an Application:
app = App()
input = InputHandler(app)

On Patterns:
hang_user_pattern_input = HangUserPattern(input_example)
input.set_hang(hang_user_pattern_input, 'project')
patterns = [
    hang_user_pattern_input,
    Pattern('project', input_example),

On a View:

    # This block will be executed on first call
    if not app.input_queue:
        app.hang_in(message)
        app.input(message, 'name', 'Enter Project Name:')
        app.input(message, 'language', 'Enter Project Language: ',
                  ['python2', 'python3'])
        return app.print_next_input(message) # To return first message of queue

    # On next calls, this block wil be executed

    stay, response = app.next_input_queue(message)
    if stay:
        return response # Contains message from Input Command
    # Queue ended, now you could save resulting Project and exit view
    app.hang_out(message)
    return 'Project created: ' + response # Response contains user entries
'''
from collections import OrderedDict


class InputHandler:
    '''Adds Input Command to views'''
    def __init__(self, app):
        self.hang = dict()
        self.input_queue = dict()
        self.user_inputs = dict()
        self._app = app

    def set_hang(self, hang, hang_pattern):
        self.hang[hang_pattern] = hang

    def hang_in(self, message):
        '''Used in conjunction with HangUserPattern. Mantains app on the view'''
        self.hang[message.text].activate_hang(message)
        self.user_inputs[message.user.id] = dict()

    def hang_out(self, message, hang_pattern):
        self.hang[hang_pattern].deactivate_hang(message)
        self.user_inputs.pop(message.user.id, None)

    def input(self, message, name, prompt, valid_values=None):
        '''Adds a input message to the dict'''
        if not self.input_queue.get(message.user.id, None):
            self.input_queue[message.user.id] = OrderedDict()
        self.user_inputs[message.user.id] = dict()
        user_input_dict = self.input_queue[message.user.id]
        user_input_dict[name] = (prompt, valid_values)

    def print_next_input(self, message):
        user_input_dict = self.input_queue[message.user.id]
        if not user_input_dict:
            return _('No messages on the input command queue')

        actual_prompt, _valid_values = list(user_input_dict.values())[0]
        print(actual_prompt)
        return actual_prompt

    def next_input_queue(self, message):
        '''Validates user input, saves user input.
         Returns a "stay" flag to say if views mantains hang or not
         Returns actual prompt OR
          a dict of name:user_input on end of prompts'''
        user_input_dict = self.input_queue[message.user.id]
        if not user_input_dict:
            return False, _('No messages on the input command queue')

        _actual_prompt, valid_values = list(user_input_dict.values())[0]
        if valid_values:
            if message.text not in valid_values:
                # If validation fail, remain on actual item
                return True, _('Enter a Valid Value: ') + ' '.join(valid_values)

        user_inputs = self.user_inputs[message.user.id]
        name = list(user_input_dict.keys())[0]
        user_inputs[name] = message.text
        user_input_dict.popitem(last=False)
        if not user_input_dict:
            # Ended! Return what user entered
            return False, user_inputs

        next_prompt, valid_values = list(user_input_dict.values())[0]
        if valid_values:
            next_prompt = next_prompt + ' - ' + ' '.join(valid_values)
        return True, next_prompt
