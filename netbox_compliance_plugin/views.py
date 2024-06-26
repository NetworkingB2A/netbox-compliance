from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class ComplianceView(generic.ObjectView):
    queryset = models.Compliance.objects.all()


class ComplianceListView(generic.ObjectListView):
    queryset = models.Compliance.objects.all()
    table = tables.ComplianceTable


class ComplianceEditView(generic.ObjectEditView):
    queryset = models.Compliance.objects.all()
    form = forms.ComplianceForm


class ComplianceDeleteView(generic.ObjectDeleteView):
    queryset = models.Compliance.objects.all()
