from django.shortcuts import render
from .models import Theme_CN, subtheme_I_CN, subtheme_V_CN, subtheme_A_CN, Image_CN, Video_CN, Audio_CN
import random

#HYPERPRARMETERS 
numberOfThemes = 3 


def index_CN(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    themes = Theme_CN.objects.all()
    randomlySelectedThemes = random.sample(list(themes), 3)
   
    subthemeA_I = subtheme_I_CN.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_I = subtheme_I_CN.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_I = subtheme_I_CN.objects.filter(theme=randomlySelectedThemes[2])
    
    subthemeA_V = subtheme_V_CN.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_V = subtheme_V_CN.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_V = subtheme_V_CN.objects.filter(theme=randomlySelectedThemes[2])

    subthemeA_A = subtheme_A_CN.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_A = subtheme_A_CN.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_A = subtheme_A_CN.objects.filter(theme=randomlySelectedThemes[2])

    context = {
        'themeA'      :randomlySelectedThemes[0],
        'themeB'      :randomlySelectedThemes[1],
        'themeC'      :randomlySelectedThemes[2],
        'subthemeA_I' :subthemeA_I,
        'subthemeB_I' :subthemeB_I,
        'subthemeC_I' :subthemeC_I,
        'subthemeA_V' :subthemeA_V,
        'subthemeB_V' :subthemeB_V,
        'subthemeC_V' :subthemeC_V,
        'subthemeA_A' :subthemeA_A,
        'subthemeB_A' :subthemeB_A,
        'subthemeC_A' :subthemeC_A,
        }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index_CN.html', context=context)

def image_detail_CN(request,pk):
    images = Image_CN.objects.filter(subtheme__pk=pk)
    context = {
        'images': images
    }
    return render(request, 'image_detail_CN.html', context)

def video_detail_CN(request,pk):
    videos = Video_CN.objects.filter(subtheme__pk=pk)
    context = {
        'videos': videos
    }
    return render(request, 'video_detail_CN.html', context)

def audio_detail_CN(request,pk):
    audio = Audio_CN.objects.filter(subtheme__pk=pk)
    context = {
        'audio': audio
    }
    return render(request, 'audio_detail_CN.html', context)




# Create your views here.
