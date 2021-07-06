from django.urls import path
from . import views
from .views import ClassCreateView, ClassDetailView, ClassUpdateMember

urlpatterns = [
    path('', views.home, name='classroom-home'),
    path('new-class/', ClassCreateView.as_view(), name='new-class'),
    path('class/<int:pk>',ClassDetailView.as_view(), name="class-detail"),
    path('class/<int:pk>/edit-member',ClassUpdateMember.as_view(), name="class-edit-member")
]