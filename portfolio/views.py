# Create your views here.
from django.core.cache import cache

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from portfolio.models import Project, initializeAllProjects
from blog.models import ImageModel, Post

@cache_page(60*60*24)
def index(request):
        #proj1 = Project.objects.get(slug="pics")
        #proj2 = Project.objects.get(slug="ibd")
    
    '''
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
        "posts": posts,
        "page_id": "home"
    })
    
    return HttpResponse(t.render(c))
    
    '''
    
    projects = []
    projects.append(Project.objects.filter(slug="paradigm")[0])
    projects.append(Project.objects.filter(slug="pics")[0])
    projects.append(Project.objects.filter(slug="sensor")[0])
    projects.append(Project.objects.filter(slug="sudoku")[0])
    
    featured = Post.objects.filter(featured=True)[0]
    
    t = loader.get_template('portfolio/templates/home.html')
    c = RequestContext(request,{
        "projects": projects,
        "page_id": "home",
        "featured": featured
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
def reset(request):
    projects = Project.objects.all()
    for project in projects:
        project.delete()
    initializeAllProjects(request)
    
    cache.clear()
    
    return HttpResponseRedirect('/') # Redirect after Reset

@login_required
def admin(request):
    t = loader.get_template('portfolio/templates/admin.html')
    c = RequestContext(request,{
        
    })

    return HttpResponse(t.render(c))
def project_view(request, slug):
    project = Project.objects.get(slug=slug)
    images = project.images.split(",")
            
    t = loader.get_template('portfolio/templates/projects/' + project.main_html)
    c = RequestContext(request,{
        "post": project.post,
        "project": project,
        "images": images,
        "page_id": "portfolio",
        "is_project": True,
        "tags": project.post.get_tags()
    })
    
    return HttpResponse(t.render(c))

@cache_page(60*60*24)
def projects(request, projects=None):
    
    if not projects:
        projects = Project.objects.all().order_by("-date")
    
    t = loader.get_template('portfolio/templates/projects.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_id": "portfolio",
        "filter_selected": "all",
        "is_ajax": request.is_ajax()
    })
    
    return HttpResponse(t.render(c))

@cache_page(60*60*24)
def projects_programming(request):
    projects = Project.objects.filter(programming=True).order_by("-date")
    
    t = loader.get_template('portfolio/templates/projects_programming.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_id": "portfolio",
        "filter_selected": "programming",
        "is_ajax": request.is_ajax()
    })
    
    return HttpResponse(t.render(c))

@cache_page(60*60*24) 
def projects_web_design(request):
    projects = Project.objects.filter(design=True).order_by("-date") 
    t = loader.get_template('portfolio/templates/projects_web_design.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_id": "portfolio",
        "filter_selected": "design",
        "is_ajax": request.is_ajax()
    })
    
    return HttpResponse(t.render(c))

@cache_page(60*60*24)
def projects_research(request):
    projects = Project.objects.filter(research=True).order_by("-date") 
    t = loader.get_template('portfolio/templates/projects_research.html')
    
    c = RequestContext(request,{
        "projects": projects,
        "page_id": "portfolio",
        "filter_selected": "research",
        "is_ajax": request.is_ajax()
    })
    
    return HttpResponse(t.render(c))

    