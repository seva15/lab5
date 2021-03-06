from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {
        'orders': [
            {'title': 'О биткоинах', 'id': '1'},
            {'title': 'О турбинах', 'id': '2'},
            {'title': 'О ионах', 'id': '3'}
        ]
    }
    return render(request, 'index.html', data)


def orders(request, id):
    data = {
        'order': {
            'id': id
        }
    }

    return render(request, 'order.html', data)
