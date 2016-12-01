from django.conf.urls import url
from django.views.generic import TemplateView

from .views import CookieView


urlpatterns = [

    url(r'^home/', CookieView.as_view(), name="cookie_view"),
]