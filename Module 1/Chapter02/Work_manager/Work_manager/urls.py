from django.urls import include, re_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    re_path(r'^admin/', include(admin.site.urls)),
]
