from django.urls import path
from .views import base_views, maincont_views, comment_views, vote_views  #기존에는 from .import views

app_name = 'pybo'  #다른 프로젝트 추가될수도 있으니 앱 네임 지정

urlpatterns = [

    # html 작성 > urls에 먼저 작성 > views에 함수 작성
    # 'name' 을 넣어서 사이트주소 특정지음

    #base_views.py
    path('',base_views.index, name='index'), #views.py로 이동 / index함수이동
    path('<int:maincont_id>/',base_views.detail, name='detail'), #각 사이트들을 눌렀을때 id를 인식함 > views.py로이동 / detail함수이동

    #maincont_views.py
    path('maincont/create/',maincont_views.maincont_create, name='maincont_create'), #추가저장 하는거 path만들어주기
    path('maincont/modify/<int:maincont_id>/' , maincont_views.maincont_modify , name='maincont_modify'), #글 수정하는창
    path('maincont/delete/<int:maincont_id>/', maincont_views.maincont_delete, name='maincont_delete'), #글 삭제

    #comment_views.py
    path('comment/create/maincont/<int:maincont_id>/',comment_views.comment_create_maincont, name='comment_create_maincont'), #댓글생성
    path('comment/modify/maincont/<int:comment_id>/',comment_views.comment_modify_maincont, name='comment_modify_maincont'), #댓글수정
    path('comment/delete/maincont/<int:comment_id>/',comment_views.comment_delete_maincont, name='comment_delete_maincont'), #댓글삭제

    #vote_views.py
    path('vote/maincont/<int:maincont_id>/',vote_views.vote_maincont, name='vote_maincont'),  #추천기능

]


