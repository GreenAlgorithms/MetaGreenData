from django import forms
from .models import EmbodiedImpact, OperationalImpact, BasicInformation, Author

HARDWARE_BOUNDARY_CHOICES = (
    ("CPUs", "CPUs"),
    ("GPUs", "GPUs"),
    ("Memory", "Memory"),
    ("Storage", "Storage"),
    ("Networking", "Networking"),
)

SOFTWARE_BOUNDARY_CHOICES = (
    ("Development and testing", "Development and testing"),
    ("Deployment", "Deployment"),
    ("Use", "Use"),
    ("Maintenance", "Maintenance"),
)

INFRASTRUCTURE_ELEMENTS_CHOICES = (
    ("energy overheads", "Energy overheads"),
    ("idle machines", "Idle machines"),
    ("water usage", "Water usage"),
    ("IoT devices", "IoT devices"),
    ("edge devices", "Edge devices"),
)


class OperationalImpactForm(forms.Form):
    # Impact values
    energy_consumption = forms.FloatField(
        label="Energy consumption (in kWh)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'})
    )
    carbon_footprint = forms.FloatField(
        label="Carbon footprint (in gCO2e)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'})
    )
    water_consumption = forms.FloatField(
        label="Water consumption (in liters)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'})
    )

    # Methods and scope
    software_boundaries = forms.MultipleChoiceField(
        label="Software boundaries - Stages included",
        choices=SOFTWARE_BOUNDARY_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'})
    )
    
    tool_stages = forms.MultipleChoiceField(
        label="Tool stages included",
        choices=SOFTWARE_BOUNDARY_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
        required=False
    )
    
    hardware_boundaries = forms.MultipleChoiceField(
        label="Hardware boundaries - Components included",
        choices=HARDWARE_BOUNDARY_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'})
    )
    
    details_of_hardware = forms.CharField(
        label="Details on hardware used",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )
    
    infrastructure_elements = forms.MultipleChoiceField(
        label="Infrastructure elements included",
        choices=INFRASTRUCTURE_ELEMENTS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled'}),
        required=False
    )
    
    pue_value = forms.FloatField(
        label="Power Usage Effectiveness (PUE) Value",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number ≥ 1', 'min': '1'}),
        required=False
    )
    
    pue_method = forms.CharField(
        label="PUE Estimation method used",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    wue_value = forms.FloatField(
        label="Water Usage Effectiveness (WUE) Value (in L/kWh)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'}),
        required=False
    )
    
    wue_method = forms.CharField(
        label="WUE Estimation method used",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    electrical_carbon_intensity = forms.FloatField(
        label="Electrical Carbon Intensity Value (in gCO2e/kWh)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number'})
    )
    
    electrical_carbon_intensity_source = forms.CharField(
        label="Electrical Carbon Intensity Source",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class EmbodiedImpactForm(forms.ModelForm):
    class Meta:
        model = EmbodiedImpact
        fields = '__all__'
        widgets = {
            'carbon_footprint': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (gCO2e)'}),
            'carbon_footprint_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'depletion_abiotic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (kg Sb-eq)'}),
            'depletion_abiotic_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'particulate_matter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (disease incidence)'}),
            'particulate_matter_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'acidification_potential': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (kg mol H+)'}),
            'acidification_potential_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'ionising_radiation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (kBq U-235)'}),
            'ionising_radiation_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'photochemical_ozone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (kg NMVOC-eq)'}),
            'photochemical_ozone_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'abiotic_depletion_fossil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (MJ)'}),
            'abiotic_depletion_fossil_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'}),
            'freshwater_ecotoxicity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a number (CTUe)'}),
            'freshwater_ecotoxicity_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Source and method'})
        }

class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformation
        fields = ['title', 'description', 'keywords', 'repository_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'repository_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'affiliation', 'orcid', 'is_corresponding']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'affiliation': forms.TextInput(attrs={'class': 'form-control'}),
            'orcid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0000-0000-0000-0000'}),
            'is_corresponding': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

