from django.shortcuts import render
from .models import Content
# Create your views here.
def index(request):
    contents = Content.objects.all()

    search_title=request.GET.get('search_title','')
    print(search_title)

    if search_title !='' or search_title is not None:
        contents = contents.filter(title__icontains=search_title) 

    context ={'contents':contents}
    return render(request,'search/index.html',context)