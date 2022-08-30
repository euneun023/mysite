from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm   #forms.py의 UserForm 함수 사용 : 상속 //from,import 사용해서 연동

def signup(request):

     # 가입 버튼클릭했을때 첫 화면 띄우는건 GET ,  회원 객체 생성하는건 POST
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')   # .cleaned 는 입력한 값을 얻기위헤 사용하는 함수
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=raw_password)  # authenticate 와 login(r,u) 는 자동 로그인
            login(request,user)
            return redirect('index')
    else:   #GET
        form = UserForm()
    return render(request, 'common/signup.html',{'form': form})