from django.urls import path
from django.views.generic import TemplateView
from appmain import views

urlpatterns = [
   path(
		'', 
		TemplateView.as_view(template_name="home.html")),
   path(
   	'about-us/', 
   	TemplateView.as_view(template_name="about_us.html")),
   path(
   	'contact-us/', 
   	views.ContactUsView.as_view(), name="contact_us",),
]
