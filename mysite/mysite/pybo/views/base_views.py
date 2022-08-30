#기본 ( index창 , detail창)
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.db.models import Q, Count   #OR 조건으로 데이터를 검색하는 장고의 함수

from ..models import Maincont  #점 두개(..)인 이유는 pybo/views/ 두번에 걸쳐서 있음
#기존의 view.py에서 가져옴

def index(request):     #창열어주기

    page = request.GET.get('page', '1')  # 1페이지을 기본으로 출력 > localhost:8000/pybo/?page1
    kw = request.GET.get('kw','')        # localhost:8000/?kw=검색어&page=3
    sr = request.GET.get('sr','recent')  #정렬기준

    if sr =='recommend':  # 추천순
        maincont_list = Maincont.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')

    elif sr =='recent':  # 최신순
        maincont_list = Maincont.objects.order_by('-create_date')


    if kw:                                                      #검색하는 함수
        maincont_list=maincont_list.filter(
            Q(subject__icontains=kw)|     #url로 검색
            Q(word__icontains=kw)|         #단어로 검색
            Q(sentence__icontains=kw)|    #문장으로 검색
            Q(author__username__icontains=kw)       #글쓴이로 검색

        ).distinct()



    #페이징 처리
    paginator = Paginator(maincont_list, 10)    #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)             #페이지 가져오기

    context = {'maincont_list': page_obj, 'page':page, 'kw':kw, 'sr':sr}    #kw(검색어)와 page도 반환
    return render(request, 'pybo/maincont_list.html',context)  #render함수 이용해서 html에 context내용 넣음
    #결과물 : 페이지 1에서 10개의 저장된데이터만 화면에 나타난다.



def detail(request, maincont_id):    #사이트 클릭했을때(id로) 다음창으로 넘어가도록 구현

    maincont=get_object_or_404(Maincont, pk=maincont_id)
    context={'maincont':maincont}

    return render(request,'pybo/maincont_detail.html',context)


