from django import template
from sendmail.forms import MailForm

register = template.Library()


@register.inclusion_tag('sendmail/tags/form.html')
def mail_form():
    return {"mail_form": MailForm()}
