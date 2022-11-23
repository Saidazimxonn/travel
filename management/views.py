from math import ceil
from urllib import response
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,View
from .models import (
    CategoryDoc, 
    Managment, 
    Sections, 
    RegionalCenters, 
    Post, 
    Poster,
    FaieldFiled, 
    Information, 
    MenuCategory,
    Media_type,
    Media
)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render
from django.urls import reverse
from .helpers import create_ad
from django.contrib import messages
from django.db.models import Q
from django.views.generic.list import MultipleObjectMixin
import requests
import json
# Create your views here.

def context(request):
 
    return render(request, 'index.html')
    
class InformationView(DetailView):
    model = MenuCategory
    model = Information
    
    template_name = 'base.html'
    
   

    def get_context_data(self, **kwargs):
        context = super(InformationView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # print(pk,"=========================")
        categor = MenuCategory.objects.all()
        print(categor,"=========================")
        context['men222u'] = Information.objects.all()
        context['elem22ent'] = categor
        return context

class ElementView(DetailView):
    model = Information
    template_name = 'engyaxshimanzillar/manzil.html'
    context_object_name = 'element_item'

    def get_context_data(self, **kwargs):
        context = super(ElementView, self).get_context_data(**kwargs)
        context['news'] = Post.objects.all().order_by('-date')[1:7]

        return context


class GlobaslView(TemplateView):
    template_name = 'index.html'
    model = Post
    model = Poster
    model = FaieldFiled
    model = Media
    # def add(request):
    #     response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Samarkand&mode=json&units=metric&appid=be6e7f0f7386c829ba7f4931a44ff58d")

    #     # Вывод 
    #     d=response.json()
    #     ip=d['main']['temp']
    #     context['dt']=ip
    #     return context

    def get_context_data(self,**kwargs):
        context = super(GlobaslView, self).get_context_data(**kwargs)
        context['news'] = Post.objects.all().order_by('-date')[0:7] 
        context['media_vedio_list'] = Media.objects.filter(category_id=2)
        # context['news2'] = Post.objects.all().order_by('-date')[1:3]
        # context['news3'] = Post.objects.all().order_by('-date')[4:7]
        context['media_photo_list'] = Media.objects.filter(category_id=1)

        # context['categor'] = CategoryDoc.objects.all().order_by('-date')

        
        # response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Samarkand&mode=json&units=metric&appid=be6e7f0f7386c829ba7f4931a44ff58d")
        # d=response.json()
        # ip=ceil(d['main']['temp'])
        context['dt']=1
        
        
        context['poster'] = Poster.objects.all().order_by('-date')[0:3] 
        return context




# class Category(ListView):
class ManagmentView(TemplateView):
    template_name = 'Rahbaryat/rahbaryat.html'
    model = Managment
    def get_context_data(self, **kwargs):
        context = super(ManagmentView, self).get_context_data(**kwargs)
        context['managers_list'] = Managment.objects.all().reverse()
        return context


class SectionsView(TemplateView):
    template_name = 'Rahbaryat/xodimlar.html'
    model = Sections
    def get_context_data(self, **kwargs):
        context = super(SectionsView, self).get_context_data(**kwargs)
        context['sections_list'] = Sections.objects.all().reverse()
        context['news'] = Post.objects.all().order_by('-date')[1:7]

        return context


class RegionalView(TemplateView):
    template_name = 'hududiy.html'
    model = RegionalCenters
    def get_context_data(self, **kwargs):
        context = super(RegionalView, self).get_context_data(**kwargs)
        context['regions_list'] = RegionalCenters.objects.all().reverse()
        return context

def bizhaqida(request):
    return render(request, 'Rahbaryat/bizhaqida.html')

def tuzilma(request):
    return render(request, 'Rahbaryat/tuzilma.html')

# New View
class NewsView(ListView):
    model = Post
    template_name = 'Matbuot/news.html'
    
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        news_list = Post.objects.all().order_by("-date")
        paginator = Paginator(news_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
       
        context['news_list'] = file_exams
        return context





# New Ditail View
class NewsDetailView(DetailView):
    model = Post
    template_name = 'oz/news_detail.html'
    context_object_name = 'news_detail'
    slug_url_kwarg = 'NewsSlug'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['news'] = Post.objects.all().order_by('-date')[1:7]

        return context
    
# Post Ditail View
class PostDetailView(DetailView):
    model = Post
    model = Poster
    template_name = 'oz/post_detail.html'
    context_object_name = 'post_detail'
    slug_url_kwarg = 'PostSlug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['news'] = Post.objects.all().order_by('-date')[1:7]

        return context

class ElonListView(ListView):
    model = Poster
    template_name = 'Matbuot/elon.html'
    context_object_name = 'elon_list'
    paginate_by = 10


# Media 
class MediaPhotoView(TemplateView):
    model = Media
    template_name = 'Matbuot/foto_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(MediaPhotoView, self).get_context_data(**kwargs)
        context['media_photo_list'] = Media.objects.filter(category_id=1)
        return context

class MediaVideoView(TemplateView):
    model = Media
    template_name = 'Matbuot/video_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(MediaVideoView, self).get_context_data(**kwargs)
        context['media_vedio_list'] = Media.objects.filter(category_id=2)
        return context



class PhotoDetailView(DetailView):
    model = Post
    model = Media
    template_name = 'Matbuot/detail_foto.html'
    context_object_name = 'photo_item'
    slug_url_kwarg = 'PhotoSlug'

    def get_context_data(self, **kwargs):
        context = super(PhotoDetailView, self).get_context_data(**kwargs)
        context['news'] = Post.objects.all().order_by('-date')[1:7]

        return context





# Contact
class Contact(TemplateView):
    model = Post
    template_name = 'oz/contact.html'


#Form action  
class ActinView(View):
    
    def post(self, request):
        post_request=request.POST
        actions = {
            'create_ad':create_ad,
        }
        messages.success(request, 'Xabaringiz yuborildi')
        actions[self.request.POST.get('action', None)](post_request)
        return redirect('contact')
# end Form action


# Gerb Madhiya Bayroq 

# class GerbView(TemplateView):
#     template_name = 'gerb.html'

# class BayroqView(TemplateView):
#     template_name = 'bayroq.html'

# class MadhiyaView(TemplateView):
#     template_name = 'madhiya.html'

# Gerb Madhiya Bayroq  end



class DocFile(DetailView):
    model = FaieldFiled
    model = Post
    model = CategoryDoc
    template_name = 'hujjatlar/hujjat_l.html'

    def get_context_data(self, **kwargs):
        context = super(DocFile, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # print(pk,"=========================")
        categor = FaieldFiled.objects.filter(categor_id=pk)
        # print(categor)
        context['bosh'] = CategoryDoc.objects.filter(id=pk)
        context['fiel_list'] = categor

        context['news'] = Post.objects.all().order_by('-date')[1:7]
        return context



# Search View
class SearchResulView(ListView):
    model = Post
    template_name = 'oz/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        objecy_list = Post.objects.filter(Q(title__icontains=query)|Q(Text__icontains=query))
                
    
        return objecy_list

#fayl
class FielView(ListView):
    template_name = 'fayl1.html'
    model = FaieldFiled
    context_object_name = 'fiel'

#fayl
class Fiel2View(ListView):
    template_name = 'fayl2.html'
    model = FaieldFiled
    context_object_name = 'fiel2'
    def get_context_data(self, **kwargs):
        context = super(Fiel2View, self).get_context_data(**kwargs)
        detail_post = FaieldFiled.objects.all().reverse()
        context['fiel2'] = detail_post
        return context




class Sahovat(TemplateView):
    template_name = 'oz/sahovat.html'

class PostsDetailView(DetailView):
    model = Poster
    template_name = 'detail_poster.html'
    context_object_name = 'poster_detail'

