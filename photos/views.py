from django.shortcuts import render

def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'photos/view_photo.html')

def addPhoto(request):
    return render(request, 'photos/add_photo.html')
