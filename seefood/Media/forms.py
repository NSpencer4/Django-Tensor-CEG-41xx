from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method='post'
        self.helper.form_action = 'Media:createUser'

        self.helper.layout = Layout(
            'email',
            'username',
            'password1',
            'password2',

            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
