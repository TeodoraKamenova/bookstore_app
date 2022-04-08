import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserChangeForm

from bookstore_app.accounts.models import Profile


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )
    image_URL = forms.URLField()

    gender = forms.ChoiceField(
        choices=Profile.GENDER_CHOICES,
    )

    date_of_birth = forms.DateField(initial=datetime.date.today)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['gender'] = Profile.GENDER_DO_NOT_SHOW

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            image_URL=self.cleaned_data['image_URL'],
            gender=self.cleaned_data['gender'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'image_URL', 'gender',
                  'date_of_birth', )


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_URL', 'gender', 'date_of_birth')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'image_URL': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                    'max': datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day),
                }
            )
        }


class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = Profile
        fields = ()


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()




