from django.shortcuts import render
from core.models import Member
from .forms import *
from SocialConclave.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView

# Create your views here.

class Registration(TemplateView):
    def get(self,request):
        form = DelegateForm()
        return render(request, 'register/register.html', {'form': form})
    def post(self,request):
        print(request.POST)
        form = DelegateForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name') 
            recepient = str(form['email'].value())

            template_delegate = get_template('register/delegate_email.html')
            context_delegate = {'user':'user'}
            content = template_delegate.render(context_delegate)

            # template_treasurer = get_template('')
            # context = Context({'user': user, 'other_info': info})
            mail_content_treasurer = f"""
                <html>
                    <body>
                        <p>{name} has registered.</p>
                    </body>
                </html>
            """
            msg_dele = EmailMessage(f'Thanks for Registering, {name}!',content, EMAIL_HOST_USER, [recepient])
            msg_tr = EmailMessage(f'{name} has registered',mail_content_treasurer,EMAIL_HOST_USER,['poorvachadha.nmims@gmail.com'])
            msg_dele.content_subtype =  'html'
            msg_tr.content_subtype = 'html'
            msg_dele.send()
            msg_tr.send()
            form.save()
            # subject = 'hi deer'
            # message = 'Hope you are enjoying your Django Tutorials'
            # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request,'main/index.html',{'recepient':recepient})
                
def home(request):
    form = DelegateForm()
    return render(request, 'register/register.html', {'form': form})
