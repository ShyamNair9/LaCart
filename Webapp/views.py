from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fridge
from.serializers import FridgeSerializer

def index(request):
	return HttpResponse("<h1> Webapp Homepage</h1>")
#ItemList
class ItemList(APIView):

	def get(self, request):
		items = Fridge.objects.all()
		serializer = FridgeSerializer(items, many=True)
		return Response(serializer.data)

	def post(self):
		pass

