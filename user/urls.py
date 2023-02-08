from django.urls import path, include
from . views import *


path('registr/', RegistrUserView.as_view(), name='registr')