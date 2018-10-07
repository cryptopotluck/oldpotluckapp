from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from upvote.models import post



# Create your views here.
@login_required
def news(request):
    import json
    import requests

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})

@login_required
def prices(request):
    if request.method == 'POST':
        import json
        import requests
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        ##picture_request = requests.get("https://min-api.cryptocompare.com/data/all/coinlist")
        ##picture = json.loads(picture_request.content)

        posts = post.objects.filter(Altcoin=quote).order_by('-pub_date')
        mainp = post.objects.filter(Main_Pair=quote).order_by('-votes_total')

        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto,  'posts': posts, 'mainp':mainp})




    else:
        notfound = "sup"
        return render(request, 'prices.html', {'notfound': notfound})


def get_data(request, *args, **kwards):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "sales": 100,
            "customers": 10,
        }

        return Response(data)

@login_required
def fourcharts(request):
    return render(request, '4charts.html', {'title': 'fourcharts'})