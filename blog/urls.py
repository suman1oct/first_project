from django.conf.urls import url
from . import views

app_name= 'blog'

urlpatterns=[
	url(r'^$', views.PostView.as_view(), name='post'),
	url(r'^blog/(?P<pk>[0-9]+)/detail/$', views.PostDetailView.as_view(), name='post_detail'),
	url(r'^login/', views.LoginView.as_view(), name='login'),
	url(r'^dashboard/', views.DashboardView.as_view(), name='dashboard'),
	url(r'^registration/', views.RegistrationView.as_view(), name='registration'),
	url(r'^edit/(?P<pk>[0-9]+)/', views.EditView.as_view(), name='edit'),
	#url(r'^logout/', views.logout_view, name='logout'),
	url(r'^logout/', views.LogoutView.as_view(), name='logout'),
	url(r'^add/', views.AddView.as_view(), name='add'),
	url(r'^delete/(?P<pk>[0-9]+)/', views.DeleteView.as_view(), name='delete'),
	
	
]
