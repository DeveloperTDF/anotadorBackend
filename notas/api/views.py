from rest_framework import generics
from notas.api.serializers import NotaSerializer
from notas.models import Nota

class NotaList(generics.ListCreateAPIView):
    queryset            =   Nota.objects.all()
    serializer_class    =   NotaSerializer

class NotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            =   Nota.objects.all()
    serializer_class    =   NotaSerializer