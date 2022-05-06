"""View module for handling requests about event s"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi1.models import Event


class EventView(ViewSet):
    """Level up event s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event 

        Returns:
            Response -- JSON serialized event 
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event s

        Returns:
            Response -- JSON serialized list of event s
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event s
    """
    class Meta:
        model = Event
        fields =('id','description','date','time','organizer','game')
        depth = 2