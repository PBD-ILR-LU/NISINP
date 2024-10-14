from django import forms

# from django.utils.translation import gettext_lazy as _

# from .models import RiskAnalysisJson


# to upload the JSON
class RiskAnalysisSubmissionForm(forms.Form):
    files = forms.FileField(
        widget=forms.TextInput(
            attrs={
                "type": "File",
                "multiple": "True",
            }
        )
    )

    # class Meta:
    #     model = RiskAnalysisJson
    #     fields = ["data"]
    #     labels = {
    #         "data": _("Upload JSON File"),
    #     }
    #     widgets = {
    #         "data": forms.FileInput(attrs={"accept": ".json"}),
    #     }