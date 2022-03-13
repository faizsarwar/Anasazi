from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Testemonial

# Create your views here.
class TestemonialList(APIView):
    def get(self,request,format=None):
        products=Testemonial.objects.all()
        serializer=TestemonialSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class FaqList(APIView):
    def get(self,request,format=None):
        products=Faq.objects.all()
        serializer=FaqSerializer(products,many=True)
        return Response(serializer.data)

# Create your views here.
class BlogList(APIView):
    def get(self,request,format=None):
        products=Blog.objects.all()
        serializer=BlogSerializer(products,many=True)
        return Response(serializer.data)
