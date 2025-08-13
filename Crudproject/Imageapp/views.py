from django.shortcuts import render,redirect
from.models import Imageupload 

# Create your views here.
def upload_image(request):
    if request.method=="POST" and request.FILES.get("image"):
        image_file =request.FILES["image"]
        Imageupload.objects.create(image=image_file)
        return redirect("upload_image")
    images =Imageupload.objects.all()
    return render(request,"index.html",{"images":images})
