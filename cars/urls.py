from django.urls import path
from .views import FetchCarsView,FetchCarView,CreateCarView,UpdateCarView,DeleteCarView

urlpatterns=[
    path('fetch-cars/',FetchCarsView.as_view()),
    path('fetch-car/<int:id>/',FetchCarView.as_view()),
    path('create-car/',CreateCarView.as_view()),
    path('update-car/<int:id>/',UpdateCarView.as_view()),
    path('delete-car/<int:id>/',DeleteCarView.as_view()),
]