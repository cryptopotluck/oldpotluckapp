from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import post
from ratelimit.decorators import ratelimit


# Create your views here.
@login_required
def potluck(request):
    posts = post.objects.order_by('-votes_total')
    return render(request, 'upvote/potluck.html', {'posts': posts})


@login_required
def bottweak(request):
    posts = post.objects.filter(sub_feed='🤖 Bot Tweaking').order_by('-votes_total')
    return render(request, 'upvote/bottweaking.html', {'posts': posts})


@login_required
def politics(request):
    posts = post.objects.filter(sub_feed='📰 Political News').order_by('-votes_total')
    return render(request, 'upvote/politicalnews.html', {'posts': posts})


@login_required
def newpotlucknews(request):
    return render(request, 'upvote/newpotlucknews.html', {'title': 'New'})


@login_required
def toppotlucknews(request):
    return render(request, 'upvote/toppotlucknews.html', {'title': 'Top'})


@login_required
def bullmarkets(request):
    posts = post.objects.filter(sub_feed='🐂 Bull News').order_by('-votes_total')
    return render(request, 'upvote/bullmarkets.html', {'posts': posts})


@login_required
def bearmarkets(request):
    posts = post.objects.filter(sub_feed='🐻 Bear News').order_by('-votes_total')
    return render(request, 'upvote/bearmarkets.html', {'posts': posts})


@login_required
def shitcoinNnews(request):
    posts = post.objects.filter(sub_feed='💩 Shitcoins & News').order_by('-votes_total')
    return render(request, 'upvote/shitcoinNnews.html', {'posts': posts})


@login_required
def userpost(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['sub_feed']:
            Post = post()
            Post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Post.url = request.POST['url']
            else:
                Post.url = 'http://' + request.POST['url']
            Post.sub_feed = request.POST['sub_feed']
            Post.pub_date = timezone.datetime.now()
            Post.author = request.user
            Post.Main_Pair = request.POST['Main_Pair'].upper()
            Post.Altcoin = request.POST['Altcoin'].upper()
            Post.body = request.POST['body']
            Post.save()

            return redirect('Potluck:Home')
        else:
            return render(request, 'upvote/userpost.html', {'error': 'Error: You must include a Title & Sub Feed '})

    else:
        return render(request, 'upvote/userpost.html', {'title': 'NewPost'})



def upvote(request, pk):
    x = 0
    if x <= 0:
        if request.method == 'POST':
            Post = post.objects.get(pk=pk)
            Post.votes_total += 1
            x += 1
            Post.save()
            return redirect('Potluck:Home')
    else:
        if request.method == 'POST':
            Post = post.objects.get(pk=pk)
            Post.votes_total += 0
            x += 1
            Post.save()
            return redirect('Potluck:Home')


def downvote(request, pk):
    if request.method == 'POST':
        Post = post.objects.get(pk=pk)
        Post.votes_total -= 1
        Post.save()
        return redirect('Potluck:Home')

    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import authentication, permissions
    from django.contrib.auth.models import User

    class UpvoteDownvote(APIView):
        """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """
        authentication_classes = (authentication.SessionAuthentication,)
        permission_classes = (permissions.IsUser,)

        def get(self, request, format=None):
            """
            Return a list of all users.
            """
            usernames = [user.username for user in User.objects.all()]
            return Response(usernames)
