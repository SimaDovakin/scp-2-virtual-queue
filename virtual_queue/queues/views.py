import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

from queues.forms import QueueForm
from queues.models import Queue, Location
from queues.services.queue import QueueService


def dashboard(request):
    all_queues = Queue.objects.order_by('-created_at')
    queue_form = QueueForm(use_required_attribute=False)

    context = {
        'all_queues': all_queues,
        'queue_form': queue_form
    }
    return render(request, 'queues/dashboard.html', context)


def create_queue(request):
    is_ajax = request.headers.get('X-Requested-With') == "XMLHttpRequest"

    if is_ajax and request.method == 'POST':
        form_data = json.load(request)
        queue_form = QueueForm(form_data)

        if queue_form.is_valid():
            queue_service = QueueService()
            form_data = queue_form.cleaned_data

            queue = queue_service.create_queue(
                cleaned_form_data=form_data,
                user=request.user
            )

            return JsonResponse({'message': 'Success'})

        else:
            return JsonResponse({
                'status': 'fail',
                'errors': dict(queue_form.errors.items())
            })

    return HttpResponseNotAllowed()
