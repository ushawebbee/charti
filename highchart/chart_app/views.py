from django.shortcuts import render
from .models import Store
from  django.db.models import Avg
import json

# Create your views here.
def display(request):
    context=Store.objects.values('category').annotate(avg_rating=Avg('rating'))
    categories = list()
    rating_data = list()


    for entry in context:
        categories.append('%s ' % entry['category'])
        rating_data.append(entry['avg_rating'])
    rating_series = {
        'name': 'Avg-Rating',
        'data': rating_data,
        'color': 'green',

    }
    chart = {

        'chart': {'type': 'column'},
        'title': {'text': 'Google Play Store Data'},
        'xAxis': {'categories': categories},
        'series': [rating_series]
    }

    dump = json.dumps(chart)

    return render(request,'chart_app/display.html', {'chart': dump})
