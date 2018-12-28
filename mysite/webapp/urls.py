from django.conf.urls import url
from mysite.webapp import views



urlpattern = [url(r"^$", views.index, name="index"
                  )]

