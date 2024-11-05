import django_filters
from django.db.models import F, Q

from governanceplatform.models import Sector

from .forms import (
    DropdownCheckboxSelectMultiple,
    IncidentStatusForm,
    IncidentWorkflowForm,
)
from .models import Incident, SectorRegulation


# define specific query to get the regulation
def sector_regulation(request):
    return SectorRegulation.objects.distinct()


class IncidentFilter(django_filters.FilterSet):
    incident_id = django_filters.CharFilter(lookup_expr="icontains")
    affected_sectors = django_filters.ModelMultipleChoiceFilter(
        queryset=Sector.objects.filter(
            ~Q(
                id__in=Sector.objects.exclude(parent=None).values_list(
                    "parent_id", flat=True
                )
            )
            | Q(id=F("parent_id"))
        ).order_by("parent"),
        widget=DropdownCheckboxSelectMultiple(
            attrs={"data-selected-text-format": "count > 2"}
        ),
    )
    sector_regulation = django_filters.ModelChoiceFilter(queryset=sector_regulation)

    class Meta:
        model = Incident
        fields = [
            "incident_id",
            "incident_status",
            "is_significative_impact",
            "affected_sectors",
            "sector_regulation",
        ]

    # Needed to add the form for modification of
    # incident_id, incident_status and significative impact
    @property
    def qs(self):
        parent = super().qs

        for incident in parent:
            incident.formsWorkflow = []
            for workflow_completed in incident.get_workflows_completed():
                incident.formsWorkflow.append(
                    IncidentWorkflowForm(instance=workflow_completed)
                )
            incident.formsStatus = IncidentStatusForm(
                instance=incident,
            )

        return parent
