from django.shortcuts import render
from .models import BlogFrame
from django.shortcuts import render, get_object_or_404

def main(request):
    blogs = BlogFrame.objects
    return render(request, 'main.html',{'blogs':blogs})



def detail(request, blog_id):
    blog_detail = get_object_or_404(BlogFrame, pk=blog_id)
    return render(request, '/detail.html', {'blogdetail': blog_detail})
# Create your views here.
