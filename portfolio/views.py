# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from portfolio.models import Project, initializeAllProjects
from blog.models import ImageModel, Post


def index(request):
    
    proj1 = None
    proj2 = None
    
    try:
        proj1 = Project.objects.get(slug="pics")
        proj2 = Project.objects.get(slug="ibd")
    except:
        initializeAllProjects()
        proj1 = Project.objects.get(slug="pics")
        proj2 = Project.objects.get(slug="ibd")
        
    
    featured_images = ImageModel.objects.all().order_by("-added")
    featured_images = featured_images.filter(featured=True)
    featured_images = featured_images[0:3]

    for image in featured_images:
        image.home_url = image.url(886) # Grab the resized image url at 886px
    
    posts = Post.objects.all().order_by("-added")[0:4]
    
    
    t = loader.get_template('portfolio/templates/home.html')
    c = RequestContext(request,{
        "proj1": proj1,
        "proj2": proj2,
        "featured_images": featured_images,
        "posts": posts,
        "page_id": "home"
    })
    
    return HttpResponse(t.render(c))

def about(request):
    
    t = loader.get_template('about.html')
    c = RequestContext(request,{
        "age": 21,
        "page_id": "about"
    })
    return HttpResponse(t.render(c))

def init(request):
    initializeAllProjects()
    return index(request)

@login_required
def admin(request):
    t = loader.get_template('portfolio/templates/admin.html')
    c = RequestContext(request,{
        
    })

    return HttpResponse(t.render(c))
def project_view(request, slug):
    project = Project.objects.get(slug=slug)
    t = loader.get_template('portfolio/templates/project_view.html')
    c = RequestContext(request,{
        "project": project,
        "page_id": "portfolio"
    })
    
    return HttpResponse(t.render(c))
    
def projects(request, projects=None):
    
    if not projects:
        projects = Project.objects.all()
    
    t = loader.get_template('portfolio/templates/projects.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_title": "PORTFOLIO",
        "page_description": """
                Below are all of the major projects that I have worked on since high school (circa 2007).  Click on the title or image for more details on each.
        """,
        "page_id": "portfolio"
    })
    
    return HttpResponse(t.render(c))

def projects_programming(request):
    projects = Project.objects.filter(programming=True)
    
    t = loader.get_template('portfolio/templates/projects_programming.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_title": "PROGRAMMING",
        "page_description": "\"Measuring programming progress by lines of code is like measuring aircraft building progress by weight.\" - Bill Gates",
        "page_id": "portfolio"
    })
    
    return HttpResponse(t.render(c))
    
def projects_web_design(request):
    projects = Project.objects.filter(design=True)
    t = loader.get_template('portfolio/templates/projects_web_design.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_title": "WEB DESIGN",
        "page_description": "\"Good design is obvious. Great design is transparent.\" - Joe Sparano",
        "page_id": "portfolio"
    })
    
    return HttpResponse(t.render(c))

def projects_research(request):
    projects = Project.objects.filter(research=True)
    t = loader.get_template('portfolio/templates/projects_research.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_title": "RESEARCH",
        "page_description": "\"The hardest thing is to go to sleep at night, when there are so many urgent things needing to be done. A huge gap exists between what we know is possible with today's machines and what we have so far been able to finish.\" - Donald Knuth",
        "page_id": "portfolio"
    })
    
    return HttpResponse(t.render(c))