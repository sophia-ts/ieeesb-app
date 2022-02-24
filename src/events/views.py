from django.shortcuts import render, get_object_or_404
from .models import Event
from django.core.paginator import Paginator


# def index(request):
#     events = Event.objects.all()
#     context = {
#         "events": events,
#     }
#     return render(request, "events/index.html", context)


def event(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        "event": event,
    }
    return render(request, "events/event.html", context)


def index(request):
    event_list = Event.objects.all().order_by('-date')
    paginator = Paginator(event_list, 3)  # Show 3 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "events/index.html", {"page_obj": page_obj})
