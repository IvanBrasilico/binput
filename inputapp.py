import sys
import logging.config
from bottery.app import App
from bottery.log import DEFAULT_LOGGING
from botteryext.binput.inputhandler import InputHandler
import botteryext.binput.localizations


app = App()
ih = InputHandler(App)


if __name__ == '__main__':
    logging.config.dictConfig(DEFAULT_LOGGING)
    logger = logging.getLogger('bottery')
    if len(sys.argv) > 1:
        if sys.argv[1] == '--debug':
            logger.setLevel(logging.DEBUG)

    app.run()
