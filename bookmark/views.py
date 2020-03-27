from django.shortcuts import render
from bookmark.models import Bookmark

# Create your views here.
def home(request):
    urlList=Bookmark.objects.order_by('title')
    urlCount=Bookmark.objects.all().count()
    
    return render(request, "bookmark/list.html" , {'urlList':urlList, 'urlCount': urlCount})

def detail(request):
    addr=request.GET['url']
    dto=Bookmark.objects.get(url=addr)
    
    return render(request, "bookmark/detail.html",{'dto':dto})



