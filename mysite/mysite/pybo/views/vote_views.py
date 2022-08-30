#추천기능

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Maincont

@login_required(login_url='common:login')
def vote_maincont(request, maincont_id):
    maincont=get_object_or_404(Maincont, pk=maincont_id)
    if request.user == maincont.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        maincont.voter.add(request.user)
    return redirect('pybo:detail',maincont_id=maincont.id)