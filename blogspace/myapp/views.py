from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 

# Create your views here.
def home (request):
    if request.method == 'GET':
        output = request.GET.get('output')
    return render (request, 'index.html', {'output': output})

def signup (request):
    # data = {}
    finalans = 0
    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            # data = {
            #     'n1': n1,
            #     'n2': n2,
            #     'output': n1+n2
            # }
            finalans = n1 + n2
            url = "/app/home/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render (request, 'signup.html', {'output':finalans})