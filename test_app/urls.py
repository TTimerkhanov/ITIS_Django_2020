from django.urls import path

from test_app.views import send_mail

urlpatterns = [
    path('notify/', send_mail, name='notify')
]
