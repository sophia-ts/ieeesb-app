from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator
from django.utils.timezone import datetime #important if using timezones

def event(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        "event": event,
    }
    return render(request, "events/event.html", context)


def index(request):
    event_upcomming_list = Event.objects.filter(date__gte = '2022-03-28').order_by("-date")
    event_past_list = Event.objects.filter(date__lt = '2022-03-28').order_by("-date")

    paginator_upcomming = Paginator(event_upcomming_list, 1)  # Show 1 contact per page.
    paginator_past = Paginator(event_past_list, 1)  # Show 3 contacts per page.

    page_number_upcomming = request.GET.get("page_upcomming")
    page_number_past = request.GET.get("page_past")
    
    page_upcomming_obj = paginator_upcomming.get_page(page_number_upcomming)
    page_past_obj = paginator_past.get_page(page_number_past)

    all_events = {"page_upcomming_obj": page_upcomming_obj,"page_past_obj": page_past_obj}
    return render(request, "events/index.html", {"all_events": all_events})

