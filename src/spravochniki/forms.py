from django import forms
from . import models
from django.core.exceptions import ValidationError
CHOISES = [(obj.pk, obj.name) for obj in models.Region.objects.all()]

def if_microsoft(data):
    if data[-14:] != "@microsoft.com":
        raise ValidationError(
            "The addres must be like this **@microsoft.com"
        )

class AddCityForm(forms.Form):
    region = forms.ChoiceField(
        choices=CHOISES,
        required=True,
        label="Pls select a Region",
        help_text="select a Region here"
    )
    name = forms.CharField(
        max_length=255,
        required=True,
        label="Pls add a name"
    )

    def save(self):
        region = models.Region.objects.get(
            pk=self.cleaned_data["region"], 
        )
        return models.City.objects.create(
            region=region, 
            name=self.cleaned_data["name"]
        )
    
class CityModelForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = [
            "region", "name"
        ]

class ContactForm(forms.Form):
    cintact_email = forms.EmailField(
        required=True,
        label="Pls enter your email", 
        validators=[
            if_microsoft
        ]           
    )
    message = forms.CharField(
        required=True,
        label="Pls enter your message",
        widget=forms.Textarea,
    )