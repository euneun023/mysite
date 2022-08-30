from django import forms
from pybo.models import Maincont , Comment

class MaincontForm(forms.ModelForm):
    class Meta:
        model = Maincont
        fields = ['subject','word','sentence'] #사이트url, 단어, 문장을 폼의 필드로 가짐
        #subject >제목 / word >단어 / sentence >문장   : 한글로 바꾸기
        labels = {
            'subject':'제목',
            'word':'단어',
            'sentence':'문장',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content'] #댓글작성하는 폼
        labels={
            'content':'댓글내용',
        }

