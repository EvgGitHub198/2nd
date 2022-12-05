from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Рады приветствовать вас! Спасибо, что подписались на нашу рассылку! Не отвечайте на это письмо, оно сгенерировано автоматически.',
        'mishagon02@gmail.com',
        [user_email],
        fail_silently=False,
    )

