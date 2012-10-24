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
            post.parse_tags("Python,PHP,jQuery,Django,Zend-Framework,Photoshop,AppEngine,Paradigm")
            
            proj.post = post
            
            proj.slug = "innobdesign"
            proj.alt = proj.post.title
            proj.date = datetime(year=2011, month=11, day=1)
            proj.years = "2009-2011"
            proj.images = "http://lh6.ggpht.com/PfJGBjbg451_lJVCC8PWgJLkplcBSMeI52f4hupP1mrsWEhxB-B3dxV8LXyYCISqodymRL-dPp2Iu8uupjrFZw_fxg,http://lh4.ggpht.com/cehVbp4isx0fhKykKFoKscy-jdXX864UADOCUift7b9ThSIzzBL8Jugqq3F_a5TWBZNEkhGe0SAT_P_rRGImK5b_,http://lh4.ggpht.com/2p16wy9P_XddGSs1pmJrn6a5UE2BzsUisMUEvuvBMaLDj2ca41BDu6y0NGEL4pxvOWbsP-PRhwoVpHD-t1QWyeaQyA,http://lh5.ggpht.com/9w-4OPz5ny8tIoX7YuHH1c1HzC6R-c3MqN7RCahEMwL8WXVvfMtBjdt1qjfL5yr_ioOjBnGZuiDOeJD_XQkIt0HElpY"
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
            post.parse_tags("Python,JavaScript,Node.js,Android,MySQL,v8-engine")
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
            post.parse_tags("JavaScript,Dojo-Toolkit,Android,PhoneGap,HTML5,Bondi,JIL,WebOS,reStructured-Text")
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
            post.parse_tags("JavaScript,jQuery,Photoshop,Python,Django,AppEngine,Paradigm")
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
            post.parse_tags("PHP,MySQL,Photoshop,JavaScript,Gaming,Clans")
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
            
            
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Paradigm Framework"
            post.content = '''Paradigm is a Python framework for deploying professional portfolio and blog websites to Google's AppEngine.  Currently it is a work in progress,
                              but it has been released on GitHub as an open source project and will continue to be developed whenever I have time to devote to it.  The website that
                              you are currently browsing is running on the Paradigm Framework.
                            '''
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = True
            post.is_project = True
            
            post.save()
            post.parse_tags("Python,Django,AppEngine,Photoshop,Framework,JavaScript,jQuery,HTML5,Paradigm")
            proj.post = post
            
            proj.slug = "paradigm"
            proj.alt = proj.post.title
            proj.date = datetime(year=2012, month=10, day=22)
            proj.years = "2011-2012"
            proj.images = "http://lh5.ggpht.com/XVFO8wiASrEyUkAwpH0B3L7V2ys4Q641xxTVPkXTDJzgrH2ce1TrQY7zAMzEAHWLr6TktDlMJ-g3lUFabb57ufTzow,http://lh3.ggpht.com/Y5h-75bPkv-cO9wL7JTsWhYG7umR7YAWYDNglSOIzN-fGmhp6Ibbqol90Li7hJ1hP4XgsvInYHOFNmVkHNoYV1wbIi0,http://lh5.ggpht.com/e7Std_2HVmiOuVHZObm4dywFpfkqQpcR52_KWRyyNcu6wDykyYnO_sF8HoWbYQplhnA--Rkl4H4GsnxYjMIMJoXAaA"
            proj.main_html = "paradigm.html"
            proj.aside_html = "paradigm_aside.html"
            
            proj.design = True
            proj.programming = True
            proj.research = False
            proj.save()
            
            
            
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Mandelbrot CUDA"
            post.content = '''This project was done as the final project for CPSC 474: Computer Architecture. Roughly 1/3 of this course was dedicated to learning about parallel architectures: two of which are used extensively in this project (CUDA and OpenMP). This research was presented at Slippery Rock University's annual student research symposium.
                            The primary focus of this research was to develop a method for generating mandelbrot fractal images using both OpenMP and CUDA and to compare different aspects of their performance. Additionally, a system for performing arbitrary precision calculations was developed and implemented on both parallel platforms.
                            '''
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = True
            post.is_project = True
            
            post.save()
            post.parse_tags("C++,CUDA,OpenGL,OpenMP,Arbitrary-Precision,Fractal")
            proj.post = post
            
            proj.slug = "mandelbrot"
            proj.alt = proj.post.title
            proj.date = datetime(year=2010, month=12, day=16)
            proj.years = "2010"
            proj.images = "http://lh6.ggpht.com/U-FdrS9fZhJQc8Q9FdILmPQ4xmgkMuitO1HlxJX_Yq9pXAIGKqH-lY3fb-KosuZwYYxotO0-bhY4bhuqUwRutA_HlQ"
            proj.main_html = "mandelbrot.html"
            proj.aside_html = "mandelbrot_aside.html"
            
            proj.programming = True
            proj.research = True
            proj.save()
            
            
            
            proj = Project()
            post = blog.models.Post()
            
            post.title = "Sudoku: Optimization Through Heuristics"
            post.content = '''This project started out as a research project that I was working on for a class but has quickly become more than that. 
            Initially I had written a series of algorithms in C and Objective-C on the iPhone that solve sudoku puzzles using "logical" methods similar 
            to those that a human would use. As the project progressed I decided that I wanted to make it multi-platform so I modified a http server written in 
            Objective-C and created an XML-RPC web service to solve sudoku problems using the same code from the iPhone and serve them to any platform. With 
            that in place I wrote a simple development environment in PHP and MySQL that can run a multitude of tests in an attempt to find more efficient ways of 
            solving sudoku puzzles.
                            '''
            post.content_parsed = post.content
            post.description = post.content
            
            post.banner_image = ""
            post.author = request.user.userprofile
            
            post.featured = True
            post.is_project = True
            
            post.save()
            post.parse_tags("iOS,Objective-C,PHP,MySQL,Photoshop,XML-RPC,Web-Service")
            proj.post = post
            
            proj.slug = "sudoku"
            proj.alt = proj.post.title
            proj.date = datetime(year=2009, month=9, day=25)
            proj.years = "2009"
            proj.images = "http://lh3.ggpht.com/iE_JegVct4YW8qmEDytYbiVyQ-olVvHeyvHVinbwQ0A12Q-j_GrytG0k3j6TWalnScq_MB9ZQ3gax8dac6w_tG4X,http://lh4.ggpht.com/0WbFloxeDTcU9ivfYcj7V2gtv_8xQIW4wBi5USX3DnP-q9JmaXBbPpwDQ6V9Wr8jL01B2rRaU6VJ8kW_h5H1ElMw,http://lh6.ggpht.com/uBEsH7yaeB36_-1iZGh8-_sQJp10h8z0BWJPTlVQFIjPjYaI7WoOrEU_3wD1zQYmr2QhZMwsRuYpgcEsAUCDZeEgVQ"
            proj.main_html = "sudoku.html"
            proj.aside_html = "sudoku_aside.html"
            
            proj.programming = True
            proj.research = True
            proj.design = True
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
        
        return self.post.getDescription
    
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

    
        
        