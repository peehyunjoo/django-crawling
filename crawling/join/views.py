from django.shortcuts import render
from .forms import JoinForm  #forms.py 의 JoinForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import join      #DB select를 위해 models를 가져옴



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
            return HttpResponse('<h1>Join Success</h1>')

    elif request.method == "GET":
        return HttpResponse('<h1>GET</h1>')
    else:
        return HttpResponse('<h1>NOTHING</h1>')

def login(request):
    return render(request, 'join/login.html')

def login_success(request):
     join_list = join.objects.filter(id=request.POST['id'], password=request.POST['password']).values()
     join_id = join_list.values_list('id',flat =True)
     join_id = list(join_id)
     print(join_id)

     if join_list.exists():

         request.session['member_id'] = join_id
         print("LOGIN:" ,request.session['member_id'])
         return render(request, 'join/main.html')
     else:
         return render(request, 'join/login.html')

def logout(request):
    #print(request.session['member_id'])
    try:
        del request.session['member_id']
        return HttpResponseRedirect("/join/main/")

    except KeyError:
        print("LOGOUT: ", request.session['member_id'])
        pass

