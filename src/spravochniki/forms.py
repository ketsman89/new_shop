from django import forms
from . import models
CHOISES = [(obj.pk, obj.name) for obj in models.Region.objects.all()]
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