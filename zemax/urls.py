from django.urls import path
from . import views
from .views import HouseListView, HouseDetailView, HouseCreateView, HouseUpdateView, HouseDeleteView


urlpatterns = [
    path('', HouseListView.as_view(), name='home'),
    path('<int:pk>/', HouseDetailView.as_view(), name='detail'),
    path('new/', HouseCreateView.as_view(), name='new listing'),
    path('register/', views.register, name='register'),
    path('<int:pk>/update', HouseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', HouseDeleteView.as_view(), name='delete'),
    path('profile/', views.profile, name='profile'),
    path('article/', views.article, name='article'),
    path('email/', views.send_mail, name='email')
]


