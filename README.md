# A Bottery Extension
:battery: Bottery - a framework for building bots

[![Build Status](https://travis-ci.org/IvanBrasilico/binput.svg?branch=master)](https://travis-ci.org/IvanBrasilico/binput)
[![CircleCI](https://circleci.com/gh/IvanBrasilico/binput/tree/master.svg?style=svg)](https://circleci.com/gh/IvanBrasilico/binput/tree/master)


```python
# quick example of a input bot
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
```

The complete example is packaged within this repository

* [Usage](#usage)
  * [Installing](#installing)
  * [Creating a project](#creating-a-project)


## Usage
Just import it on a bottery project. 
```python
# On bottery app
from botteryext.binput.inputhandler import InputHandler
import botteryext.binput.localizations

app = App()
ih = InputHandler(App)

# On patterns.py
from botteryext.binput.patterns import HangUserPattern
hang_user_pattern = HangUserPattern(aview)
ih.set_hang(hang_user_pattern, 'apattern')

patterns = [
    hang_user_pattern,
    Pattern('project', input_example),
***
# On views
from inputapp import ih
```

### Installing
```bash
$ git clone https://github.com/IvanBrasilico/binput.git
$ pip install -e .
```

### Creating a project 

Refer to [bottery](https://github.com/rougeth/bottery/) documentation




