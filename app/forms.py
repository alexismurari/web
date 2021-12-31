from wtforms import Form
from wtforms.fields.simple import StringField

"""Contact Form"""
class ContactForm(Form):
    message = StringField('Message:')