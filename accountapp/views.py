from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        #model 객체를 DB에 저장하는 방법
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld() #send POST data
        new_hello_world.text = temp #receive POST data
        new_hello_world.save() #save DB

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
