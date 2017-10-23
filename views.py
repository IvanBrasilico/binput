'''Custom views just for show example of Usage'''
from inputapp import ih


def help_text(message):
    '''List of available Patterns'''
    return (_('help - this help list') + '\n' +
            _('ping - test, returns "pong"') + '\n' +
            _('project - enters Project View') + '\n')


def say_help(message):
    '''Set as default - if no recognized command'''
    return _('Sorry, I did not understood you. \n'
             'Type "help" for a list of available commands')


def input_example(message):
    # ih.input(message, name, prompt, valid_values=[]) ->
    #   Creates an name entry in a OrderedDict with a tuple
    #   (prompt, valid_values)
    # user_session ->
    #   dict with returned user ihs
    if not ih.input_queue:
        ih.hang_in(message)
        ih.input(message, 'name', 'Enter Project Name:')
        ih.input(message, 'language', 'Enter Project Language: ',
                 ['python2', 'python3'])
        ih.input(message, 'site', 'Enter Project site:')
        ih.input(message, 'priority', 'Enter Project priority:',
                 ['insane', 'medium', 'dontmatter'])
        return ih.print_next_input(message)
    stay, response = ih.next_input_queue(message)
    if stay:
        return response
    # Now you could save resulting Project and exit view
    ih.hang_out(message, 'project')
    return 'Project created: ' + ' '.join('{}:{}'.format(key, val) for key, val in response.items())
