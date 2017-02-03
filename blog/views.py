from django.shortcuts import render

# Create your views here.
def post_list(request):
    return renter(request, 'blog/post_list.html', {})
