from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import path
from app.setting.views import CalculatorView

class HelloView(APIView):
    def get(self, request):
        return Response({
            "status" : "success",
            "message" : "Hello world"  
        })
    

urlpatterns = [
    path("calc/", CalculatorView.as_view())
]