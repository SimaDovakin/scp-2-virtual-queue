from django.shortcuts import render

from .models import Queue


def dashboard(request):
    all_queues = Queue.objects.order_by('-created_at')

    context = {'all_queues': all_queues}
    return render(request, 'queues/dashboard.html', context)
