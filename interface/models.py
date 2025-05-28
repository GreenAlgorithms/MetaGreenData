from django.db import models

class BasicInformation(models.Model):
    title = models.CharField("Project Title", max_length=255)
    description = models.TextField("Project Description")
    keywords = models.CharField("Keywords (comma-separated)", max_length=255)
    repository_url = models.URLField("Repository URL", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE, related_name='authors')
    name = models.CharField("Full Name", max_length=255)
    email = models.EmailField("Email Address")
    affiliation = models.CharField("Affiliation", max_length=255, blank=True)
    orcid = models.CharField("ORCID", max_length=19, blank=True)
    is_corresponding = models.BooleanField("Corresponding Author", default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class EmbodiedImpact(models.Model):
    carbon_footprint = models.FloatField("Carbon footprint (gCO2e)", null=True, blank=True)
    carbon_footprint_source = models.CharField("Source and method (carbon footprint)", max_length=255, blank=True)
    depletion_abiotic = models.FloatField("Depletion of Abiotic Resources (kg Sb-eq)", null=True, blank=True)
    depletion_abiotic_source = models.CharField("Source and method (depletion)", max_length=255, blank=True)
    particulate_matter = models.FloatField("Particulate Matter Emissions (disease incidence)", null=True, blank=True)
    particulate_matter_source = models.CharField("Source and method (particulate matter)", max_length=255, blank=True)
    acidification_potential = models.FloatField("Acidification potential (kg mol H+)", null=True, blank=True)
    acidification_potential_source = models.CharField("Source and method (acidification)", max_length=255, blank=True)
    ionising_radiation = models.FloatField("Ionising Radiation (kBq U-235)", null=True, blank=True)
    ionising_radiation_source = models.CharField("Source and method (ionising radiation)", max_length=255, blank=True)
    photochemical_ozone = models.FloatField("Photochemical Ozone Formation (kg NMVOC-eq)", null=True, blank=True)
    photochemical_ozone_source = models.CharField("Source and method (ozone)", max_length=255, blank=True)
    abiotic_depletion_fossil = models.FloatField("Abiotic Depletion Potential (MJ)", null=True, blank=True)
    abiotic_depletion_fossil_source = models.CharField("Source and method (fossil fuels)", max_length=255, blank=True)
    freshwater_ecotoxicity = models.FloatField("Freshwater Eco-Toxicity Potential (CTUe)", null=True, blank=True)
    freshwater_ecotoxicity_source = models.CharField("Source and method (ecotoxicity)", max_length=255, blank=True)

class OperationalImpact(models.Model):
    energy_consumption = models.FloatField("Energy consumption (kWh)", null=True, blank=True)
    carbon_footprint = models.FloatField("Carbon footprint (gCO2e)", null=True, blank=True)
    water_consumption = models.FloatField("Water consumption (liters)", null=True, blank=True)
