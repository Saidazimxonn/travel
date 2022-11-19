from django.contrib import admin
from django.contrib.admin.decorators import register
from modeltranslation.admin import TranslationAdmin
from django import forms
from .models import (
    Managment, 
    Sections, 
    RegionalCenters, 
    Post,LiveMessage, 
    Poster, 
    FaieldFiled, 
    CategoryDoc, 
    Information, 
    MenuCategory,
    Media,
    Media_type
    )


from ckeditor_uploader.widgets import CKEditorUploadingWidget 

 
class SectionsAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Sections
        fields = '__all__'

class TadbirAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Media
        fields = '__all__'

# Register your models here.

# Register your models here.
@admin.register(FaieldFiled)
class FaieldFiledAdmin(TranslationAdmin):
    list_display = ('name','categor')
    prepopulated_fields = {
        'slug': ['name']
    }

# Register your models here.
@admin.register(CategoryDoc)
class CategoryDocAdmin(TranslationAdmin):
    list_display = ('name',)
    prepopulated_fields = {
        'slug': ['name']
    }
    

@admin.register(Managment)
class ManagmentAdmin(TranslationAdmin):

    list_display = ('name', 'title', 'biography', 'functions_tasks')
    prepopulated_fields = {
        'slug': ['name']
    }


@admin.register(Sections)
class SectionsAdmin(TranslationAdmin):
    list_display = ('name', 'title', 'biography', 'functions_tasks')
    prepopulated_fields = {
        'slug': ['name']
    }


@admin.register(RegionalCenters)
class RegionalCentersAdmin(TranslationAdmin):
    list_display = ('name', 'leader', 'title')


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title','date')
    list_display_links = ('title',)
    prepopulated_fields = {
        'slug': ['title']
    }
    list_per_page = 15
    search_fields = ['title','Text']

@admin.register(LiveMessage)
class LiveMessageAdmin(TranslationAdmin):
    list_display = ('name', 'message', 'message_long')

@admin.register(Poster)
class PosterMessageAdmin(TranslationAdmin):
    list_display = ('title', 'title')
       
    list_per_page = 15
    prepopulated_fields = {
        'slug': ['title']
    }

# @admin.register(Information)
# class InformationAdmin(TranslationAdmin):
#     list_display = ('title', 'body')

# @admin.register(MenuCategory)
# class MenuCategoryAdmin(TranslationAdmin):
#     list_display = ('name')

# admin.site.register(Managment, ManagmentAdmin)
# admin.site.register(Sections, SectionsAdmin)
# admin.site.register(RegionalCenters, register)
# admin.site.register(Information)
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')
    form  = SectionsAdminForm

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('category', 'nomi')
    prepopulated_fields = {
        'slug': ['nomi']
    }
    form  = TadbirAdminForm



admin.site.register(MenuCategory)
# admin.site.register(Media)
admin.site.register(Media_type)

