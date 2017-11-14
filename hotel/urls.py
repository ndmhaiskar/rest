"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
# from restaurants.views import home, about, contact, ContactView
from restaurants.views import HomeView
from menus.views import HomeView
from profiles.views import ProfileFollowToggle
from profiles.views import ProfileFollowToggle, RegisterView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

"""from restaurants.views import (
    restaurant_listview, restaurant_detailview, restaurant_createview,
    RestaurantListView, RestaurantDetailView, RestaurantCreateView
)"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^$', HomeView.as_view()), How django works
    # url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^menus/', include('menus.urls', namespace='menus')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    # url(r'^restaurants/$', restaurant_listview),
    # url(r'^restaurants/create/$', restaurant_createview),
    # url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
    # url(r'^restaurants/$', RestaurantListView.as_view()),
    # url(r'^restaurants/create/$', restaurant_createview),
    # url(r'^restaurants/$', restaurant_detailview),
    # url(r'^restaurants/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<rest_id>\w+)$', RestaurantDetailView.as_view()),
    # url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    # url(r'^contact/$', contact),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
