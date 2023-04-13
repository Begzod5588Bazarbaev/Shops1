from django.urls import path
from .views import *

urlpatterns = [
    path('', newsline, name='newsline'),
    path('seatch/', Search, name='search'),
    path('rubric/<int:rubric_id>/', rubric_list),
    path('news/<int:pk>/',details.as_view()),
    path('news/<int:pk>/edit/', edit),
    path('news/<int:pk>/delete/', deletes),
    path('news/create/',create)
]
