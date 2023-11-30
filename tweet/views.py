from django.shortcuts import render, redirect
from .models import Tweet
from .forms import AddTweetForm, AddTweetModelForm


# Create your views here.

def listtweet(request):
    all_tweets = Tweet.objects.all()
    context = {
        'all_tweets': all_tweets,
    }
    return render(request, 'listweet.html', context)


def addtweet(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        message = request.POST['message']
        tweet = Tweet(nickname=nickname, message=message)
        tweet.save()
        return redirect('listtweet')
    else:
        return render(request, 'addtweet.html')


def addtweetbyform(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            message = form.cleaned_data['message_input']
            Tweet.objects.create(nickname=nickname, message=message)
            return redirect('addtweetbyform')
        else:
            return render(request, 'addtweetbyform.html', context={'form': form})


    else:
        form = AddTweetForm()
        context = {
            'form': form
        }
        return render(request, 'addtweetbyform.html', context)


def addtweetmodelform(request):
    if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            message = form.cleaned_data['message']
            Tweet.objects.create(nickname=nickname, message=message)
            return redirect('addtweetbyform')
        else:
            return render(request, 'addtweetmodelform.html', context={'form': form})

    else:
        form = AddTweetModelForm()
        context = {
            'form': form
        }
        return render(request, 'addtweetmodelform.html', context)
