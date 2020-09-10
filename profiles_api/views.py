from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView feaatures"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, delete, put)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
