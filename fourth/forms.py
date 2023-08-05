from django import forms
from django.core.exceptions import ValidationError

from fourth.models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'not selected'

    class Meta:
        model = Man
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60,'rows':10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('title have very a lot of symbols')
        return title