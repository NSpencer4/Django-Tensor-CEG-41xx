from django.shortcuts import render, redirect
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
import os

# Example output: C:\Users\Chase\Documents\projects\group-4110\seefood\Media
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Example output: C:\Users\Chase\Documents\projects\group-4110\seefood\Media\uploads
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        image_path = os.path.join(UPLOADS_DIR, filename)
        print ("RUNNING TENSORFLOW ON IMAGE:", image_path, ". THIS WILL TAKE A COUPLE OF MINUTES...")
        tensor_results = find_food.find_food(image_path)
        return render(request, 'Media/upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'tensor_results': tensor_results
        })
    return render(request, 'Media/upload.html')

def gallery(request):
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Upload.objects.filter(pub_date__lte=timezone.now())

def index(request):

    context = {
        'recent': Upload.objects.all(),
        'loginForm': AuthenticationForm()
    }
    return render(request, 'Media/homepage.html', context)


def random(request):
    p = Upload.objects.order_by('?').first()

    return redirect(p)

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
    return render(request, 'Media/test.html')

def help(request):
    return render(request, 'Media/help.html')

def upload(request):
    return render(request, 'Media/upload.html')