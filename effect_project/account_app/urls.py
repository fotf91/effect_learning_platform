from django.conf.urls import patterns, url
from account_app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^connect$','account_app.views.register', name='register'),
        url(r'^login$','account_app.views.login', name='login'),
        url(r'^logout$','account_app.views.logout', name='logout'),
        # edit profile page - personal_profile.html
        url(r'^profile$','account_app.views.personal_profile', name='personal_profile'),
        url(r'^update_profile_Gtype$','account_app.views.update_profile_Gtype', name='update_profile_Gtype'),
        url(r'^update_profile_Ctype$','account_app.views.update_profile_Ctype', name='update_profile_Ctype'),
        url(r'^update_profile/$','account_app.views.update_profile', name='update_profile'),


        # old version methonds
        # url(r'^add_position$','account_app.views.add_position', name='add_position'),
        # url(r'^edit_position$','account_app.views.edit_position', name='edit_position'),
        # url(r'^delete_position$','account_app.views.delete_position', name='delete_position'),
        # url(r'^get_skill_list/$', views.get_skill_list, name='get_skill_list'), # get the list of skills after typing
        # url(r'^get_skills_id/$', views.get_skills_id, name='get_skills_id'), # get the list of ids of the skills the user already has
)
