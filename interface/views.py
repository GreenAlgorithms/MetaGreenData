from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import yaml

from .forms import HARDWARE_BOUNDARY_CHOICES, SOFTWARE_BOUNDARY_CHOICES, OperationalImpactValues


def index(request):
    return render(request, "home.html")

def convert_response_to_yml(response_dict):
    output_dict = {}

    output_dict["computing"] = {}

    output_dict["computing"]["operational"] = {}

    #Impact values
    output_dict["computing"]["operational"]["impact_values"] = {}
    output_dict["computing"]["operational"]["impact_values"]["energy_consumption"] = response_dict.get("energy_consumption")
    output_dict["computing"]["operational"]["impact_values"]["carbon_footprint"] = response_dict.get("carbon_footprint")
    output_dict["computing"]["operational"]["impact_values"]["water_consumption"] = response_dict.get("water_consumption")

    #methods
    output_dict["computing"]["operational"]["methods"] = {}
    hardware_boundary_choices = response_dict.getlist("hardware_boundaries")
    software_boundary_choices = response_dict.getlist("software_boundaries")
    output_dict["computing"]["operational"]["methods"]["hardware_boundaries"] = [v for (k, v) in HARDWARE_BOUNDARY_CHOICES if k in hardware_boundary_choices]
    output_dict["computing"]["operational"]["methods"]["software_boundaries"] = [v for (k, v) in SOFTWARE_BOUNDARY_CHOICES if k in software_boundary_choices]
    output_dict["computing"]["operational"]["methods"]["details_of_hardware"] = response_dict.get("details_of_hardware")
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"] = {}
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"]["value"] = response_dict.get("electrical_carbon_intensity")
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"]["source"] = response_dict.get("electrical_carbon_intensity_source")

    return output_dict
    
    
def get_metadata(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
            # create a form instance and populate it with data from the request:
        form = OperationalImpactValues(request.POST)
        if form.is_valid():
            yml_formatted_dict = convert_response_to_yml(request.POST)
            return download_yaml(yml_formatted_dict)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OperationalImpactValues()

    return render(request, "metadata.html", {"form": form})


def download_yaml(dict):
    yaml_content = yaml.dump(dict, sort_keys=False)

    response = HttpResponse(yaml_content, content_type='application/x-yaml')
    response['Content-Disposition'] = 'attachment; filename="data.yaml"'
    return response
