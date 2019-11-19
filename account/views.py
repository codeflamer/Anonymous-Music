from django.shortcuts import render,redirect
from .forms import RegistrationForm,UpdateForm
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Friends
# Create your views here.


def register(request):
    form=RegistrationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        form.save()
        return redirect('tutorial:login')


    template='account/register.html'
    context={
        'form':form
    }
    return render(request,template,context)


def view_profile(request, num=None):
    if num:
        user = User.objects.get(pk=num)
        userquery = request.user.owner
        friends = userquery.users.all()
        context={'friends':friends,'user':user}
        return render(request, 'account/profile.html', context)
    else:
        user = request.user
        context = {
            'user': user,
        }

        return render(request, 'account/profile.html', context)







def edit_profile(request):
    form = UpdateForm(request.POST or None,instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('tutorial:view_profile')

    context = {
        'form':form,
        'user':request.user
    }
    return render(request,'account/edit_profile.html', context)


def change_password(request):
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('tutorial:view_profile')

    context = {
        'form':form,
        'user':request.user
    }
    return render(request,'account/passwordchange.html', context)