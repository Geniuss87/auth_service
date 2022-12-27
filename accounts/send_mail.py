from django.core.mail import send_mail


def send_message_to_mail(email):

    send_mail(
        'test',
        'Activation code',
        'ashyrov.n@mail.ru',
        [email, ],
        fail_silently=False,
    )
