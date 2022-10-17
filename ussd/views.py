import africastalking
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def home(request):
    if request.method =='POST':
        session_id = request.POST.get("sessionId", None)
        servise_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")
        response = ""
        if text == "":
            response = "CON welcom to mobile money \n"
            response += "1. send money \n"
            response += "2. buy airtime \n"
            response += "3. pay bills \n"
            response += "4. bank services \n"
            response += "5. mocash \n"
        elif text == '1':
            response = "CON send money to your friend \n"
            response += "1. Momo user \n"
            response += "2. send to ecash \n"
            response += "3. across the board \n"
            response += "4. cancel \n"
        elif text == '1*1':
            response = "CON welcom to momo user \n"
            response += "list member \n"
            return HttpResponse(response)
        return HttpResponse(response)    


