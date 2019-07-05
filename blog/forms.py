from django import forms

from .models import Post
from django.core.validators import EmailValidator
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class FeedbackForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100, required=True)
    your_mail = forms.EmailField(label="Your e-mail", validators=[EmailValidator(message="doommain",whitelist="softcatalyst.com")])
    your_feedback = forms.CharField(label="Your feedback")


    def clean_your_mail(self):
        data = self.cleaned_data['your_mail']
        domain = data.split('@')[1]
        domain_list = ["softcatalyst.com"]
        if domain not in domain_list:
            raise forms.ValidationError("Email is invalid. The email should be a softcatalyst email")
        return data
