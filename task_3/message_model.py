import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Massanger():
    """
    Класс для отправки и получения писем через электронную почту
    """

    def __init__(self):
        """
        Инициализируем поля класса
        login: логин
        passowrd: пароль
        recipients: адреса получателей
        msg: объект письма
        """
        self.login = 'login@gmail.com'
        self.password = 'qwerty'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.msg = MIMEMultipart()

    def create_message(self, subject: str, message: str, server_adress: str, port: int = 587) -> None:
        """
        Метод для создания объекта письма и его отправления
        :param subject: string (тема письма)
        :param message: string (текст письма)
        :param server_adress: string (адрес сервера)
        :param port: int (значение по умолчанию)
        :return: None
        """
        self.msg['From'] = self.login
        self.msg['To'] = ', '.join(self.recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))

        ms = smtplib.SMTP(server_adress, port)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, self.msg.as_string())
        ms.quit()

    def search_msg(self, server_adress: str, header: str = ''):
        """
        Метод класса для поиска письмем, позволяет искать по указанному заголовку
        :param server_adress: string (адрес сервера)
        :param header: string (значение по умолчанию, при получении аргумента осуществляет поиск по указанному значению)
        :return: None
        """
        mail = imaplib.IMAP4_SSL(server_adress)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
