from netbox.filtersets import NetBoxModelFilterSet
from .models import Compliance


# class ComplianceFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = Compliance
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
