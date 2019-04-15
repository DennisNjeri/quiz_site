from django.conf.urls import url #patterns,

#from .views import
from . import views

urlpatterns = [
                # new home-page link
                url( r'^$', views.homeView.as_view(), name='graphs_home' ),
                url( r'^Ematerials/$', views.resourcesView.as_view(), name='Ematerials' ),
                url( r'^Teacherprofile/$', views.teacherView.as_view(), name='Teacherprofile' ),
                url( r'^Erupload/$', views.UploadView.as_view(), name='Teacherprofile' ),
                
              ]
