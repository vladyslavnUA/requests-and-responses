from django import forms
from wiki.models import Page
from .models import Question


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page

class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = QuestionCreateForm
        fields = ['question_text', 'pub_date']