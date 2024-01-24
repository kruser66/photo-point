import requests
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from exchange.models import Exchange


def fetch_current_excange_usd(currency: str = 'RUB'):

    # запрашиваем текущий курс
    response = requests.get('https://open.er-api.com/v6/latest/USD')
    response.raise_for_status()

    exchange = response.json()

    Exchange.objects.create(
        rate=exchange['rates'][currency],
        currency=currency,
        timestamp=datetime.now()
    )

    return exchange['rates'][currency]


def index(request):

    return HttpResponse('Доступный endpoint: /exchange/get_current_usd')


def get_current_usd(request):

    rate = fetch_current_excange_usd('RUB')
    current_rate = {
        'rate': rate,
        'timestamp': datetime.now()
    }

    latest_exchanges = Exchange.objects.order_by('-timestamp')[:10]

    latest_rate = [
        {
            'rate': exchange.rate,
            'timestamp': exchange.timestamp,
        } for exchange in latest_exchanges
    ]

    current_answer = {
        'current_rate': current_rate,
        'latest_rate': latest_rate,
    }

    return JsonResponse(current_answer, safe=False)
