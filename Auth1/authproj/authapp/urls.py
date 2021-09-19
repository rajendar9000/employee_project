from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile),
    path('age', views.age),
    path('logout',views.logout_view)
]