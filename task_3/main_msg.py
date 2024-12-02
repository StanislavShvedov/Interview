from message_model import Massanger
from config import GMAIL_SMTP, GMAIL_IMAP

if __name__ == '__main__':
    messanger = Massanger()
    messanger.create_message('sub', 'text', GMAIL_SMTP)
    messanger.search_msg(GMAIL_IMAP, 'header')
