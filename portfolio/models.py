from django.db import models
from django.template import Context, loader

import re
# Create your models here.

def initializeAllProjects():
        # Remove all existing
        projects = Project.objects.all()
        for proj in projects:
            proj.delete()
        
        
        proj = Project()
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
        proj.save()
        

class Project(models.Model):
    
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    alt = models.CharField(max_length=255)
    
    date = models.CharField(max_length=100)
    years = models.CharField(max_length=20)
    tools = models.CharField(max_length=255)
    
    image_count = models.IntegerField(default=3)
    
    html = models.TextField(default="Info Here")
    
    design = models.BooleanField(default=False)
    programming = models.BooleanField(default=False)
    research = models.BooleanField(default=False)
    
    large_content = ""
    
    def description(self):
        t = loader.get_template('portfolio/templates/projects/' + self.slug + '.html')
        c = Context({
        })
        self.large_content = t.render(c)
        p = re.compile(r'<.*?>')
        description = p.sub('', self.large_content)
        if len(description) > 300:
            description = description[0:296] + " ..."
        
        return description
    
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
        t = loader.get_template('portfolio/templates/project.html')
        c = Context({
            "project": self
        })
        return t.render(c)
    
    def getInfo(self):
        if not self.large_content:
            t = loader.get_template('portfolio/templates/projects/' + self.slug + '.html')
            c = Context({
            })
            return t.render(c)
        else:
            return self.large_content

    
        
        