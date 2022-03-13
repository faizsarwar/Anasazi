from django.urls import path, include
from .views import *

urlpatterns = [
    path('Testemonials/',TestemonialList.as_view()),
    path('Blogs/',BlogList.as_view()),
    path('Faqs/',FaqList.as_view())
]