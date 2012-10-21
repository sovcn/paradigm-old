from django.db import models
from django.template import Context, loader

import blog
import re
from datetime import datetime
from django.utils.html import strip_tags
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
        
        if hasattr(request.user, 'userprofile'):
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Innovation by Design"
            post.content = "Innovation by Design was my first portfolio website, which was replaced by the website you are currently browsing in October, 2012. This project was originally constructed in 2009, and has gone through several iterations since."
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
            proj.images = "http://lh6.ggpht.com/PfJGBjbg451_lJVCC8PWgJLkplcBSMeI52f4hupP1mrsWEhxB-B3dxV8LXyYCISqodymRL-dPp2Iu8uupjrFZw_fxg"
            proj.main_html = "innobdesign.html"
            proj.aside_html = "innobdesign_aside.html"
            
            proj.design = True
            proj.programming = True
            proj.save()





            proj = Project()
            post = blog.models.Post()
            
            post.title = "Platform Independent Cloud Scripting"
            post.content = "In recent years it has become well understood that Moore's promised exponential growth in computational power can only continue if there is a shift in the fundamental design of software to exploit parallelism. Previous work has been done in minimizing the inherent difficulties of parallel programming, however in the same way that scripting and high-level languages represent a natural progression towards ease of development and platform independence, so too does this research represent a progression from these other parallelization methods to a Platform Independent Cloud Scripting (PICS) method."
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = True
            post.is_project = True
            
            post.save()
            proj.post = post
            
            proj.slug = "pics"
            proj.alt = proj.post.title
            proj.date = datetime(year=2012, month=5, day=1)
            proj.years = "2010-2012"
            proj.images = "http://lh6.ggpht.com/ugneQwpPhrfsLbqWKc6BSpTSsOrm6J8p2MorG0uyPC_-LYaEMDAiscZksRo_aWaEvSQMgBxmCgcnd1fP4lgWBL7W,http://lh4.ggpht.com/a1JqjaCAb6NJeSxsbEaC6sJqlQpBW_YJhsCSd2j1lFhi_OJ4lrdND_AMO3d8Or7-ks-JlK3eacml9PGO3A2CnonM0A,http://lh6.ggpht.com/m3VrKcmV8b0lJGS_wz9mNF0ZHBATAqDKj9Mypk5aCPicxE3aGUhmoTgNfbutD6bU27wBNQTuTVnEQFezLzji4QJtrg,http://lh4.ggpht.com/2vBbXPD7SOAJliN5rJXFZ2E5BclQhwFoxGMMiTpVgs-DZYyLaxMDUs83vCg-jXThNI6kbrw2bF-8cwq0neL9uqABAQ"
            proj.main_html = "pics.html"
            proj.aside_html = "pics_aside.html"
            
            proj.design = False
            proj.programming = True
            proj.research = True
            proj.save()
            
            
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Google Summer of Code"
            post.content = "This project was part of work that I did for Google's Summer of Code 2010. I worked together with a JavaScript consultant from Germany to design a sensor API plugin for the Dojo JavaScript framework. I worked closely with my mentoring organization (Dojo Toolkit) to develop a JavaScript API for accessing geolocation, accelerometer, and camera features on a variety of mobile devices and platforms including PhoneGap, W3C compliant browsers, WebOS, Bondi, and JIL."
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = True
            post.is_project = True
            
            post.save()
            proj.post = post
            
            proj.slug = "sensor"
            proj.alt = proj.post.title
            proj.date = datetime(year=2010, month=8, day=1)
            proj.years = "2010"
            proj.images = "http://lh5.ggpht.com/7yNwtQjF6jey8o5slxc6OOHggEYao12mrFSl-aWA_1NUxERBIate3-oHb6kzZHRcty4S1aODMDx1vpGXJV1vfF2S_L4"
            proj.main_html = "sensor.html"
            proj.aside_html = "sensor_aside.html"
            
            proj.design = False
            proj.programming = True
            proj.research = False
            proj.save()
            
            
            
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Starcraft Metagame Central"
            post.content = '''This project is currently a work in progress.  The goal is to create a 1-stop website
                            for all things related to competitive Starcraft 2.  Right now, much of the foundation,
                            user framework, and web design is finished, however I just don't have the time right now
                            to see the rest of the project come to fruition. I will be looking for more time to finish
                            what I've started, but for now I am content to use the <a href="http://www.allbuttonspressed.com/projects/django-nonrel">Django-nonrel</a> base that I have finished
                            to deploy other smaller web apps on <a href="http://code.google.com/appengine/">Google App Engine</a>.
                            '''
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = False
            post.is_project = True
            
            post.save()
            proj.post = post
            
            proj.slug = "sc2meta"
            proj.alt = proj.post.title
            proj.date = datetime(year=2011, month=8, day=1)
            proj.years = "2011"
            proj.images = "http://lh3.ggpht.com/EEVEXEsxd-HMu24L5e41Zg_03u8ZAuyiHTbTUUknBZLYzToG1pGD_Sjxn64Ih2yzcEtg8uQt_M4gr3FUTnl45-uyvg"
            proj.main_html = "sc2meta.html"
            proj.aside_html = "sc2meta_aside.html"
            
            proj.design = True
            proj.programming = True
            proj.research = False
            proj.save()
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Sovereign Clan Manager"
            post.content = '''Sovereign Clan Manager is a content management system that I built from the ground up while in high school. 
                                It is designed to provide a seamless web interface that allows gaming communities to organize and keep track of their members, 
                                news, and other gaming related content.
                            '''
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = False
            post.is_project = True
            
            post.save()
            proj.post = post
            
            proj.slug = "scm"
            proj.alt = proj.post.title
            proj.date = datetime(year=2009, month=5, day=1)
            proj.years = "2007-2009"
            proj.images = "http://lh3.ggpht.com/sCu1AidocSS6Fdo2-FW-4GjEh-e4T6bdOg8oKs19_3U4p1Qu270G4m0zHA9UTwX5pTIuP3E24E4py6Dz2O1rkVy2hg"
            proj.main_html = "scm.html"
            proj.aside_html = "scm_aside.html"
            
            proj.design = True
            proj.programming = True
            proj.research = False
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
        
        return strip_tags(self.post.description)
    
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
    
    def hasImages(self):
        if(len(self.images) > 0 and len(self.images.split(",")) > 0):
            return True;
    
    def getPrimaryImage(self):
        if self.hasImages():
            return self.images.split(",")[0]
    
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
        except (blog.models.Post.DoesNotExist, AttributeError):
            pass
        super(Project, self).delete(*args, **kwargs)
    
    
    def getAside(self):
        t = loader.get_template('portfolio/templates/projects/' + self.aside_html)
        c = Context({
            "project": self
        })
        return t.render(c)

    
        
        