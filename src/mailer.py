from flask_mail import Mail, Message


class Mailer:
    def __init__(self, flask_app):
        self._mail = Mail(flask_app)

    def send_contact_mail(self, message_subj, recipient_email, message, service_email):
        msg = Message(
            subject=message_subj,
            sender=service_email,
            recipients=[recipient_email],
            body=f'''You have received a new message from {recipient_email}:
            {message}'''
        )
        self._mail.send(msg)

    def send_confirmation_mail(self, service_email, recipient_email, name):
        msg = Message(
            subject="Thanks for contacting me!",
            sender=service_email,
            recipients=[recipient_email],
            body=f'''Hey there {name}!\n Thanks for reaching out to me. I will get back to you as soon as possible.'''
        )
        self._mail.send(msg)
