from django.shortcuts import render, redirect
from .models import Category, Photo


# Code Credit: Dennis Ivy (Link in README)
def gallery(request):
    """
    Display various pictures

    **Context**

    ``categories``
        Various categories based on picture topic
    ``photos``
        Category attaches and created based on 
        photo uploaded
    """
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    """
    Display one photo
    """
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/view_photo.html', {'photo': photo})


def addPhoto(request):
    """
    Form for authenticated users to add photos
    """
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image,
        )

        return redirect('gallery')    
    context = {'categories': categories}

    return render(request, 'photos/add_photo.html', context)
