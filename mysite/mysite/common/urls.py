from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
        #django.contrib.auth 사용할거라 중간에 auth~~씀, view안씀 > view를 안쓰니까 templates/.html을 바로 연결해야됨 :html안만들고 기본틀로 생성
        path('logout/' , auth_views.LogoutView.as_view(),name='logout'),
        #as_view() 공백인 이유는 로그인은  로그인 html로 넘어가야 하지만, 로그아웃은 그냥 홈화면으로 돌아가면 됨
        path('signup/' , views.signup, name='signup'),

]