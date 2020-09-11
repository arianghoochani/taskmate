
from django.contrib import admin
from django.urls import path , include
import todolist_app.urls
from todolist_app import views
import users_app.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('todolist/',include(todolist_app.urls)),
    path('account/', include(users_app.urls)),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

]
