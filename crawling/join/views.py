from django.shortcuts import render
from .forms import JoinForm,ChoiceForm #forms.py 의 JoinForm,ChoiceForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import join,choice      #DB select를 위해 models를 가져옴
from bs4 import BeautifulSoup
import requests
from django.contrib import messages



def index(request):
    if request.session.get('member_id',False):
        return render(request, 'join/main.html')
    else:
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
    if request.session.get('member_id', False):
        return render(request, 'join/main.html')
    else:
        return render(request, 'join/login.html')

def login_success(request):
     join_list = join.objects.filter(id=request.POST['id'], password=request.POST['password']).values()
     print("리스트", join_list)
     join_id = join_list.values_list('id',flat =True)
     join_id = list(join_id)
     #join_id = join.objects.filter(id=request.POST['id'], password=request.POST['password'])
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

def crawling(request):
    param = request.GET.get('kind')
    print(param)
    if param == 'concert':
        url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv'
    elif param == 'musical':
        url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Mus'

    if request.session.get('member_id',False):
        response= requests.get(url)
        html = response.text
        soup = BeautifulSoup(html,"html.parser")

        content = soup.find("div",{"class":"stit"})
        content_info = content.find_all("td",{"class":"RKthumb"})

        list = []
        data = dict()
        for alt in content_info:

            content_img = alt.find('img')
            content_alt  = content_img['alt']

            list.append(content_alt)

            #print(content_alt)
            #print(content_info)

        print(list)

        data['title']= list        #list에 담은 데이터를 key, value형식의 dictionary에 다시 담기
        print(data['title'][1])

       # return render(request, 'join/crawling.html',{ 'content' : list})
        return render(request, 'join/crawling.html', {'content': data})
    else:
        return HttpResponseRedirect("/join/login/")

def my_crawling(request):

    #choice_list = choice.objects.values()
    choice_list = choice.objects.filter(id = request.session['member_id']).values()
    print(choice_list)
    context = {
        'content' : choice_list
    }
    print(context)
    return render(request, 'join/my_crawling.html',context)

def my_crawling_success(request):

    data = {}
    data['id'] = request.session.get('member_id',False)
    data['etc1'] = request.POST['etc1']
    data['etc2'] = request.POST['etc2']

    if request.method == "POST":
        form = ChoiceForm(data)
        print(form)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.save()  # 디비에 저장
            return HttpResponse('<h1>Register Success</h1>')

    elif request.method == "GET":
        return HttpResponse('<h1>GET</h1>')
    else:
        return HttpResponse('<h1>NOTHING</h1>')

def update(request):
    choice.objects.filter(id=request.session['member_id']).update(etc1=request.POST.get('etc1'), etc2=request.POST.get('etc2'))
    messages.success(request, "Update Success")

    return HttpResponseRedirect("/join/my_crawling/")
    #return render(request, 'join/my_crawling.html')