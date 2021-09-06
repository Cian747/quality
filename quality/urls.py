from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,AddImagesView,imageDetailsView,UpdateImagesView,DeleteImagesView, search_results
from . import views

urlpatterns=[
    path('',views.all_images,name = 'welcome'),
    path('image/<int:pk>',imageDetailsView.as_view(), name='image_details'),
    path('post/',AddImagesView.as_view(), name='addImage'),
    path('image/update_post/<int:pk>',UpdateImagesView.as_view(),name = 'update_post'),
    path('image/delete_post/<int:pk>/removed',DeleteImagesView.as_view(),name = 'delete_post'),
    url(r'^search/',views.search_results,name = 'search_category'),
    path('nav/location/<int:pk>',views.view_locations,name = 'all_locations'),
    url(r'^location/(\d+)',views.go_to_locations,name = 'view_locations'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)