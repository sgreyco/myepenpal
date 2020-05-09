# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import User, Message


class IndexView(generic.ListView):
    template_name = 'webtext/index.html'

    def get_queryset(self):
        return HttpResponse("Welcome")


def login(request):
    user, created = User.objects.get_or_create(
        username=request.POST['username'])
    user_id = user.id
    return HttpResponseRedirect(reverse('webtext:userHome', args=(user.id,)))


class UserHomeView(generic.DetailView):
    model = User
    template_name = "webtext/userHome.html"


def new_message(request, user_id):
    message = Message()
    message.sender = User.objects.get(id=user_id)
    # message.receiver = User.objects.get_or_create(username=request.POST['receiver'])
    message.message_text = request.POST['message']

    return HttpResponseRedirect(reverse('webtext:success', args=(message.sender.id,)))

class SuccessView(generic.DetailView):
    model = User
    template_name = "webtext/success.html"
