from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put ...)',
            'Similar to a traditional Django view',
            'Gives you the most control over your app\'s logic',
            'Is mapped manually to URLs',
        ]
        return Response({
            'message': 'Hello',
            'an_apiview': an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, id=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, id=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, id=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})
