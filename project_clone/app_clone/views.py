from django.shortcuts import render,loader
from django.http import HttpResponse
from django.contrib.auth.models import User #this one will fetch and insert the data in admin database
from django.db.models import Q # to Use the Q object to combine the queries for username and email.
# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')
def home(request):
    return render(request,'nava_bar.html')
def image_test1(request):
    return render(request,'image_test.html')

def vishnu12(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          email = request.POST.get('email')
          password1 = request.POST.get('password1')
          password2 = request.POST.get('password2')
          if username == '' and email != '' and password1 != ''  and password2 != '' :
                        template = loader.get_template('entry_singup_page.html')
                        context = {
                                    'mymembers1': 'Please Entere The User Name'
                                  }
                        return HttpResponse(template.render(context, request))
          if username != '' and email == '' and password1 != ''  and password2 != '' :
                        template = loader.get_template('entry_singup_page.html')
                        context = {
                                    'mymembers2': 'Please Entere The Emial ID'
                                }
                        return HttpResponse(template.render(context, request))
          if password1 != password2:
                        template = loader.get_template('entry_singup_page.html')
                        context = {
                                    'mymembers4': 'Passowrd its not matchning both'
                                }
                        return HttpResponse(template.render(context, request))
          else:
                  if not User.objects.filter(Q(username=username) | Q(email=email)).exists():
                          User.objects.create_superuser(username=username, email=email, password=password1)
                          template = loader.get_template('entry_singup_page.html')
                          context = {
                                  
                                        'mymembers5': 'Success full created'

                                    }
                          return HttpResponse(template.render(context, request))                  
          
     return render(request,'entry_singup_page.html')


def popup(request):
        return render(request,'button_page.html')
