from django.urls import path
from .views import (
    GlobaslView,
    PostsDetailView, 
    ManagmentView, 
    SectionsView, 
    RegionalView, 
    NewsView, 
    NewsDetailView, 
    ActinView,
    SearchResulView, 
    Contact,
    InformationView,
    ElementView,
    PostDetailView,
    DocFile,
    MediaPhotoView,
    MediaVideoView,
    PhotoDetailView,
    
    ElonListView,
)


urlpatterns = [
    path('', GlobaslView.as_view(), name='gmenyu'),
    path('management/', ManagmentView.as_view(), name='management'),
    path('aparat/', SectionsView.as_view(), name='section'),
    path('regional/', RegionalView.as_view(), name='regional'),
    path('news/', NewsView.as_view(), name='news'),
    path('doc_f/<int:pk>/', DocFile.as_view(), name='doc_file'),
    path('news/<slug:NewsSlug>/', NewsDetailView.as_view(), name='news_d'),
    path('elon/<slug:PostSlug>/', PostDetailView.as_view(), name='posts_d'),
    path('elon_l/', ElonListView.as_view(), name='elonlar'),

    path('menu/<int:pk>/', ElementView.as_view(), name='element_items'),
    path('menu/<int:pk>/', ElementView.as_view(), name='element_items'),
    
    path('photos/', MediaPhotoView.as_view(), name="photo"),
    path('videos/', MediaVideoView.as_view(), name="video"),
    path('photos/<slug:PhotoSlug>/', PhotoDetailView.as_view(), name="photo_detail"),
    


    path('actions/', ActinView.as_view(), name="action_view"),
    path('search/', SearchResulView.as_view(), name="search"),
    path('contact/', Contact.as_view(), name="contact"),
]