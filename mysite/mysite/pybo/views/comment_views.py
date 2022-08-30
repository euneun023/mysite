#댓글 관리 (생성 , 수정 , 삭제)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404 , redirect , resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Maincont , Comment


@login_required(login_url='common:login')
def comment_create_maincont(request , maincont_id):                             #<댓글추가>
    maincont=get_object_or_404(Maincont, pk=maincont_id)  #게시판 글 번호
    if request.method =="POST":
        form=CommentForm(request.POST) #comment form을 가져옴
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author=request.user
            comment.create_date=timezone.now()
            comment.maincont=maincont
            comment.save()
            #댓글 앵커 return / maincont_id=comment.maincont.id 그러나 maincont.id 해도 상관 없지않나..?
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', maincont_id=comment.maincont.id), comment.id))
            #return redirect('pybo:detail',maincont_id=maincont.id)  기존 리턴 > 댓글앵커 전
    else:
        form=CommentForm()
    context={'form':form}
    return render(request, 'pybo/comment_form.html',context)


@login_required(login_url='common:login')
def comment_modify_maincont(request, comment_id):                           #<댓글수정>
    comment=get_object_or_404(Comment,pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정 권한이 없습니다.')
        return redirect('pybo:detail',maincont_id=comment.maincont.id)  #comment의 maincont의 id > comment의 model 확인, 이댓글이 달린 게시글의 아이디로  간다.
                                                                        #comment의 id는 댓글번호(몇번째인지) _ maincont의 id는 게시글이 몇번째 인지
    if request.method == "POST":   #POST : 댓글업데이트
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.modify_date=timezone.now()
            comment.save()
        # 댓글 앵커 return / maincont_id=comment.maincont.id 얘는 model.py에서 가져오는 거라 comment.maincont.id를 꼭해야됨 , 그냥 maincont.id 인식안됨
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', maincont_id=comment.maincont.id), comment.id))
           # return redirect('pybo:detail',maincont_id=comment.maincont.id) 기존 리턴 > 앵커 없음

    else:   #GET : 댓글조회
       form=CommentForm(instance=comment)  #instance=comment:이전에 있던 내용 가져옴

    context={'form':form}
    return render(request,'pybo/comment_form.html',context)



@login_required(login_url='common:login')
def comment_delete_maincont(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)                           #<댓글삭제>
    if request.user != comment.author:
        messages.error(request,'댓글삭제 권한이 없습니다.')
        return redirect('pybo:detail',maincont_id=comment.maincont.id)
    else:
        comment.delete()
    return redirect('pybo:detail',maincont_id=comment.maincont.id)
