from django.shortcuts import render

# Create your views here.
def index(request):
    # url로부터 호출받는 view 함수
    # index view 함수의 목적 - 메인 페이지 1개를 응답
    # 응답 덩어리(객체)는 반드시 함수의 반환 값으로 클라이언트에게 전달됨
    # 경로를 적는 것임. index.html 이 부분이 
    # 함수 이름과 템플릿 이름이 꼭 동일하지 않아도 됨. 그러나 헷갈리니까
    return render(request, 'index.html')