from django.shortcuts import render,redirect

import uuid , requests 
import string    
import random, json 
from django.contrib import messages


# Create your views here.
def index(request):
    
    S = 6  
    ran = ''.join(random.choices(string.ascii_letters +string.digits, k = S)) 

    global captcha_text
    
    captcha_text = ran
    
    

    return render(request, 'index.html',{'ran':ran})

def show(request):
    if request.method == 'POST':
        VID = request.POST.get('Vid')
        uservalue = request.POST.get('uservalue')

        if(len(VID)==12):
            if(captcha_text==uservalue):
                global v
                v=str(VID)
                global x
                id = uuid.uuid4()
                x= str(id)
                url= 'https://stage1.uidai.gov.in/onlineekyc/getOtp/'


                headers = {'content-type' : 'application/json'}

                data = {"uid": 	v,
                        "txnId": x,
                        }

                response = requests.post(url, json=data, headers=headers)

                json_loads=json.loads(response.text)

                if (json_loads['status']=='y' or json_loads['status']== 'Y'):
                    print("success")
                else:
                    print("error in otp")
                    return render(request,'index.html')

                return render(request, 'show.html')
            else:
                messages.error(request,'Invalid Captcha')
                return redirect('show')
        else:
            messages.error(request,'Invalid Vid')
            return redirect('show')
    return index(request)

def home(request):

    if request.method == 'POST':
        otp = request.POST.get('otp')
        headers = {'content-type' : 'application/json'}
        url1= 'https://stage1.uidai.gov.in/onlineekyc/getAuth/'
        print(otp)
        data2 = {"uid": v,
                "txnId": x,
                "otp": otp,
                }

        response2 = requests.post(url1, json=data2, headers=headers)


        a=json.loads(response2.text)
        


        if(a['status']=='y' or a['status']=='Y' ):

            print("success")
            return render(request, 'home.html')
        else:
            messages.error(request,'Invalid otp')
            print("error in otp")
            return index(request)

    return render(request, 'show.html')


def requestaddress(request):
    return render(request, 'requestaddress.html')


def changeaddress(request):
    return render(request, 'changeaddress.html')

def home1(request):
    return render(request, 'home.html')

    