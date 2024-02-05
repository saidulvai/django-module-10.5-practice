from django.shortcuts import render
import datetime
def home(request):
    d = {
        'lst' : ['python', 'is', 'fun'],
         
         'date' : datetime.datetime.now(),
         'add' : '5',
         'capfirst' : 'django',
         'cut' : "Python is Fun",
         'dic' : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
],
        'firstFilter':  ['Apple', 'Mango', 'Orange'],
        'lengthFilter' : ['Banana', 'Mango', 'Orange'],
        'linenumbersFilter' : 'cat',

        'time' : '10:30:00.000123+02:00',
         }
    return render(request, 'home.html', d)
