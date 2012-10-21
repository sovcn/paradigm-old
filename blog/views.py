from django.core import serializers 

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, RequestContext, loader
from django.core.urlresolvers import reverse

from blog.forms import PostForm, ImageForm

from blog.models import Post, Category, Tag, ImageModel, PostCategory, PostTag

from filetransfers.api import prepare_upload, serve_file

from google.appengine.api import images
from google.appengine.api.images import get_serving_url
from google.appengine.api import files

import re, logging

from django.utils import simplejson

### START CONTEXT PROCESSORS ###
def blog_processor(request=None):
    # Loads category and tag information for displaying
    posts = Post.objects.filter(featured=True, is_project=False)
    posts = sorted(posts, key=lambda post: post.added, reverse=True)
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cloud = Tag.generateCloud(tags)
    
    t = loader.get_template('tag_link.html')
    
    out = ""
    for tag, count in cloud.items():
        c = Context({
            "tag": tag
        })
        if count >= 10:
            c.update({"tag_class": "biggest"})
        elif count >= 6:
            c.update({"tag_class": "big"})
        elif count >= 4:
            c.update({"tag_class": "medium"})
        elif count >= 2:
            c.update({"tag_class": "small"})
        else:
            c.update({"tag_class": "smallest"})
        
        out += t.render(c)
            
    return {"featured": posts, "categories": categories, "tag_cloud": out, 'page_id': 'blog'}

### END CONTEXT PROCESSORS ###

### START BASIC VIEWS ###

def list(request):
    posts = Post.objects.filter(is_project=False)
    
    t = loader.get_template('blog_list.html')
    c = RequestContext(request,{
        "posts": posts
    }, [blog_processor])
    
    return HttpResponse(t.render(c))
    
def list_category(request, category):
    
    category = get_object_or_404(Category, name=category)
    conn = PostCategory.objects.filter(category=category)
    posts = []
    for connection in conn:
        try:
            posts.append(connection.post)
        except (Post.DoesNotExist):
            pass
    
    posts = sorted(posts, key=lambda post: post.added, reverse=True)
    
    t = loader.get_template('blog_list.html')
    c = RequestContext(request,{
        "candy_trail": '<a href="/blog">Home</a> -> <strong>%s</strong>' % (category.label),
        "title": category.label,
        "sub_title": category.description,
        "posts": posts
    }, [blog_processor])
    
    return HttpResponse(t.render(c))

def list_tag(request, slug):
    slug = slug
    tag = get_object_or_404(Tag, slug=slug)
    conn = PostTag.objects.filter(tag=tag)
    posts = []
    for connection in conn:
        try:
            posts.append(connection.post)
        except (Post.DoesNotExist):
            pass
    
    posts = sorted(posts, key=lambda post: post.added, reverse=True)
    
    t = loader.get_template('blog_list.html')
    c = RequestContext(request,{
        "candy_trail": '<a href="/blog">Home</a> -> <strong>Tag: %s</strong>' % (tag.slug),
        "title": "Tag: " + tag.slug,
        "sub_title": "",
        "posts": posts
    }, [blog_processor])
    
    return HttpResponse(t.render(c))

def view(request, blog_id):
    post = get_object_or_404(Post, pk=int(blog_id))
    
    og_image = None
    if post.image_file:
        og_image = post.image_file.thumbnail()
    elif "[image=" in post.content:
        # Parse the image to get the url
        image = re.compile("\[image=\d+,\d+,\d+\]")
        match = image.search(post.content).group(0)
        info = match.replace("[image=", "")
        info = info.replace("]", "")
        nums = info.split(",")
        
        try:
            img_file = ImageModel.objects.get(pk=int(nums[0]))
            og_image = img_file.thumbnail()  
        except ImageModel.DoesNotExist:
            og_image = None
    else:
        og_image = None
    
    t = loader.get_template('post_view.html')
    c = RequestContext(request,{
        "candy_trail": '<a href="/blog">Blog</a> - <strong>' + post.title + '</strong>',
        "post": post,
        "og_image": og_image
    }, [blog_processor])
    
    return HttpResponse(t.render(c))

@login_required
def create(request,blog_id=None):
    
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            
            added = None
            if blog_id:
                old_post = get_object_or_404(Post, pk=int(blog_id))
                added = old_post.added
                old_post.delete()
            
            post = form.save(commit=False)
            if blog_id:
                post.pk = blog_id
                post.added = added # Preserve the date of the old post
                
            post.title = form.cleaned_data['title']
            post.author = request.user.userprofile
            post.content_parsed = post.content = form.cleaned_data['text_wysiwyg']
            
            post.featured = form.cleaned_data['featured']
            post.draft = form.cleaned_data['draft']
            post.is_project = form.cleaned_data['is_project']
            
            # Parse for images
            image = re.compile("\[image=\d+,\d+,\d+\]")
            matches = image.findall(post.content_parsed)
            for match in matches:
                info = match.replace("[image=", "")
                info = info.replace("]", "")
                nums = info.split(",")
                try:
                    img_file = ImageModel.objects.get(pk=int(nums[0]))
                    width = int(nums[1])
                    height = int(nums[2])
                    code = str(Post.generateImage(img_file, width, height))
                    post.content_parsed = post.content_parsed.replace(match,code)
                    
                except ImageModel.DoesNotExist:
                    post.content_parsed = post.content_parsed.replace(match,"Invalid Image Id")
            
            
            # Geneerate Description
            p = re.compile(r'<.*?>')
            nohtml = p.sub('', post.content_parsed)
            if len(nohtml) > 500:
                post.description = nohtml[0:496] + " ..."
            else:
                post.description = nohtml
                
                
            try:
                if not (request.POST['image_hidden'] == 'None'):
                    post.image_file = ImageModel.objects.get(pk=int(request.POST['image_hidden']))
                else:
                    post.image_file = None
                
                post.save()
                
                post.parse_tags(request.POST['tags_hidden'])
                post.parse_categories(request.POST['categories_hidden'])
                
                return HttpResponseRedirect('/blog/' + str(post.pk)) # Redirect after POST
                
            except (ImageModel.DoesNotExist, ImageModel.MultipleObjectsReturned):
                form.errors.append("Invalid image file.");
            

    else:
        if not blog_id == None:
            post = get_object_or_404(Post, pk=int(blog_id))
            
            tags = post.get_tags()
            categories = post.get_categories()
            
            tag_string = ""
            for tag in tags:
                tag_string += str(tag.slug) + ","
            tag_string = tag_string[0:len(tag_string)-1]
            
            cat_string = ""
            for category in categories:
                cat_string += str(category.name) + ","
            cat_string = cat_string[0:len(cat_string)-1]
            
            #try:
            image_file_pk = None
            if(post.image_file is not None):
                image_file_pk = post.image_file.pk
            form = PostForm(initial={"title": post.title, "featured": post.featured, "draft": post.draft, 
                                         "text_wysiwyg":post.content_parsed,"tags": tag_string,"categories": cat_string, 
                                         "image": image_file_pk},instance=post)
            '''except AttributeError:
                # Post objects don't have a Draft attribute yet.
                # This was added in to fix an error that happened when adding a  new attribute to a post
                posts = Post.objects.all()
                for post in posts:
                    post.draft = False
                    post.save()
                #return HttpResponseRedirect(request.get_full_path())'''
                
        else:
            form = PostForm()
        

    t = loader.get_template('create_post.html')
    c = RequestContext(request,{
        'form': form,
        'title': 'Blog Post'
    })
    
    return HttpResponse(t.render(c))

@login_required
def image_upload(request):
    view_url = reverse('blog.views.image_upload')
    if request.method == 'POST': # If the form has been submitted...
        form = ImageForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            image = form.save()
            
            return HttpResponseRedirect('/image/info/' + str(image.pk)) # Redirect after POST

    else:
        form = ImageForm()
        
    upload_url, upload_data = prepare_upload(request, view_url)

    t = loader.get_template('image_upload.html')
    c = RequestContext(request,{
        'form': form,
        'title': 'Image Upload',
        'upload_url': upload_url, 
        'upload_data': upload_data
    })
    return HttpResponse(t.render(c))

# Depreceated....
def image(request, image_id, width=None, height=None):
    image = get_object_or_404(ImageModel, pk=image_id)
    
    width = int(width)
    height = int(height)
    
    if width or height:
        img = images.Image(blob_key=image.file.file.blobstore_info._BlobInfo__key)

        if height:
            img.resize(width=int(width),height=int(height))
        else:
            img.resize(width=int(width),height=int(width))
        img.im_feeling_lucky()
        img_out = img.execute_transforms(output_encoding=images.JPEG)

            
        
        response = HttpResponse(img_out)
        response['Content-Type'] = "image/JPEG"
        response['Cache-Control'] = "max-age=36000"
        return response
    else:
        return serve_file(request, image.file)
    
def image_info(request, image_id):
    image = get_object_or_404(ImageModel, pk=image_id)
    image_code = Post.generateImage(image, 500, 500, image.url())
    
    posts = Post.objects.all().order_by("-added")
    posts_out = []
    for post in posts:
        try:
            if "[image=" + str(image_id) in post.content or (post.image_file and post.image_file.pk == image_id):
                posts_out.append(post)
        except ImageModel.DoesNotExist:
            pass
    
    t = loader.get_template('image_info.html')
    c = RequestContext(request,{
        "candy_trail": '<a href="/blog">Home</a> -> <strong>Image: ' + image.caption + '</strong>',
        "title": "Image Info",
        "sub_title": "",
        "image_code": image_code,
        "posts": posts_out
    }, [blog_processor])
    
    return HttpResponse(t.render(c))

### END BASIC VIEWS ###

### START AJAX VIEWS ###
def async_add_category(request):
    if not request.POST:
        raise Http404
    
    data = {}
    
    name = request.POST.get('name', False)
    slug = request.POST.get('slug', False)
    if name == False or slug == False:
        data.update({"status": False, "message": "Invalid data."})
    elif len(name) == 0 or len(slug) == 0:
        data.update({"status": False, "message": "Neither field can be blank."})
    else:
        try:
            cat = Category(name=slug,label=name) # Stupid naming of the model.  Don't feel like fixing all references..
            cat.save()
            data.update({"status": True, "message": "Category successfully added.", 
                         "slug": cat.name, "name": cat.label})
        except:
            data.update({"status": False, "message": "An unknown error occured. Please reload the page."})
    
    return HttpResponse(simplejson.dumps(data), mimetype="application/javascript")

### END AJAX VIEWS ###
    