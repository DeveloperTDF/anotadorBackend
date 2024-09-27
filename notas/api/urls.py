from django.urls import path
from notas.api.views import NotaList, NotaDetail

urlpatterns =   [
    path('', NotaList.as_view(), name='list'),
    path('<int:pk>', NotaDetail.as_view(), name='Detail'),
]

