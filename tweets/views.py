from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
import random

from .models import Tweet
from .forms import TweetForm

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>hello world!</h1>")
    return render(request, "pages/home.html", context = {})

def tweet_create_view(request, *args, **kwargs):
    # initialize data as a method or none
    print('post data is', request.POST)
    next_url = request.POST.get("next") or None
    print("next_url", next_url)
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # valid => save
        # do other form related logic
        obj.save()
        form = TweetForm()
        # if form is not valid component/forms.html call
    return render(request, 'components/form.html', context = {"form": form})

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift or Java/ IOS/ Android
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes" : random.randint(0, 123)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift or Java/ IOS/ Android
    return json data
    """
    data = {
        "id": tweet_id,
        #"image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status = status) # json.dumps content_type = 'application/json'