from django.urls import path
from . import views

app_name = 'service_requests'  # This is important for namespace

urlpatterns = [
    path('', views.service_request_list, name='list'),
    path('create/', views.service_request_create, name='create'),
    path('<int:pk>/', views.service_request_detail, name='detail'),
    path('<int:pk>/update/', views.service_request_update, name='update'),
    path('<int:pk>/delete/', views.service_request_delete, name='delete'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('<int:pk>/attachment/', views.add_attachment, name='add_attachment'),
]