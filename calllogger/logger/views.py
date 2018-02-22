from models import Call
from serializers import CallSerializer
from rest_framework.urls import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CallDetail(APIView):
    """
    Call record
    """
    def get_object(self, pk):
        try:
            return Call.objects.get(pk=pk)
        except Call.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = CallSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = CallSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
