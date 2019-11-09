from django.shortcuts import render, get_object_or_404
from .models import Landmark
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def landmark_list(request):
    lm = Landmark.objects.all()
    return render(request, 'sights/landmark/list.html', {'landmarks': lm})

def landmark_detail(request, name):
    landmark = get_object_or_404(Landmark, name=name)
    return render(request, 'sights/landmark/detail.html', {'landmark': landmark})

class LandmarkListView(ListView):
    queryset = Landmark.objects.all()
    context_object_name = 'landmarks'
    paginate_by = 3
    template_name = 'sights/landmark/list.html'