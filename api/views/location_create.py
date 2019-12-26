from rest_framework.generics import CreateAPIView
from rest_framework import serializers
from api.models import Location

class LocationCreateSerailizer(serializers.Serializer):
	class Meta:
		model = Location
		field = "__all__"




class LocationCrateView(CreateAPIView):
	serializer_classes = LocationCreateSerailizer
	authentication_classes = ()