from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from catalog import views as catalog_views

urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', user_views.login, name='login'),
    path('search/', catalog_views.search, name='search'),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('movie/', include('catalog.urls')),
]
