from django.shortcuts import render, get_object_or_404, redirect # redirect<- redirect를 사용하기 위해 임포트
from django.utils import timezone  #timezone.datetime.now()를 사용하기 위해 
from .models import Blog

def home(request):
    blogs=Blog.objects #model로 부터 blog의 객체 정보를 전달 받을수 있게됨(.objects)
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']        #new에서 입력한 제목을 블로그의 제목에 넣어준다.
    blog.body=request.GET['body']          #new에서 입력한 내용을 블로그의 내용에 넣어준다.
    blog.pub_date=timezone.datetime.now()  #블로그를 작성한 시점을 넣어줌 timezone.datetime.now()<- 이 함수를 쓰려면 from django.utils import timezone를 해줘야함
    blog.save()                            #블로그라는 객체에 넣은 내용을 데이터베이스에 저장하라
                                           #객체.delete() <- 객체에 해당하는 내용을 지워라
    return redirect('/blog/'+str(blog.id)) #위에 있는 함수들을 처리후 ()안의 url로 넘겨라 <-redirect 를 쓰려면 import를 따로해줘야함
                                           #입력한 정보를 저장후 이동하고 싶은 url은 home/blog/blog아이디(번호)
                                           #str(blog.id)에서 str을 써준이유는 url은 str(문자열)이기 때문에 형변환을 해줌 (int)blog.id->(str)blog.id 
