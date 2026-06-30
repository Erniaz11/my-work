from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class HelloView(APIView):
    def get(self, request):
        return Response({
            "status": "success",
            "message": "Hello world"  
        })

class CalculatorView(APIView):
    def post(self, request):
        data = request.data
        try:
            num1 = float(data.get('num1'))
            num2 = float(data.get('num2'))
            operation = data.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    return Response({"error": "Division by zero is not allowed."}, status=400)
            else:
                return Response({"error": "Invalid operation."}, status=400)

            return Response({"result": result})

        except (ValueError, TypeError):
            return Response({"error": "Invalid input. Please provide valid numbers."}, status=400)
     



class TemperatureView(APIView):
    def get(self, request):
        temp_param = request.query_params.get('temp')
        
        if temp_param is None:
            return Response(
                {"message": "Передайте температуру в строке поиска, например: ?temp=25"}, 
                status=status.HTTP_200_OK
            )
            
        try:
            temp = float(temp_param)
            
            if temp < -10:
                result_status = "очень холодно"
            elif -10 <= temp < 0:
                result_status = "холодно"
            elif 0 <= temp < 10:
                result_status = "нормально"
            elif 10 <= temp <= 60:
                result_status = "жарко"
            else:
                result_status = "очень жарко"
                
            return Response({"temperature": temp, "status": result_status}, status=status.HTTP_200_OK)
            
        except ValueError:
            return Response({"error": "Вводите только числа!"}, status=status.HTTP_400_BAD_REQUEST)