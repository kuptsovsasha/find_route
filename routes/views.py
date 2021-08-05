from django.contrib import messages
from django.shortcuts import render
from routes.forms import RouteForm
from routes.utils import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
        return render(request, 'routes/home.html', context)
    else:
        form = RouteForm()
        messages.error(request, 'No data to save')
        return render(request, 'routes/home.html', {'form': form})


