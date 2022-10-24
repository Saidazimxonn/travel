from .models import (
    CategoryDoc, 
    Information,
    MenuCategory,
    Media_type,
    Media
)

def extras(request):
    categories = CategoryDoc.objects.all().order_by('-date')
    menyu = MenuCategory.objects.all()
    shaharhokm = Information.objects.filter(category_id=1)
    shaharhaqida = Information.objects.filter(category_id=2)
    mahallykengash = Information.objects.filter(category_id=3)

    mediaPhoto = Media_type.objects.filter(id=1)
    mediaVideo = Media_type.objects.filter(id=2)


    return {
            'categor':categories,
            'menu':menyu,
            'shaharhokm_elemnts':shaharhokm,
            'shaharhaqida_elemnts':shaharhaqida,
            'mahallykengash_elemnts':mahallykengash,

            'Photo':mediaPhoto,
            'Video':mediaVideo,
        }