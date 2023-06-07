from django.shortcuts import render
from .models import Theme, subtheme_I, subtheme_V, subtheme_A, Image, Video, Audio
import random

#HYPERPRARMETERS 
numberOfThemes = 3 


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    themes = Theme.objects.all()
    randomlySelectedThemes = random.sample(list(themes), 3)
   
    subthemeA_I = subtheme_I.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_I = subtheme_I.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_I = subtheme_I.objects.filter(theme=randomlySelectedThemes[2])
    
    subthemeA_V = subtheme_V.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_V = subtheme_V.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_V = subtheme_V.objects.filter(theme=randomlySelectedThemes[2])

    subthemeA_A = subtheme_A.objects.filter(theme=randomlySelectedThemes[0])
    subthemeB_A = subtheme_A.objects.filter(theme=randomlySelectedThemes[1])
    subthemeC_A = subtheme_A.objects.filter(theme=randomlySelectedThemes[2])

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
    return render(request, 'index.html', context=context)

def image_detail(request,pk):
    images = Image.objects.filter(subtheme__pk=pk)
    context = {
        'images': images
    }
    return render(request, 'image_detail.html', context)

def video_detail(request,pk):
    videos = Video.objects.filter(subtheme__pk=pk)
    context = {
        'videos': videos
    }
    return render(request, 'video_detail.html', context)

def audio_detail(request,pk):
    audio = Audio.objects.filter(subtheme__pk=pk)
    context = {
        'audio': audio
    }
    return render(request, 'audio_detail.html', context)




# Create your views here.
