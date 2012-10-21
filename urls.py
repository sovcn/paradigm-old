from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^admin/$', include(admin.site.urls)),
    ('^about/$', 'portfolio.views.about'),
    ('^permission-denied/$', 'sc2meta.views.permission_denied'),
    ('^project/list/$', 'portfolio.views.projects'),
    ('^project/list/programming/$', 'portfolio.views.projects_programming'),
    ('^project/list/design/$', 'portfolio.views.projects_web_design'),
    ('^project/list/research/$', 'portfolio.views.projects_research'),
    ('^project/(?P<slug>[a-z0-9-]+)/$', 'portfolio.views.project_view'),
    ('^blog/$', 'blog.views.list'),
    ('^blog/create/$', 'blog.views.create'),
    ('^blog/edit/(?P<blog_id>\d+)/$', 'blog.views.create'),
    ('^blog/(?P<blog_id>\d+)/$', 'blog.views.view'),
    ('^blog/category/(?P<category>[a-z0-9-]+)/$', 'blog.views.list_category'),
    ('^blog/tag/(?P<slug>[a-zA-Z0-9-]+)/$', 'blog.views.list_tag'),
    ('^image/upload/$', 'blog.views.image_upload'),
    ('^image/(?P<image_id>\d+)/$', 'blog.views.image'),
    ('^image/info/(?P<image_id>\d+)/$', 'blog.views.image_info'),
    ('^image/(?P<image_id>\d+)/(?P<width>\d+)/$', 'blog.views.image'),
    ('^image/(?P<image_id>\d+)/(?P<width>\d+)/(?P<height>\d+)/$', 'blog.views.image'),
    ('^content/(?P<page_slug>[a-z0-9-]+)/$', 'sc2meta.views.content'),
    ('^accounts/', include('registration.backends.default.urls')),
    ('^profile/$', 'sc2meta.views.profile'),
    ('^profile/(?P<user_id>\d*)/$', 'sc2meta.views.profile'),
    ('^profile/edit/$', 'sc2meta.views.edit_profile'),
    ('^init/$', 'portfolio.views.init'),
    ('^ibd-admin/$', 'portfolio.views.admin'),
    ('^async/blog/add-category/$', 'blog.views.async_add_category'),
    ('^$', 'portfolio.views.index'),
)

urlpatterns += staticfiles_urlpatterns()