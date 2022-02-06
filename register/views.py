from django.shortcuts import render
from core.models import Member
from django.http import HttpResponseRedirect
from .forms import *
from SocialConclave.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

import json
import requests
# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/
from Paytm import Checksum

# Create your views here.

Paytm_id = 'UtSWuc20243991814656'
Paytm_Key = '65vTE5Ov888@WIRv'

def success(request):
    return render(request, 'register/success.html')

def Renderform(request):
    args = {}

    if request.method == 'POST':
        print(request.POST)
        form = DelegateForm(request.POST)
        if form.is_valid():
            request.POST._mutable = True
            i = Delegate.objects.all().order_by('-counter')[0]
            request.POST['counter'] = i.counter+1
            request.POST['counter'] = "{:03d}".format(request.POST['counter'])
            order_id = "OD" + request.POST['counter']
            form.save()


            paytmParams = dict()

            paytmParams = {
                "requestType"   : "Payment",
                "mid"           : Paytm_id,
                "websiteName"   : "WEBSTAGING",
                "orderId"       : order_id,
                "callbackUrl"   : "http://127.0.0.1:8000/register/handlerequest/",
                "txnAmount"     : {
                    "value"     : "1.00",
                    "currency"  : "INR",
                },
                "userInfo"      : {
                    "custId"    : request.POST['counter'],
                },
            }

            # # Generate checksum by parameters we have in body
            # # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
            # checksum = paytmchecksum.generateSignature(json.dumps(paytmParams["body"]), Paytm_Key)

            # paytmParams["head"] = {
            #     "signature"    : checksum
            # }

            # post_data = json.dumps(paytmParams)

            # # for Staging
            # url = f'https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=cQYdlG10371492229645&orderId={order_id}'

            # for Production
            # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
            # response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
            # print(response)

            # payment_page = {
            #     'mid' : Paytm_id,
            #     'orderId' : order_id,
            # }
            paytmParams['CHECKSUMHASH'] = Checksum.generate_checksum(paytmParams, Paytm_Key)
            return render(request, 'register/PaymentRedirect.html', {'data': paytmParams})


            # return HttpResponseRedirect('../main/index.html')
    else:
        form = DelegateForm()
    args['form'] = form

    return render(request,'register/register.html', args)



@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, Paytm_Key, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'register/success.html', {'response': response_dict})





















# # class Renderform(TemplateView):
#     def get(self,request):
#         form = DelegateForm()
#         return render(request, 'register/register.html', {'form': form})
#     def post(self,request):
#         print(request.POST)
#         form = DelegateForm(request.POST)
#         if form.is_valid():
#             name = request.POST.get('name') 
#             recepient = str(form['email'].value())

#             template_delegate = get_template('register/delegate_email.html')
#             context_delegate = {'user':'user'}
#             content = template_delegate.render(context_delegate)

#             # template_treasurer = get_template('')
#             # context = Context({'user': user, 'other_info': info})
#             mail_content_treasurer = f"""
#                 <html>
#                     <body>
#                         <p>{name} has registered.</p>
#                     </body>
#                 </html>
#             """
#             # msg_dele = EmailMessage(f'Thanks for Registering, {name}!',content, EMAIL_HOST_USER, [recepient])
#             # msg_tr = EmailMessage(f'{name} has registered',mail_content_treasurer,EMAIL_HOST_USER,['email2vrushit@gmail.com'])
#             # msg_dele.content_subtype =  'html'
#             # msg_tr.content_subtype = 'html'
#             # msg_dele.send()
#             # msg_tr.send()
#             form.save()
#             print("==========IN===========")
#             # subject = 'hi deer'
#             # message = 'Hope you are enjoying your Django Tutorials'
#             # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
#             return render(request,'main/index.html',{'recepient':recepient})
                
# # def home(request):
# #     form = DelegateForm()
# #     print("*************==IN=************==")
# #     return render(request, 'register/register.html', {'form': form})
