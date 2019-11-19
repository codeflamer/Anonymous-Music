from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm
from .models import Post,Friends
from django.contrib.auth.models import User
from .forms import MessageForm,TweetForm
from home.models import Message,Tweet

# def home(request):
#
#     return render(request,'home/home.html')

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        friends = User.objects.exclude(id=request.user.id)
        list=Friends.objects.get(current_user=request.user)
        lists = list.users.all()

        argss = {'form': form, 'posts': posts,'friends':friends, 'lists': lists}
        return render(request, self.template_name, argss)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save(commit=True)
            text = form.cleaned_data['post']
            HomeForm()
            return redirect('home:home')

        args = {'form': form,'text':text}
        return render(request, self.template_name, args)


def change_friends(request,alpha,num):
    new_friend = User.objects.get(pk=num)
    if alpha == 'add':
        Friends.make_friend(request.user,new_friend)
    elif alpha == 'remove':
        Friends.lose_friend(request.user,new_friend)
    return redirect('home:home')

def chat(request,num):
    receiver = User.objects.get(pk=num)
    if request.method == 'GET':
        form = MessageForm()
        chatfriend = User.objects.get(pk=num)
        messages = request.user.message_set.filter(receiver__username__icontains=chatfriend)
        chatfriend = chatfriend.message_set.filter(receiver__username__icontains=request.user)
        context = {'messages': messages, 'friendmessages': chatfriend,'receiver':receiver,'form':form}
        return render(request,'home/chat.html', context)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender= request.user
            obj.receiver = receiver
            obj.save()
            return redirect('/home/message/{}/'.format(num))

def tweets(request):
    if request.method=='GET':
        form=TweetForm()
        ttws = Tweet.objects.filter(User__username__icontains=request.user).order_by('-date')
        context = {'tweets':ttws,'form':form}
        return render(request, 'home/tweet.html', context)
    if request.method =='POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User=request.user
            obj.save()
            return redirect('home:tweets')

def publictweets(request):
    friends=Friends.objects.get(current_user__id=request.user.id)
    print(friends)

    for friend in friends.users.all():
        for tweet in friend.tweet_set.all():
            print(tweet.text)
    context = {'friends':friends}
    return render(request, 'home/timeline.html', context)
