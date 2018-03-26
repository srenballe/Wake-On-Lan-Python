from django.shortcuts import render
from .models import *
from wol import wake_on_lan

def home(request):
    context = {}
    context['devices'] = Device.objects.all()
    context['broadcast'] = Broadcast.objects.get(pk=1)

    return render(request, 'core/index.html', {'context': context})

def start(request, id):
    device = Device.objects.get(pk=id)
    broadcast = Broadcast.objects.get(pk=1)
    context = {}
    try:
        if wake_on_lan(device.mac, broadcast.ip):
            context['message'] = "Magic package is on the way!"
    except ValueError as e:
        context['message'] = "Error: Incorrect address format."
        return render(request, 'core/index.html', {'context': context})
    except Exception as e: #TODO: Correct exceptionhandling
        context['message'] = "Error: Network unreachable."
        return render(request, 'core/index.html', {'context': context})

    return render(request, 'core/index.html', {'context': context})

