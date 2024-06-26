import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import Compliance


class ComplianceTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Compliance
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
