from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

import events
from .models import Event, Review
from datetime import datetime
from accounts.models import UserProfile

# Create your views here.

def get_user_profile(request):
    if request.user.is_authenticated:
        [profile, created] = UserProfile.objects.get_or_create(user=request.user)
        return profile

def details(request, id):
    eventsFromDB = get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {"event":eventsFromDB})

def new_review(request, id):
    event  = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        rating = request.POST['rating']
        text = request.POST['text']
        new_review = Review(
            rating = rating,
            text = text,
            event = event,
            user_profile = get_user_profile(request)
        )
        new_review.save()
        return redirect('/events')


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

def dashboard(request):
    today = datetime.today()
    user_profile = get_user_profile(request)

    get_future_attend = user_profile.attending
    future_attend= get_future_attend.filter(
        datetime__gte=today).order_by('datetime')

    get_past_attend = user_profile.attending
    past_attend = get_past_attend.filter(
        datetime__lt=today).order_by('datetime')
    return render(request, 'events/dashboard.html',{'events': future_attend, 'past_events':past_attend})

@login_required
def add_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(event)
    return redirect("events_list")


@login_required
def remove_attending(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(event)
    return redirect("events_list")