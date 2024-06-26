from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import Compliance


class ComplianceForm(NetBoxModelForm):
    class Meta:
        model = Compliance
        fields = ("name", "tags")
