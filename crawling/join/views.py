from django.shortcuts import render
from .forms import JoinForm  #forms.py 의 JoinForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



def index(request):
    return render(request, 'join/index.html')

def main(request):
    return render(request, 'join/main.html')

@csrf_exempt
def signup(request):

    data = request.POST.get('email')
    print(data)
    if request.method == "POST":
        form = JoinForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # 디비에 저장
            return HttpResponse('<h1>Join Success</h1>');

    elif request.method == "GET":
        return HttpResponse('<h1>GET</h1>');
    else:
        return HttpResponse('<h1>NOTHING</h1>');