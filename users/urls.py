# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.static import serve

from . import views

#from django.views.generic import TemplateView

urlpatterns = [

	# home/index page for app[ users ]
	url( r'^$', views.indexView.as_view(), name="users_index_link" ),

	# view [ login ]
	url( r'^login/$', views.loginView.as_view(), name='users_login_link' ),
	# (?P<site_msg>[^\/]*)/

	# view [ Register ]
	url( r'^register/$', views.registerView.as_view(), name='users_register_link' ),

	# view-function [ Logout ]
	url( r'^logout/$', views.logoutFunctionView, name='users_logout_link' ),

	# view [ profile details ]
	url( r'^profile_details/$', views.profileView.as_view(), name='profile_details_link' ),

	# testing django-bootstrap4
  	url( r'^testpage/$', views.testView.as_view(), name='test_link' ),

  	#chartView
  	#url( r'^userchart/$', views.chartView.as_view(), name='Charts' ),
  	#url( r'^userchart/(?P<slug>[\w-]+)/$', views.chartView.as_view(), name='Charts' ),
  	#url(r'^user/(?P<user_id>\d+)/profile/$', views.chartView.as_view(), name='user_url'),
    #progress
  	#url( r'^userprogress/$', views.getdataView.as_view(), name='progress' ),
  	#updateprofileview
  	url( r'^updateprofile/$', views.updateView.as_view(), name='Edit_Profile' ),
  	url( r'^analysisfeed/$', views.analysisView.as_view(), name='analysis' ),

  	# pdfView
	url( r'^pdf/$', views.pdfView.as_view(), name='pdf_link' ),

	#media urls
	#url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT })

]