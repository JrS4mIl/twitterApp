from django.shortcuts import render,redirect
from .models import Tweet
from .forms import AddTweetForm


# Create your views here.

def listtweet(request):
    all_tweets = Tweet.objects.all()
    context = {
        'all_tweets': all_tweets,
    }
    return render(request, 'listweet.html', context)


def addtweet(request):
    if request.method == 'POST':
        nickname=request.POST['nickname']
        message=request.POST['message']
        tweet=Tweet(nickname=nickname,message=message)
        tweet.save()
        return redirect('listtweet')
    else:
        return render(request, 'addtweet.html')
def addtweetbyform(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('addtweetbyform')
    else:
        form = AddTweetForm()
        context={
            'form':form
        }
        return render(request,'addtweetbyform.html',context)