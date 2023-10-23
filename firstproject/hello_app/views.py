from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def print_hello(request):

        movie_data ={ 'movies' :[ {
            'title': 'aquaman',
            'year': 2020,
            'summary' : 'marvel movie in atlantic'
        },
        {
            'title': 'Ironman',
            'year': 2017,
            'summary' : 'marvel movie in steel rod'
        },{
            'title': 'Spiderman',
            'year': 2018,
            'summary' : 'marvel movie when a spider bites a man'
        },{
            'title': 'Caption Marvel',
            'year': 2016,
            'summary' : 'The man high in steroids '
        },{
            'title': '  Doctor Strange',
            'year': 2021,
            'summary' : 'The man which can alter the time'
        }]}
        return render(request,'hello.html',movie_data)