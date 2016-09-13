from django.conf.urls import url
from album import views

urlpatterns = [
 	url(r'^$', views.first_view, name='first-view'),
 	url(r'^category/$', views.category, name='category-list'), 
	url(r'^category/?(\d+)/detail/$', views.category_detail, name='category-detail'), 
 	url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
 	url(r'^photo/?(\d+)/detail/$',views.PhotoDetailView.as_view(), name='photo-detail'), 
]