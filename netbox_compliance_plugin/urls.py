from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("compliances/", views.ComplianceListView.as_view(), name="compliance_list"),
    path("compliances/add/", views.ComplianceEditView.as_view(), name="compliance_add"),
    path("compliances/<int:pk>/", views.ComplianceView.as_view(), name="compliance"),
    path("compliances/<int:pk>/edit/", views.ComplianceEditView.as_view(), name="compliance_edit"),
    path("compliances/<int:pk>/delete/", views.ComplianceDeleteView.as_view(), name="compliance_delete"),
    path(
        "compliances/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="compliance_changelog",
        kwargs={"model": models.Compliance},
    ),
)
