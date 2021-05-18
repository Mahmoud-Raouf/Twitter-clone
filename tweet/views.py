from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render ,redirect
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.models import User
from django.views.generic import CreateView , ListView , View , UpdateView , DetailView ,DeleteView
from .mixins import FormUserNeededMixin , UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomeView(View):
    model = Tweet
    form_class = TweetForm
    success_url = reverse_lazy("tweets:homeview")
    
    def get(self, request, *args, **kwargs):
        view = TweetList.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Create_Tweet.as_view()
        return view(request, *args, **kwargs)

#Here i create a mixin file and create a valid_form in "FormUserNeededMixin" class and import it here
class Create_Tweet(FormUserNeededMixin ,CreateView):
    model = Tweet
    form_class = TweetForm
    success_url = reverse_lazy("tweets:homeview")
    
class TweetList(ListView):
    model = Tweet
    template_name = 'tweet/home_page.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(content__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list



class UpdateTweet(LoginRequiredMixin, UserOwnerMixin ,DetailView ,UpdateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweet/updatetweet.html'
    success_url = reverse_lazy("tweets:homeview")
    

class DeleteTweet(LoginRequiredMixin,DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweets:homeview")


# def create_tweet(request):
#     if request.method == "POST":
#         form = TweetForm(data = request.POST)
#         if form.is_valid():
#             new_tweet = form.save(commit=False)
#             new_tweet.user = request.user
#             new_tweet.save()
#             print(new_tweet)
#         return redirect('home/')

#     context={ 
#         'form' : form
#     }
#     return render(request , 'tweet/home_page.html', context)


# def tweet_detail(request , id):
#     query = Tweet.objects.get(id=id)
#     context={ 
#         'query' : query
#     }
#     return render(request , 'tweet/tweet_detail.html', context)

# def tweet_list(request):
#     query = Tweet.objects.all()

#     context={ 
        
#         'query' : query
#     }
#     return render(request , 'tweet/home_page.html', context)

# def tweet_home(request):
#     return render(request , 'tweet/home.html', {})