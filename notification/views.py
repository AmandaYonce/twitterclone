from django.shortcuts import render
from .models import *


def NotificationView(request):
    notifs = Notification.objects.filter(at_person=request.user, read=False)
    for note in notifs:
        note.read = True
        note.save()
    return render(request, "notifications.html", {"notifs": notifs})
