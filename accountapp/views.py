from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        #model 객체를 DB에 저장하는 방법
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld() #send POST data
        new_hello_world.text = temp #receive POST data
        new_hello_world.save() #save DB


        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'targetUser'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'targetUser'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'