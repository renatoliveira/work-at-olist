from rest_framework import serializers
from models import Call, CallStart, CallEnd


class CallSerializer(serializers.Serializer):
    class Meta:
        model = Call
        fields = ('id', 'created_at', 'last_modified_at', 'source', 'destination')


class CallStartSerializer(serializers.Serializer):
    class Meta:
        model = CallStart
        fields = ('id', 'created_at', 'last_modified_at')


class CallEndSerializer(serializers.Serializer):
    class Meta:
        model = CallEnd
        fields = ('id', 'created_at', 'last_modified_at')
