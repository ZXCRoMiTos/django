from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms.widgets import HiddenInput
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super(ShopUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password", "email", "first_name", "last_name", "age", "avatar")

    def __init__(self, *args, **kwargs):
        super(ShopUserChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()
                continue
            field.widget.attrs['class'] = 'form-control'