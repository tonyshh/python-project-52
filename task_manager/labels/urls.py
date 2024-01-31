from django.urls import path
from .views import ListLabels, CreateLabel, UpdateLabel, DeleteLabel

urlpatterns = [
    path('', ListLabels.as_view(), name='home_labels'),
    path('create/', CreateLabel.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete_label')
]
