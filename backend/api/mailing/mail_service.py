# -*- coding: utf-8 -*-
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from api.settings import DEFAULT_FROM_EMAIL, BASE_FRONTEND_SITE_URL


class EmailSender:

    SUBJECT_REGISTRATION = _('[Orion Vault] - Private sale')
    TEMPLATE_REGISTRATION = 'mailing/private_sale_register.html'

    @classmethod
    def send_template_mail(cls, template, context, subject, target_emails, from_email=DEFAULT_FROM_EMAIL):
        context.update({
            'BASE_SITE_URL': BASE_FRONTEND_SITE_URL
        })
        html = render_to_string(template, context)
        subject = "{}".format(subject)
        mail = EmailMessage(subject, html, from_email, target_emails)
        mail.content_subtype = 'html'
        return mail.send()
