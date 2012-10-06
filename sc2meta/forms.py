from sc2meta.models import UserProfile
from django.forms import ModelForm
from django import forms

from sc2meta.widgets import jQueryDateField


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user')