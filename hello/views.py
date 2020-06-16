from rest_framework import viewsets

from hello.models import HelloWorld
from hello.serializers import HelloWorldSerializer


class HelloWorldView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Category
    """
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer
