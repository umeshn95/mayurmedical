from django.utils.functional import empty
from django.shortcuts import redirect, render
from .models import Product
from django.core.mail import EmailMessage
from twilio.rest import Client
import math
import random
from .form import ProductForm

otp = empty
mobile = empty

def MedicineX(request):
    try:
        if request.method == 'POST':
            mobile1 = request.POST.get("customer_phone")
            form = ProductForm(request.POST, request.FILES)
            mo = mobile1
            global mobile
            mobile = mo
            digits="0123456789"
            OTP=""
            for i in range(6):
                OTP+=digits[math.floor(random.random()*10)]
            c = OTP
            global otp
            otp = c
            msg= f"Hello There this is your OTP {otp}"

            OTP_Request(mobile1, msg)
            if form.is_valid():
                obj = Product()
                obj.customer_name = form.cleaned_data['customer_name']
                obj.product_name = form.cleaned_data['product_name']
                obj.customer_address = form.cleaned_data['customer_address']
                obj.customer_phone = form.cleaned_data["customer_phone"]
                obj.image = form.cleaned_data["image"]
                obj.save()
                return redirect('confirmotp')
            else:
                return render(request, 'api/fail.html') 
        else:
            form = Product()
        return render(request, 'api/profile.html')
    except:
        return render(request, 'api/server.html')


def ConfirmOtp(request):
    if request.method == 'POST':
        inputOtp = request.POST.get("otp")
        print(inputOtp)
        print(otp)
        print(mobile)
        if inputOtp == otp:
            email = EmailMessage(f'Order From {mobile}', f"\nOrder is completed on this order OTP. \n\nOrder OTP   :  {otp}", to=['visheshsolanki12345@gmail.com'])
            email.send()
            return render(request, 'api/index.html')
        else:
            return render(request, 'api/otp_verfy.html')
    return render(request, 'api/otp.html')



def OTP_Request(mobile, msg):
    try:
        account_sid = 'AC7716acf04aa71375e3edf153d709bf06'
        auth_token = 'd923c5f02203b84ebee1f6e74333ae70'
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=msg,
                            from_='+14354944539',
                            to=f"+91{mobile}"
                        )
        print(message.sid)
        return None
    except:
        print("OTP func error.................")



# def ConfirmOtp(request):
#     if request.method == 'POST':
#         mobile = request.POST.get("mobile")
#         # otp_ = request.Post.get("otp")
#         print('................', mobile)
#         # print('................', otp_)
#         digits="0123456789"
#         OTP=""
#         for i in range(6):
#             OTP+=digits[math.floor(random.random()*10)]
#         otp = OTP + " is your OTP"
#         msg= f"Hello There this is your OTP {otp}"
#         OTP_Request(mobile, msg)
#         print(OTP)
#     return render(request, 'api/otp.html')
