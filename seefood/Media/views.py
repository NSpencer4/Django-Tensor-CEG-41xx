from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Upload
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Media import forms, find_food
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse
import logging
import os

# Example output: C:\Users\Chase\Documents\projects\group-4110\seefood\Media
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Example output: C:\Users\Chase\Documents\projects\group-4110\seefood\Media\uploads
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')

def upload(request):
    # If a user is trying to upload
    if request.method == 'POST' and request.FILES['image_src']:
        image_src = request.FILES['image_src']
        fs = FileSystemStorage()
        filename = fs.save(image_src.name, image_src)
        uploaded_file_url = fs.url(filename)
        image_path = os.path.join(UPLOADS_DIR, filename)
        display_path = os.path.join('/uploads/', filename)
        print ("RUNNING TENSORFLOW ON IMAGE:", image_path, ". THIS WILL TAKE A COUPLE OF MINUTES...")

        # Run the image through tensorflow
        tensor_results = find_food.find_food(image_path)

        # Send the Upload obj to the database
        # Package up the necessary fields
        upload_obj = {}
        upload_obj['image_path'] = display_path
        upload_obj['user'] = request.user
        upload_obj['confidence_score'] = tensor_results['scores']
        upload_obj['tensor_verdict'] = tensor_results['result']
        upload_obj['title'] = request.POST.get('image_title')
        upload_obj['accurate'] = 'Default User Accuracy'

        new_upload = Upload.objects.create(image_path=upload_obj['image_path'],
                                     added_on=datetime.utcnow(),
                                     user=upload_obj['user'],
                                     confidence_score=upload_obj['confidence_score'],
                                     tensor_verdict=upload_obj['tensor_verdict'],
                                     title=upload_obj['title'],
                                     accurate=upload_obj['accurate'])

        return render(request, 'Media/upload.html', {
        'uploaded_file_url': uploaded_file_url,
        'tensor_results': tensor_results,
        'new_upload_id': new_upload
        })

    # Regardless of the event render the page if not done
    return render(request, 'Media/upload.html')

def upload_from_cam(request):
    # If a user is trying to upload
    if request.method == 'POST' and request.POST.get('cam_image_src'):
        # Base64
        image_src = request.POST.get('cam_image_src')
        img_title = request.POST.get('img_title')

        # Imports
        import base64
        from django.core.files.base import ContentFile

        # Get extension and set title
        format, imgstr = image_src.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=img_title+'.' + ext)

        fs = FileSystemStorage()
        filename = fs.save(img_title, data)
        uploaded_file_url = fs.url(filename)
        image_path = os.path.join(UPLOADS_DIR, filename)
        display_path = os.path.join('/uploads/', filename)
        print ("RUNNING TENSORFLOW ON IMAGE:", image_path, ". THIS WILL TAKE A COUPLE OF MINUTES...")

        # Run the image through tensorflow
        tensor_results = find_food.find_food(image_path)

        # Send the Upload obj to the database
        # Package up the necessary fields
        upload_obj = {}
        upload_obj['image_path'] = display_path
        upload_obj['user'] = request.user
        upload_obj['confidence_score'] = tensor_results['scores']
        upload_obj['tensor_verdict'] = tensor_results['result']
        upload_obj['title'] = img_title
        upload_obj['accurate'] = 'Default User Accuracy'

        new_upload = Upload.objects.create(image_path=upload_obj['image_path'],
                                     added_on=datetime.utcnow(),
                                     user=upload_obj['user'],
                                     confidence_score=upload_obj['confidence_score'],
                                     tensor_verdict=upload_obj['tensor_verdict'],
                                     title=upload_obj['title'],
                                     accurate=upload_obj['accurate'])

        return render(request, 'Media/upload.html', {
        'uploaded_file_url': uploaded_file_url,
        'tensor_results': tensor_results,
        'new_upload_id': new_upload
        })

    # Regardless of the event render the page if not done
    return render(request, 'Media/upload.html')

def gallery(request):
    context = {}
    context['uploads'] = []

    if request.user.is_authenticated:
        for e in Upload.objects.filter():
            context['uploads'].append(e)

    return render(request, 'Media/gallery.html', context)

def set_accuracy(request):
    if request.method == 'POST':
        id = request.POST.get('pk')
        accurate = request.POST.get('accurate')
        # Update the upload obj to see if tensorflow was accurate or not
        get_object_or_404(Upload, pk=id)

        try:
            selected_img = Upload.objects.get(pk=id)
        except (KeyError, Upload.DoesNotExist):
            return render(request, 'Media/gallery.html')
        else:
            selected_img.accurate = accurate
            selected_img.save()

        # logger = logging.getLogger(__name__)
        # logger.debug(request)
    context = {}
    context['uploads'] = []

    for e in Upload.objects.all():
        context['uploads'].append(e)

    return render(request, 'Media/gallery.html', context)

def index(request):

    context = {
        'recent': Upload.objects.all(),
        'loginForm': AuthenticationForm()
    }
    return render(request, 'Media/homepage.html', context)

def createUser(request):
    form = forms.RegistrationForm()

    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            newuser = form.save()
            messages.add_message(request, messages.SUCCESS, 'User created!')
            return redirect(reverse('Media:loginUser'))

    return render(request, 'registration/createUser.html', {'form': form})

def loginUser(request):
    if request.user.is_authenticated():
        return redirect('/')

    context = {}
    context['loginForm'] = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, 'Logged in!')

                # Go back to previous page if not at the login page
                if request.POST.get('next') == request.get_full_path():
                    return redirect('/')
                else:
                    return redirect(request.POST.get('next'))
            else:
                # user not active
                context['error'] = 'Your account is inactive'
        else:
            # bad login
            context['error'] = 'Your username or password are incorrect'

    return render(request,'registration/loginPage.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'Media/homepage.html')

def test(request):
    print (request)
    # If a user is trying to upload
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        image_path = os.path.join(UPLOADS_DIR, filename)
        print ("RUNNING TENSORFLOW ON IMAGE:", image_path, ". THIS WILL TAKE A COUPLE OF MINUTES...")

        # Run the image through tensorflow
        tensor_results = find_food.find_food(image_path)

        # Send the Upload obj to the database
        # Package up the necessary fields
        upload_obj = {}
        upload_obj['image_path'] = image_path
        upload_obj['user'] = request.user
        upload_obj['confidence_score'] = tensor_results['scores']
        upload_obj['tensor_verdict'] = tensor_results['result']
        upload_obj['title'] = 'Default Title'
        upload_obj['accurate'] = 'Default User Accuracy'

        new_upload = Upload.objects.create(image_path=upload_obj['image_path'],
                                     added_on=datetime.utcnow(),
                                     user=upload_obj['user'],
                                     confidence_score=upload_obj['confidence_score'],
                                     tensor_verdict=upload_obj['tensor_verdict'],
                                     title=upload_obj['title'],
                                     accurate=upload_obj['accurate'])

        return render(request, 'Media/results.html', {
        'uploaded_file_url': uploaded_file_url,
        'tensor_results': tensor_results,
        'new_upload_id': new_upload
        })
    # Regardless of the event render the page if not done
    return render(request, 'Media/test.html')

def help(request):
    return render(request, 'Media/help.html')