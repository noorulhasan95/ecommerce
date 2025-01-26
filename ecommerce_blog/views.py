from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.urls import reverse
import logging

from .models import Post, Category, Subcategory

# Create your views here.

# def index(request):
#     return HttpResponse('hrllow')
def index(request):
    # logger = logging.getLogger("TESTING")
    # logger.debug(f"post variable is ")

        #static data
    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    # log
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post_id}')

    all_posts = Post.objects.all()

    all_category = Category.objects.all()
    all_subcategory = Subcategory.objects.all()

    # all_subcategory = Subcategory.objects.filter(category_id = "1").values()

    # all_category = Category.objects.all()
    # all_subcategory = {
    #     category: Subcategory.objects.filter(category=category)
    #     for category in all_category
    # }

    context = {
                'all_posts':all_posts,'all_category':all_category,'all_subcategory':all_subcategory,
    }


            
    return render(request,'blog/home-standard.html',context)


def index2(request,post_id):

    logger = logging.getLogger("TESTING")
    logger.debug(f'post variable is {post_id}')
            
    return render(request,'blog/home-standard.html')

def register(request):

    logger = logging.getLogger("TESTING")
    logger.debug(f'post variable is')
            
    return render(request,'blog/register.html')
