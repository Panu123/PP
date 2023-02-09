

import profile
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import Http404, HttpResponse
from .models import *
from .forms import *
import os
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from django.contrib import messages



def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            
            # New directory name
            field_name = 'username'
            obj = User.objects.order_by('-pk')[0]
            field_object = User._meta.get_field(field_name)
            field_value = field_object.value_from_object(obj)
  
            # Parent Directory path
            parent_dir = "/home/neros/neros/media"
            
            # Path
            path = os.path.join(parent_dir, field_value)
            
            # Create the directory
            try:
                os.makedirs(path, exist_ok = True)
                print("Directory '%s' created successfully" % field_value)
            except OSError as error:
                print("Directory '%s' can not be created" % field_value)

            
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

# Profiilitiedot
@login_required(login_url='register/')
def edit_details(request):
    return render(request, 'users/edit_detail.html')

# Asetukset
@login_required(login_url='register/')
def settings(request):
    return render(request, 'users/settings.html')

# Imagehomma
@login_required(login_url='register/')

def picture_image_view(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
  
        if form.is_valid():
            
            form.save()
            return redirect('success')
    

    else:
        form = PictureForm()
    return render(request, 'users/picture_image_form.html', {'form' : form})

def success(request):
    print('successfully uploaded')
    # HttpResponse('successfully uploaded')
    return redirect( 'picture_images')
    
@login_required(login_url='register/')

def display_picture_images(request):
    
    if request.method == 'GET':
  
        # getting all the objects of picture.
        pictures = Picture.objects.all()
        
        return render(request, 'templates/users/display_picture_images.html', {'picture_images' : pictures})


@login_required(login_url='register/')
def edit(request):
    return render(request, 'users/edit.html')


#kuvan poisto

@login_required(login_url='register/')
def deleteProduct( request, pk):
    if request.method == "POST":
        picture = Picture.objects.get(pk=pk)
        picture.delete("")
    return redirect( 'picture_images')

#Edit kuvaa
@login_required
def editProduct(request, pk):
    prod = Picture.objects.get(pk=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.picture_Main_Img) > 0:
                os.remove(prod.picture_Main_Img.path)
            prod.picture_Main_Img = request.FILES['picture_Main_Img']
        prod.name = request.POST.get('name')
        prod.tags = request.POST.get('tags')
        prod.is_visible = request.POST.get('is_visible')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'edit.html', context)
    
        
    
#salasanan vaihto KÄYTTÄJÄN
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
import time
@login_required(login_url='register/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            time.sleep(5)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })








