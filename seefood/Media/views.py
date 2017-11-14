from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Post
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Media import forms


def index(request):

    context = {
        'recent' : Post.objects.all(),
        'loginForm'   : AuthenticationForm()
    }
    return render(request, 'Media/gallery.html', context)


def random(request):
    p = Post.objects.order_by('?').first()

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

                #Go back to previous page if not at the login page
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



def gallery(request, pk=None):
    context= {}
    context['loginForm'] = AuthenticationForm()

    allPosts = Post.objects.all()
    length = allPosts.count()
    for i, p in enumerate(allPosts):
        if p.pk == int(pk):
            context['current'] = p
            if i+1 < length:
                context['nextPost'] = allPosts[i+1]

            if i > 0:
                context['prevPost'] = allPosts[i-1]
            break

    if "current" not in context:
        raise Http404

    return render(request, 'Media/post.html', context)

def test(request):
    return render(request, 'Media/test.html')
