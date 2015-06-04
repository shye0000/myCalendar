from django import forms
from calendarApp.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput  
      
class LoginForm(forms.Form):  
    username = forms.CharField(  
        required=True,  
        label=u"Username",  
        error_messages={'Required': 'Please insert username.'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"username",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"Password",  
        error_messages={'Required': u'Please insert password.'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }  
        ),  
    )     
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"Username and Password are required.")  
        else:  
            cleaned_data = super(LoginForm, self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField(  
        required=True,  
        label=u"Username",  
        error_messages={'Required': 'Please insert username.'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"username",  
            }  
        ),  
    ) 
    firstname = forms.CharField(  
        required=True,  
        label=u"First name",  
        error_messages={'Required': 'Please insert Firstname.'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"first name",  
            }  
        ),  
    )     
    lastname = forms.CharField(  
        required=True,  
        label=u"Last name",  
        error_messages={'Required': 'Please insert Lastname.'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"last name",  
            }  
        ),  
    )          
    password = forms.CharField(  
        required=True,  
        label=u"Password",  
        error_messages={'Required': u'Please insert password.'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }  
        ),  
    )     
    password2 = forms.CharField(  
        required=True,  
        label=u"Repeat Password",  
        error_messages={'Required': u'Please insert again the password.'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"repeat password",  
            }  
        ),  
    )
    email = forms.EmailField(
        required=True,
        label=u"Email",
        error_messages={'Required':u'Please insert an Email.'},
        widget=forms.EmailInput(
            attrs={
                'placeholder':u"email",
            }
        ),
    )

