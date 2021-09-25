from typing import ContextManager
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'login&reg.html')

def new_user(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        request.session['logged_user_id'] = new_user.id
        return redirect('/wishes')    
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['logged_user_id'] = logged_user.id
        return redirect('/wishes')
    else:
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def all_wishes(request):
    context = {
        'user': User.objects.get(id=request.session['logged_user_id']),
        'user_wishes' : Wish.objects.filter(uploaded_by=request.session['logged_user_id']),
        'granted_wishes' : Wish.objects.filter(uploaded_by=request.session['logged_user_id'], granted = True)
        }
    return render(request, 'main.html', context)

def new_wish(request):
    context = {
        'user' : User.objects.get(id=request.session['logged_user_id'])
    }
    return render(request, 'new_wish.html', context)

def create_wish(request):
    user = User.objects.get(id=request.session['logged_user_id'])
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/wishes/new')
    else: 
        new_wish = Wish.objects.create(item = request.POST['item'], description = request.POST['description'], uploaded_by = user)
        return redirect('/wishes')    

def edit_wish(request, wish_id):
    context ={
        'user' : User.objects.get(id=request.session['logged_user_id']),
        'wish' : Wish.objects.get(id=wish_id)
    }
    return render(request, 'edit_wish.html', context)

def update_wish(request, wish_id):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/wishes/new')
    else: 
        update_wish = Wish.objects.get(id=wish_id)
        update_wish.item = request.POST['item']
        update_wish.description = request.POST['description']
        update_wish.save()
        return redirect('/wishes') 

def delete_wish(request, wish_id):
    delete_wish = Wish.objects.get(id=wish_id)
    delete_wish.delete()
    return redirect('/wishes')

def grant_wish(request, wish_id):
    granted_wish = Wish.objects.get(id=wish_id)
    granted_wish.granted = True
    granted_wish.save()
    return redirect('/wishes')
