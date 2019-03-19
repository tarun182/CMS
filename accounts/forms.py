from django import forms
from django.contrib.auth import ( 
    authenticate,
    get_user_model
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username= forms.CharField(max_length=50, required=True)
    password= forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        super().clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        
        if username and password:
            user = authenticate(username=username, password=password)
            
            #if not user.check_username(username):
                #raise forms.ValidationError('this user does not exist')
  
            try:
                user.check_password(password)!=True
            except:
                raise forms.ValidationError('Incorrect Password') 
            if not user:
                raise forms.ValidationError('this user does not exist')


class UserRegisterForm(forms.ModelForm):
    email=forms.EmailField(label="email address", required=True)
    email2=forms.EmailField(label="confirm email", required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
    
    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Email addresses must match!')
            
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email address already registered!')












