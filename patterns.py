'''Configuration of the routes, or vocabulary of the bot'''
from inputapp import ih
from bottery.conf.patterns import Pattern, DefaultPattern
from bottery.views import pong
from botteryext.binput.patterns import HangUserPattern
from views import input_example, help_text, say_help


hang_user_pattern_input = HangUserPattern(input_example)

ih.set_hang(hang_user_pattern_input, 'project')

patterns = [
    hang_user_pattern_input,
    Pattern('project', input_example),
    Pattern('ping', pong),
    Pattern('help', help_text),
    DefaultPattern(say_help)
]
