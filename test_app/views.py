
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from test_app.tasks import send_mail_task


@csrf_exempt
def send_mail(request):
    if request.method == 'POST':
        send_mail_task.delay(
            message=request.POST.get('message'),
            subject=request.POST.get('subject'),
            recipients=request.POST.getlist('recipients')
        )
        return HttpResponse('result')
