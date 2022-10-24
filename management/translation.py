from django.db.models import fields
from modeltranslation.translator import register, TranslationOptions
from .models import Managment, Poster, Sections, RegionalCenters, Post, LiveMessage,FaieldFiled, CategoryDoc, Information, MenuCategory
# from .admin import PostAdminForm


@register(FaieldFiled)
class FaieldFiledTranslationOptions(TranslationOptions):
    fields = ('name', 'categor')

@register(CategoryDoc)
class CategoryDocTranslationOptions(TranslationOptions):
    fields = ('name')


class ManagmentTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'biography', 'functions_tasks')

@register(Managment)
class ManagmentTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'biography', 'functions_tasks')


@register(Sections)
class SectionsTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'biography', 'functions_tasks')


@register(RegionalCenters)
class RegionalCentersTranslationOptions(TranslationOptions):
    fields = ('name', 'leader', 'title')


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title','Text')
    

@register(LiveMessage)
class LiveMessageTranslationOptions(TranslationOptions):
    fields = ('name', 'message', 'message_long')

@register(Poster)
class PosterMessgeTranslationOptions(TranslationOptions):
    fields = ('title', 'Text')


# @register(Information)
# class PosterMessgeTranslationOptions(TranslationOptions):
#     fields = ('title', 'Text')

# @register(MenuCategory)
# class PosterMessgeTranslationOptions(TranslationOptions):
#     fields = ('title', 'Text')