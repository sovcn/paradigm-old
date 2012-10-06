from django.db import models
from django.template import Context, loader
from sc2meta.models import UserProfile

from google.appengine.api.images import get_serving_url

class ImageModel(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    caption = models.CharField(blank=True,max_length=255)
    
    added = models.DateTimeField(auto_now_add=True)
    
    featured = models.BooleanField(default=False)
    
    thumb_key = models.TextField(null=True)
    large_key = models.TextField(null=True)
    
    def __unicode__(self):
        return str(self.caption)
    
    def url(self, width=None, height=None):
        if width or height:
            return get_serving_url(blob_key=self.file.file.blobstore_info._BlobInfo__key) + "=s" + str(width)
        else:
            return get_serving_url(blob_key=self.file.file.blobstore_info._BlobInfo__key)
        
    def thumbnail(self):
        return self.url(200,150)
    
    def thumbnail_medium(self):
        return self.url(100,100)
    
    def thumbnail_small(self):
        return self.url(75,75)
        
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    content_parsed = models.TextField(blank=True)
    description = models.TextField(blank=True,max_length=500)
    
    image_file = models.ForeignKey(ImageModel,blank=True,null=True)

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    author = models.ForeignKey(UserProfile)
    
    featured = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    #web_design = models.BooleanField(default=False) # Depreceated - KS 2/1/2012
    #programming = models.BooleanField(default=False) # Depreceated
    
    def parse_tags(self, tag_string):
        tags = tag_string.split(",")
        existing_tags = self.get_tags()
        
        # Remove missing tags from post
        for tag in existing_tags:
            if tag not in tags:
                try:
                    # This could probably be done in one query
                    conn = PostTag.objects.get(post=self,tag=tag)
                    conn.delete()
                except PostTag.DoesNotExist:
                    continue # somethign weird has happened
                except PostTag.MultipleObjectsReturned:
                    continue # something weird has happened
        
        iTag = None # Global for this function
        if tags[0] != "":
            for tag in tags:
                try:
                    iTag = Tag.objects.get(slug=tag)
                except Tag.DoesNotExist:
                    iTag = Tag(slug=tag)
                    iTag.save()
                
                # Don't create replicate entries
                try:
                    conn = PostTag.objects.get(post=self,tag=iTag)
                except PostTag.DoesNotExist:
                    conn = PostTag(post=self, tag=iTag)
                    conn.save()
                except PostTag.MultipleObjectsReturned:
                    continue

    def parse_categories(self, cat_string):
        cats = cat_string.split(",")
        category = None
        
        existing_categories = self.get_categories()
        
        # Remove missing tags from post
        for cat in existing_categories:
            if cat not in cats:
                try:
                    # This could probably be done in one query
                    conn = PostCategory.objects.get(post=self,category=cat)
                    conn.delete()
                except PostCategory.DoesNotExist:
                    continue # somethign weird has happened
                except PostCategory.MultipleObjectsReturned:
                    continue # something weird has happened
        
        if cats[0] != "":
            for cat in cats:
                try:
                    category = Category.objects.get(name=cat)
                except Category.DoesNotExist:
                    category = Category(name=cat,label="Label",description="Default description...")
                    category.save()
                
                # Don't create replicate entries
                try:
                    conn = PostCategory.objects.get(post=self,category=category)
                except PostCategory.DoesNotExist:
                    conn = PostCategory(post=self,category=category)
                    conn.save()
                except PostTag.MultipleObjectsReturned:
                    continue
    
    def get_categories(self):
        conns = PostCategory.objects.filter(post=self)
        categories = []
        for conn in conns:
            categories.append(conn.category)
            
        return categories
    
    def get_tags(self):
        conns = PostTag.objects.filter(post=self)
        tags = []
        for conn in conns:
            tags.append(conn.tag)
            
        return tags
    
    @staticmethod    
    def generateImage(image, width, height, link=None):
        if not link:
            link = image.url(width, height)
        
        t = loader.get_template('post_image.html')
        c = Context({
            "image_id": image.pk,
            "image_url": image.url(width, height),
            "image_caption": image.caption,
            "image_height": height,
            "image_width": width,
            "image_link": link
        })
        return t.render(c)

class Tag(models.Model):
    slug = models.CharField(max_length=30)
    
    def __unicode__(self):
        return str(self.slug)
    
    @staticmethod
    def generateCloud(tags):
        #List of tags as argument
        cloud = {}
        for tag in tags:
            tagCount = len(PostTag.objects.filter(tag=tag))
            cloud[tag] = tagCount
        
        return cloud
    
# Connection Model
class PostTag(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)

    
class Category(models.Model):
    name = models.CharField(max_length=30)
    label = models.CharField(max_length=30,blank=True)
    description = models.TextField(blank=True,max_length=1000)
    
    def get_posts(self):
        conns = PostCategory.objects.filter(category=self)
        posts = []
        for conn in conns:
            posts.append(conn.post)
    
    def link(self):
        return '<a href="/blog/category/' + self.name + '">' + self.label + '</a>'

class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)
    
class Comment(models.Model):
    
    post = models.ForeignKey(Post)
    
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, max_length=1000)
    
    author = models.ForeignKey(UserProfile)