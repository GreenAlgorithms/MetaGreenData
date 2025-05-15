from django import forms

HARDWARE_BOUNDARY_CHOICES = (
        ("1", "CPUs"),
        ("2", "GPUs"),
        ("3", "Memory"),
        ("4", "Storage"),
        ("5", "Networking"),
    )

SOFTWARE_BOUNDARY_CHOICES = (
        ("1","Development and testing"),
        ("2","Deployment"),
        ("3","Use"),
        ("4","Maintenance"),
    )

class MetaDataForm(forms.Form):
    meta1 = forms.CharField(label="Meta data 1", max_length=100)
    meta2 = forms.CharField(label="Meta data 2", max_length=100)
    meta3 = forms.CharField(label="Meta data 3", max_length=100)


class OperationalImpactValues(forms.Form):
    energy_consumption = forms.FloatField(label="Energy consumption (in kWh)")
    carbon_footprint = forms.FloatField(label="Carbon footprint (in gCO2e)")
    water_consumption = forms.FloatField(label="Water consumption (in litres)")
    software_boundaries = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=SOFTWARE_BOUNDARY_CHOICES,
    )
    hardware_boundaries = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=HARDWARE_BOUNDARY_CHOICES
    )
    details_of_hardware = forms.CharField(label="Hardware description", max_length=5000)
    electrical_carbon_intensity = forms.FloatField(label="Electric carbon intensity (in gCO2e/kWh)")
    electrical_carbon_intensity_source = forms.CharField(label="Electric carbon intensity source", max_length=5000)
                                                   
