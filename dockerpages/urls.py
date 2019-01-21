from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    #path('get-containers/',views.ListContainersUI,name='containers'),
    path('get-images/',views.images,name='images'),
    path('pull-image/',views.PullImage,name='pullimage'),
    path('contact-me/',views.contact,name='contact'),
    path('Image-Form/',views.Image_Form,name='ImageForm'),
    path('Remove-Image/',views.remove_image,name='remove_image'),
    path('stop-container/',views.stop_contianer),
    path('start-container/',views.start_container),
    path('create-container/',views.CreateContainerUI,name='create_container'),
    path('remove-container/',views.removecontainer),
    path('testing/',views.testing),
    path('get-containers/',views.SearchContainerUI,name='containers')
]

