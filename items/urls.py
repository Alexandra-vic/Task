from rest_framework.routers import DefaultRouter

from django.urls import path, include


from rest_framework.urlpatterns import format_suffix_patterns

from . views import *

urlpatterns = [
    path('items/', ItemsList.as_view()),
    path('items/<int:pk>', ItemsDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)