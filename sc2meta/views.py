# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from google.appengine.api.urlfetch import fetch

from django.contrib.auth.models import User

from django.core.mail import send_mail

import datetime, random, sha

from sc2meta.models import UserProfile
from sc2meta.forms import UserProfileForm


def index(request):

    t = loader.get_template('home.html')
    c = RequestContext(request,{
   
    })
    
    return HttpResponse(t.render(c))
    '''return render_to_response('home.html', {"content": "testing",
                                                      "sc2_stats": stats})'''

def permission_denied(request):
    t = loader.get_template('permission-denied.html')
    c = RequestContext(request,{})
    return HttpResponse(t.render(c))
   
def content(request, page_slug):
    return render_to_response('home.html',{"content": page_slug})

def profile(request, user_id=None):
    
    if user_id:
        profile = UserProfile.objects.get(pk=int(user_id))
    elif request.user.is_authenticated():
        profile = request.user.userprofile
    else:
        return HttpResponseRedirect('/error/')
    
    
    t = loader.get_template('profile/profile.html')
    c = RequestContext(request,{
        "profile": profile 
    })
    
    return HttpResponse(t.render(c))

@login_required
def edit_profile(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            profile = form.save(commit=False)
            request.user.userprofile.updateFromProfile(profile)
            request.user.userprofile.save()
            return HttpResponseRedirect('/profile/') # Redirect after POST
    else:
        form = UserProfileForm(instance=request.user.userprofile) # Load the current user's information

    t = loader.get_template('generic-form.html')
    c = RequestContext(request,{
        'form': form,
        'title': 'Edit Profile'
    })
    
    return HttpResponse(t.render(c))
