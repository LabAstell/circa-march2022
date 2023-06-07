from django.shortcuts import render


def start_circa(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'start_circa.html')









# Create your views here.
