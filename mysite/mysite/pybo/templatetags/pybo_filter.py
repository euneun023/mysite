import markdown                             #마크다운 필터 등록
from django.utils.safestring import mark_safe
from django import template               #게시판 번호 메기는거 템플릿 만들기 > 빼기 함수가 없으므로 직접만들어 템플릿 적용

register = template.Library()

@register.filter
def sub(value, arg):
    return value-arg


@ register.filter()
def mark(value):
    extensions=["nl2br","fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

#mark_safe(markdown()) : 문자열을 HTML코드로 변환해 반환
#nl2br : 줄바꿈문자를 <br>태그로 바꿈 / enter한번만 해도 줄바꿈으로 인식
#fenced_code : 마크다운의 소스코드 표현을 위해 적용