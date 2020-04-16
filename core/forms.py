from django import forms

from core.models import Link
from core.util import adiciona_form_control


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        # exclude = ('url_encurtado','contador')

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)
