from blog.models import Post, ImageModel, Category
import blog.views

from django.forms import ModelForm, TextInput
from django.forms.widgets import Input
from django import forms

from django.template import Context, RequestContext, loader

from django.utils.safestring import mark_safe

class TagInput(TextInput):
    def render(self, name, value, attrs=None):
        blog_info = blog.views.blog_processor()
        
        out = super(TagInput, self).render(name,value,attrs)
        out += '''
                <div class="spacer"><span class="helptext">Existing tags</span> | %s</div>
                <span id="cb_used_tags"></span>
                <input id="id_tags_hidden" type="hidden" name="tags_hidden" value ="" />''' % blog_info['tag_cloud'] 
                
        return mark_safe(out)   

class CategoryInput(Input):
    def render(self, name, value, attrs=None):
        
        categories = Category.objects.all()
        
        t = loader.get_template('form/element_categories.html')
        c = Context({
            "value": value,
            "categories": categories
        })
        
        out = t.render(c)
        
        return out
    
class ImageInput(Input):
    def render(self, name, value, attrs=None):
        
        if value:
            try:
                image = ImageModel.objects.get(pk=int(value))
            except ImageModel.DoesNotExist:
                image = None
        else:
            image = None
        
        images = ImageModel.objects.order_by('-added')[0:11]
        
        t = loader.get_template('form/element_images.html')
        c = Context({
            "name": name,
            "value": value,
            "images": images,
            "image": image
        })
        
        out = t.render(c)
        
        return out

class ContentInput(TextInput):
    def render(self, name, value, attrs=None):
    
        t = loader.get_template('form/element_content.html')
        c = Context({
            "value": value
        })
        
        out = t.render(c)
        
        return out

class PostForm(ModelForm):
    
    title_str = "Create Post"
    
    title = forms.CharField(required=True, label="", max_length=200, widget=forms.TextInput(attrs={'title': 'Title', 'class': 'basic-form-text-input'}))
    featured = forms.BooleanField(required=False, initial=False)
    draft = forms.BooleanField(required=False, initial=True, label="Draft?")
    is_project = forms.BooleanField(required=False, initial=False, label="Is Project?")
    
    image = forms.ImageField(label=None,widget=ImageInput,required=False,help_text="Images can be dragged into the content to place at the current position.")
    
    text_wysiwyg = forms.CharField(label="Content",widget=ContentInput)
    # Removed to allow for a more user friendly tag and category system.
    tags = forms.CharField(label="Tags", max_length=200,required=False,widget=TagInput, help_text="Click on existing tags or enter tags separated by commas.")
    categories = forms.CharField(label="Categories", max_length=200,required=False, widget=CategoryInput, help_text="Ctrl-click (Cmd-click on OSX) or click and drag to select multiple.")
    
    class Meta:
        model = Post
        exclude = ('title', 'featured', 'draft', 'is_project', 'banner_image', 'author', 'content', 'description', 'content_parsed', 'image_file')
        
class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        exclude = ('thumb_key', 'large_key')