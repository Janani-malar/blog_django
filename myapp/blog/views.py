from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse  #for using path - (name=) instead of (path "----" )
import logging
from .models import Post,Category,AboutUs
from  django.core.paginator import Paginator
from .forms import ContactForm


#static demo data

# posts=[
#     {'id':1,'title':'post 1','content':'content of post 1'},
#     {'id':2,'title':'post 2','content':'content of post 2'},
#     {'id':3,'title':'post 3','content':'content of post 3'},
#     {'id':4,'title':'post 4','content':'content of post 4'},
# ]

def index(request):
    blog_title= "Lastest posts"

    #getting data from post model
    all_posts=Post.objects.all() 

    #paginate
    paginator=Paginator(all_posts,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,"index.html",{'blog_title':blog_title, 'page_obj':page_obj})

def detail(request, slug):

    #static data..
    # post=next((item for item in posts if item['id'] == post_id),None)

    try:
        post = Post.objects.get(slug=slug)  # Fetch the current post
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist!")
    
    # logger=logging.getLogger("TESTING")
    # logger.debug(f"post variable is {post} ")   
    return render(request, "detail.html", {'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"Post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "Your email has been sent!"
            return render(request, "contact.html", {'form': form, 'success_message': success_message})
        else:
            logger.debug("Form validation failure")
            return render(request, "contact.html", {'form': form, 'name': name, 'email': email, 'message': message})
    
    # Render form on GET request
    return render(request, "contact.html")

def about(request):
    about_content = AboutUs.objects.first().Content
    return render(request,'about.html',{'about_content':about_content})