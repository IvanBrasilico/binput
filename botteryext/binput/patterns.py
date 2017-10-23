'''Patterns needed for the behavior of Input Extension'''
from bottery.conf.patterns import DefaultPattern


class HangUserPattern(DefaultPattern):
    '''Creates a "Hang" to stay on the view while
    there are Input commands remaining'''

    def __init__(self, view):
        self.hanged_users = set()
        super().__init__(view)

    def activate_hang(self, message):
        '''Creates a dict entry vinculated to actual User'''
        self.hanged_users.add(message.user.id)

    def deactivate_hang(self, message):
        '''Releases dict entry vinculated to actual User'''
        self.hanged_users.discard(message.user.id)

    def check(self, message):
        if message is None:
            return _('Empty message')
        if message.user.id in self.hanged_users:
            return self.view
        return False
