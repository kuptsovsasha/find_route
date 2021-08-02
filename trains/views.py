from datetime import timezone

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from trains.forms import TrainForm
from trains.models import Train


__all__ = ('home', 'TrainListView', 'TrainDetailView', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView', 'TrainListView')


def home(request, pk=None):

    qs = Train.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}

    return render(request, "trains/home.html", context)



class TrainListView(ListView):
    paginate_by = 2
    model = Train
    template_name = "trains/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TrainForm()
        context['form'] = form
        return context



class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = "trains/detail.html"
#
#
class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/create.html"
    success_url = reverse_lazy('cities:home')
    success_message = "Train creating successful"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/update.html"
    success_url = reverse_lazy('trains:home')
    success_message = "Train editing successful"


class TrainDeleteView(DeleteView):
    model = Train

    template_name = "trains/delete.html"
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Train deleted successful')
        return self.post(request, *args, **kwargs)


