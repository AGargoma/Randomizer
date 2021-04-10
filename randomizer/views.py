import random

from django.shortcuts import render

# Create your views here.

def randomize(request):
    try:
        start, end, count = int(request.GET['start']), int(request.GET['end']),\
                            int(request.GET['count'])
        output = random.choices(range(start, end), k=count)
        return render(request,'randomizer/index.html', {
            'range': input_range,
            'output': output,
            'start': start,
            'end': end,
            'count': count,
        })
    except:
        return render(request,'randomizer/index.html', {
            'range': [],
        })
