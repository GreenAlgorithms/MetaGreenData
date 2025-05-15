from django import forms


class MetaDataForm(forms.Form):
    meta1 = forms.CharField(label="Meta data 1", max_length=100)
    meta2 = forms.CharField(label="Meta data 2", max_length=100)
    meta3 = forms.CharField(label="Meta data 3", max_length=100)


class OperationalImpactValues(forms.Form):
    energy_consumption = forms.FloatField(label="Energy consumption (in kWh)")
    carbon_footprint = forms.FloatField(label="Carbon footprint (in gCO2e)")
    water_consumption = forms.FloatField(label="Water consumption (in litres)")
    hardware_boundary_choices = (
        ("1", "CPUs"),
        ("2", "GPUs"),
        ("3", "Memory"),
        ("4", "Storage"),
        ("4", "Networking"),
    )
    hardware_boundaries = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=hardware_boundary_choices
    )
    details_of_hardware = forms.CharField(label="Hardware description", max_length=5000)
    
