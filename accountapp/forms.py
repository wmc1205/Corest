from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].label ="패스워드"
        self.fields['password'].help_text = "패스워드는 대,소문자를 구별합니다."
        self.fields['username'].disabled = True