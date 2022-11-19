from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

# Managment create
class Managment(models.Model):
    name = models.CharField(verbose_name="F.I.SH", max_length=250)
    title = models.CharField(verbose_name="Lavozimi", max_length=250)
    slug = models.SlugField(max_length=512, unique=True)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=100)
    acceptance_dates = models.CharField(verbose_name="Qabul kunlari", max_length=250)
    biography = RichTextField(verbose_name="Tarjimai hol", null=True, blank=True)
    functions_tasks = RichTextField(verbose_name="Funksiya va vazifalar", null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Rahbaryat  AZOSI"
        verbose_name_plural="Rahbaryat  AZOLARI"

# Sections create  
class Sections(models.Model):
    name = models.CharField(verbose_name="F.I.SH", max_length=250)
    title = models.CharField(verbose_name="Lavozimi", max_length=250)
    slug = models.SlugField(max_length=512, unique=True)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    email = models.CharField(verbose_name="Email", max_length=100)
    acceptance_dates = models.CharField(verbose_name="Qabul kunlari", max_length=250)
    biography = RichTextField(verbose_name="Tarjimai hol", null=True, blank=True)
    functions_tasks = RichTextField(verbose_name="Funksiya va vazifalar", null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()


    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Rahbaryat  XODIM"
        verbose_name_plural="Rahbaryat XODIMLAR"

# Regionalny Centers Create
class RegionalCenters(models.Model):
    name = models.CharField(verbose_name="Hududiy boshqarma nomi", max_length=250)
    leader = models.CharField(verbose_name="F.I.SH BOshqarma boshlig'i", max_length=250)
    title = models.CharField(verbose_name="Manzili", max_length=250)
    phone = models.CharField(verbose_name="Phone", max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.name
    class Meta:
        verbose_name="Hududiy  BO'LIM"
        verbose_name_plural="Hududiy  BO'LIMLAR"

# Post Create    
class Post(models.Model):
    user = models.ForeignKey(User,verbose_name='Muallif', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Qisqa matn", max_length=300)
    slug = models.SlugField(max_length=512, unique=True)
    Text = RichTextField(verbose_name="Text", null=True, blank=True)
    image = models.ImageField()
    date  = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Matbuot  YANGILIK"
        verbose_name_plural="Matbuot  YANGILIKLAR"


# LIve Messages
class LiveMessage(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    phone = models.CharField(verbose_name="Phone", max_length=100)
    message = models.CharField(verbose_name="Message", max_length=100)
    message_long = models.TextField(verbose_name="Matin ")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox,)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'

#Poster Create new ad

class Poster(models.Model):
    user = models.ForeignKey(User,verbose_name='Muallif', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Qisqa matn", max_length=300)
    slug = models.SlugField(max_length=512, unique=True)
    Text = RichTextField(verbose_name="Text", null=True, blank=True)
    image = models.ImageField()
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Matbuot  E'LONLAR"
        verbose_name_plural="Matbuot  E'LONLAR"




#Category fail

class CategoryDoc(models.Model):
    name = models.CharField('Category name',max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=512, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Xujjat  TURI"
        verbose_name_plural="Xujjatlar  TURLARI"

#Faield Filed Doc
class FaieldFiled(models.Model):
    name = models.CharField("Doc name",max_length=250)
    slug = models.SlugField(max_length=512, unique=True)
    categor = models.ForeignKey(CategoryDoc, on_delete=models.CASCADE)
    fiel_name = models.FileField("Fiels",upload_to='documents/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Xujjat BAZASI"
        verbose_name_plural="Xujjatlar BAZASI"


class MenuCategory(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Menyu  KATEGORYA"
        verbose_name_plural="Menyu  KATEGORYALAR"

class Information(models.Model):
    category = models.ForeignKey(MenuCategory, verbose_name='Kategoriya', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = RichTextField(verbose_name="Text", null=True, blank=True)
    fiel_name = models.FileField("Files",upload_to='documents/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name="Menyu BO'LIM"
        verbose_name_plural="Menyu BO'LIMLAR"



class Media_type(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name="Media TURI"
        verbose_name_plural="Media TURLARI"

class Media(models.Model):
    category = models.ForeignKey(Media_type, verbose_name='Media nomi', on_delete=models.CASCADE)
    nomi = models.CharField(max_length=250)
    slug = models.SlugField(max_length=512, unique=True)
    body = RichTextField(verbose_name="Text", null=True, blank=True)
    fiel_name = models.FileField("Media yuklash shart",upload_to='documents/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomi} - {self.category}"


























    class Meta:
        verbose_name="Media"
        verbose_name_plural="Medialar" 