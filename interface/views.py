from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import OperationalImpactValues


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
    output_dict["computing"]["operational"]["methods"]["software_boundaries"] = response_dict.get("software_boundaries")
    output_dict["computing"]["operational"]["methods"]["hardware_boundaries"] = response_dict.get("hardware_boundaries")
    output_dict["computing"]["operational"]["methods"]["details_of_hardware"] = response_dict.get("details_of_hardware")
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"] = {}
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"]["value"] = reponse_dict.get("electrical_carbon_intensity")
    output_dict["computing"]["operational"]["methods"]["electrical_carbon_intensity"]["source"] = reponse_dict.get("electrical_carbon_intensity_source")

    return output_dict
    
    
def get_metadata(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = OperationalImpactValues(request.POST)
        yml_formatted_dict = convert_response_to_yml(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "thanks.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OperationalImpactValues()

    return render(request, "metadata.html", {"form": form})

    
