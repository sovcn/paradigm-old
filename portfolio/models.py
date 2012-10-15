from django.db import models
from django.template import Context, loader

import blog
import re
from datetime import datetime
# Create your models here.

def initializeAllProjects(request):
        # Remove all existing
        projects = Project.objects.all()
        for proj in projects:
            proj.delete()
        
        
        '''proj = Project()
        proj.title = "Platform Independent Cloud Scripting"
        proj.slug = "pics"
        proj.alt = proj.title
        proj.date = "Fall 2010 - Present"
        proj.tools = "Python, JavaScript, Django, Node.js, Mozilla Rhino, Android, jQuery"
        proj.image_count = 3
        proj.programming = True
        proj.research = True
        proj.save()
        
        proj = Project()
        proj.title = "Innovation by Design"
        proj.slug = "ibd"
        proj.alt = proj.title
        proj.date = "June 2009 and November 2011"
        proj.tools = "Photoshop, PHP, Python, Zend Framework, Django-nonrel, Appengine, JQuery"
        proj.programming = True
        proj.design = True
        proj.save()
        
        proj = Project()
        proj.title = "SRU Competitive Gaming"
        proj.slug = "srugaming"
        proj.alt = proj.title
        proj.date = "Fall 2011"
        proj.tools = "Python, Django-nonrel, Google Appengine, Photoshop"
        proj.image_count = 1
        proj.programming = True
        proj.design = True
        proj.save()
        
        proj = Project()
        proj.title = "Starcraft Metagame Central"
        proj.slug = "sc2meta"
        proj.alt = proj.title
        proj.date = "Summer 2011"
        proj.tools = "Python, Django-nonrel, Google Appengine, Photoshop"
        proj.image_count = 3
        proj.programming = True
        proj.design = True
        proj.save()
        
        proj = Project()
        proj.title = "Arbirary Precision: Mandelbrot"
        proj.slug = "mandelbrot"
        proj.alt = proj.title
        proj.date = "Fall 2010"
        proj.tools = "C++, CUDA, OpenMP, OpenGL"
        proj.image_count = 1
        proj.programming = True
        proj.research = True
        proj.save()
        
        proj = Project()
        proj.title = "Dojo Sensor"
        proj.slug = "sensor"
        proj.alt = proj.title
        proj.date = "Summer 2010"
        proj.tools = "JavaScript, reStructuredText, PhoneGap, Android, WebOS, JIL, BONDI"
        proj.image_count = 2
        proj.programming = True
        proj.save()
        
        proj = Project()
        proj.title = "Sudoku Heuristics and Classification"
        proj.slug = "sudoku"
        proj.alt = proj.title
        proj.date = "September 2009"
        proj.tools = "Xcode, Objective-C, PHP, XML-RPC, Photoshop"
        proj.image_count = 3
        proj.programming = True
        proj.research = True
        proj.save()
        
        proj = Project()
        proj.title = "Pokemon Java Clone"
        proj.slug = "pokemon"
        proj.alt = proj.title
        proj.date = "June 2009"
        proj.tools = "Java, Photoshop, MySQL"
        proj.image_count = 2
        proj.programming = True
        proj.save()
        
        proj = Project()
        proj.title = "ClaniT Application Framework"
        proj.slug = "clanit"
        proj.alt = proj.title
        proj.date = "June 2008"
        proj.tools = "Photoshop, PHP, MySQL, Zend Framework, HTML, CSS"
        proj.programming = True
        proj.design = True
        proj.save()
        
        proj = Project()
        proj.title = "Sovereign Clan Manager"
        proj.slug = "scm"
        proj.alt = proj.title
        proj.date = "April 2007"
        proj.tools = "Photoshop, PHP, MySQL, JavaScript"
        proj.image_count = 2
        proj.programming = True
        proj.design = True
        proj.save()'''
        
        proj = Project()
        post = blog.models.Post()
        
        post.title = "Innovation by Design"
        post.content = "Content"
        post.content_parsed = post.content
        post.description = post.content
        
        post.banner_image = ""
        post.author = request.user.userprofile
        
        post.featured = False
        post.is_project = True
        
        post.save()
        proj.post = post
        
        proj.slug = "innobdesign"
        proj.alt = proj.post.title
        proj.date = datetime(year=2011, month=11, day=1)
        proj.years = "2009-2011"
        proj.images = ""
        proj.main_html = "innobdesign.html"
        proj.aside_html = "innobdesign_aside.html"
        
        proj.design = True
        proj.programming = True
        proj.save()

class Project(models.Model):
    
    post = models.OneToOneField(blog.models.Post, null=True)
    
    #title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    alt = models.CharField(max_length=255)
    
    date = models.DateTimeField()
    years = models.CharField(max_length=20)
    
    #image_count = models.IntegerField(default=3)
    images = models.TextField()
    
    main_html = models.TextField()
    aside_html = models.TextField()
    
    design = models.BooleanField(default=False)
    programming = models.BooleanField(default=False)
    research = models.BooleanField(default=False)
    
    large_content = ""
    
    def description(self):
        ''''t = loader.get_template('portfolio/templates/projects/' + self.slug + '.html')
        c = Context({
        })
        self.large_content = t.render(c)
        p = re.compile(r'<.*?>')
        description = p.sub('', self.large_content)
        if len(description) > 300:
            description = description[0:296] + " ..."
        
        return description'''
        
        return self.post.description
    
    def title(self):
        return self.post.title
    
    def getLink(self):
        return "/project/" + self.slug + "/"
    
    def displayDate(self):
        return self.date.strftime("%B %Y")
    
    def renderImages(self):
        out = ""
        for i in range(1,self.image_count+1):
            out += """
                <a class="fancy" rel="group" title="%s" href="/static/images/projects/%s/%d.jpg">
                    <img width="100px" height="100px" src="/static/images/projects/%s/%d_thumb.jpg" />
                </a>
            """ %(self.title, self.slug, i, self.slug, i)
        
        return out
    
    def smallView(self):
        t = loader.get_template('portfolio/templates/project_small.html')
        c = Context({
            "project": self
        })
        return t.render(c)
    
    def __unicode__(self):
        return self.title()
    
    def displayGallery(self):
        t = loader.get_template('portfolio/templates/project_gallery.html')
        c = Context({
            "project": self
        })
        return t.render(c)
    
    def delete(self, *args, **kwargs):
        try:
            self.post.delete()
        except (blog.models.Post.DoesNotExist):
            pass
        super(Project, self).delete(*args, **kwargs)
    
    
    def getAside(self):
        t = loader.get_template('portfolio/templates/projects/' + self.aside_html)
        c = Context({
            "project": self
        })
        return t.render(c)

    
        
        