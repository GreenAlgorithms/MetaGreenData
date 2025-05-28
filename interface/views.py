from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
import yaml
import json

from .forms import (
    HARDWARE_BOUNDARY_CHOICES, 
    SOFTWARE_BOUNDARY_CHOICES, 
    BasicInformationForm,
    EmbodiedImpactForm, 
    OperationalImpactForm
)
from .models import BasicInformation

def index(request):
    return render(request, "home.html")


def get_yml_preview(request):
    try:
        # Get form data from request
        data = {
            'title': request.GET.get('title', ''),
            'description': request.GET.get('description', ''),
            'keywords': [k.strip() for k in request.GET.get('keywords', '').split(',') if k.strip()],
            'repository': request.GET.get('repository_url', ''),
            'Computing': {
                'Embodied': {
                    'Carbon footprint': {
                        'Value (in gCO2e)': request.GET.get('carbon_footprint', ''),
                        'Source and method': request.GET.get('carbon_footprint_source', '')
                    },
                    'Depletion of Abiotic Resources (Minerals, Metals)': {
                        'Value (in kg Sb-eq)': request.GET.get('depletion_abiotic', ''),
                        'Source and method': request.GET.get('depletion_abiotic_source', '')
                    },
                    'Particule Matter Emissions': {
                        'Value (disease incidence)': request.GET.get('particulate_matter', ''),
                        'Source and method': request.GET.get('particulate_matter_source', '')
                    },
                    'Acidification potential': {
                        'Value (in kg mol H+)': request.GET.get('acidification_potential', ''),
                        'Source and method': request.GET.get('acidification_potential_source', '')
                    },
                    'Ionising Radiation Related to Human Health': {
                        'Value (in kBq U-235)': request.GET.get('ionising_radiation', ''),
                        'Source and method': request.GET.get('ionising_radiation_source', '')
                    },
                    'Photochemical Ozone Formation': {
                        'Value (in kg NMVOC-eq)': request.GET.get('photochemical_ozone', ''),
                        'Source and method': request.GET.get('photochemical_ozone_source', '')
                    },
                    'Abiotic Depletion Potential (Fossil Fuels)': {
                        'Value (in MJ)': request.GET.get('abiotic_depletion_fossil', ''),
                        'Source and method': request.GET.get('abiotic_depletion_fossil_source', '')
                    },
                    'Freshwater Eco-Toxicity Potential': {
                        'Value (in CTUe)': request.GET.get('freshwater_ecotoxicity', ''),
                        'Source and method': request.GET.get('freshwater_ecotoxicity_source', '')
                    }
                },
                'Operational': {
                    'Impact values': {
                        'Energy consumption (in kWh)': request.GET.get('energy_consumption', ''),
                        'Carbon footprint (in gCO2e)': request.GET.get('operational-carbon_footprint', ''),
                        'Water consumption (in liters)': request.GET.get('water_consumption', '')
                    },
                    'Methods and scope': {
                        'Software boundaries': {
                            'Stages included': request.GET.getlist('software_boundaries[]', [])
                        },
                        'Tool stages': {
                            'Stages included': request.GET.getlist('tool_stages[]', [])
                        },
                        'Hardware boundaries': {
                            'Components included': request.GET.getlist('hardware_boundaries[]', []),
                            'Details on hardware used': request.GET.get('details_of_hardware', '')
                        },
                        'Infrastructure': {
                            'Elements included': request.GET.getlist('infrastructure_elements[]', []),
                            'Power Usage Effectiveness (PUE)': {
                                'Value': request.GET.get('pue_value', ''),
                                'Estimation method used': request.GET.get('pue_method', '')
                            },
                            'Water usage effectiveness': {
                                'Value (in L/kWh)': request.GET.get('wue_value', ''),
                                'Estimation method used': request.GET.get('wue_method', '')
                            }
                        },
                        'Electricity carbon intensity': {
                            'Value (in gCO2e/kWh)': request.GET.get('electrical_carbon_intensity', ''),
                            'Source': request.GET.get('electrical_carbon_intensity_source', '')
                        }
                    }
                }
            }
        }

        # Remove empty values
        def clean_dict(d):
            if isinstance(d, dict):
                return {k: clean_dict(v) for k, v in d.items() if v not in ['', [], None, {}]}
            elif isinstance(d, list):
                return [x for x in d if x not in ['', None]]
            return d
        
        data = clean_dict(data)
        
        # Convert to YAML
        yml_content = yaml.dump(data, sort_keys=False, allow_unicode=True)
        return JsonResponse({'success': True, 'yml': yml_content})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def download_yml(request):
    try:
        response = get_yml_preview(request)
        if response.status_code == 200:
            data = json.loads(response.content)
            yml_content = data['yml']
            
            # Create response
            response = HttpResponse(yml_content, content_type='application/x-yaml')
            filename = request.GET.get('title', 'metadata').lower().replace(' ', '_')
            response['Content-Disposition'] = f'attachment; filename="{filename}.yml"'
            return response
        else:
            return response
    
    except Exception as e:
        return HttpResponse(str(e), status=400)

def work_in_progress(request, form_type):
    return render(request, "work_in_progress.html", {'form_type': form_type})

def computing_form_view(request):
    if request.method == 'POST':
        # Handle form submission based on the current step
        step = request.POST.get('step', 'basic')
        
        if step == 'basic':
            form = BasicInformationForm(request.POST)
            if form.is_valid():
                basic_info = form.save()
                return JsonResponse({'success': True, 'id': basic_info.id})
        
        elif step in ['embodied', 'operational']:
            if step == 'embodied':
                form = EmbodiedImpactForm(request.POST, prefix='embodied')
            else:
                form = OperationalImpactForm(request.POST, prefix='operational')
            
            if form.is_valid():
                impact = form.save()
                return JsonResponse({'success': True, 'id': impact.id})
    
    # Initialize forms for GET request
    context = {
        'basic_form': BasicInformationForm(),
        'embodied_form': EmbodiedImpactForm(prefix='embodied'),
        'operational_form': OperationalImpactForm(prefix='operational'),
    }
    return render(request, 'computing.html', context)
