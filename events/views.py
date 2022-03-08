from django.shortcuts import render, get_object_or_404
from .models import Event
from datetime import datetime
# Create your views here.

def details(request, id):
    eventsFromDB = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {"event":eventsFromDB})

def list(request):
    today =datetime.today()
    
    filter_map={
        'title': 'title__icontains',
        'is_free': 'cost__exact',
    }

    filters={ }
    
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value

    events= Event.objects.filter(
        datetime__gte=today).filter(**filters).order_by('datetime')
    # eventlist = Event.objects.all().order_by('datetime')
    return render(request, 'events/list.html', {"events": events})