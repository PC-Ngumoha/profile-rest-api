from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

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
