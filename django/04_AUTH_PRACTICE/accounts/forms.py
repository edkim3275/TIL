from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.forms import get_user_model
from django.contrib.auth import get_user_model


# get_user_model()은 관습!
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)