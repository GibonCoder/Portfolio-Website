from flask_mail import Mail, Message


class Mailer:
    def __init__(self, flask_app):
        self._mail = Mail(flask_app)

    def send_contact_mail(self, cm_subj, rp_email, cm_message, cm_email):
        msg = Message(
            subject=cm_subj,
            recipients=[cm_email],
            body=f'''You have received a new message from {rp_email}:
            {cm_message}'''
        )
        self._mail.send(msg)

    def send_confirmation_mail(self, rp_email):
        msg = Message(
            subject="Thanks for contacting me!",
            recipients=[rp_email],
            body='''Hey there!\n Thanks for reaching out to me. I will get back to you as soon as possible.'''
        )
        self._mail.send(msg)
