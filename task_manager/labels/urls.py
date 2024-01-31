from task_manager.labels import views
from django.urls import path

urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels'),
    path('create/', views.LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(),
         name='label_update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(),
         name='label_delete'),
]
