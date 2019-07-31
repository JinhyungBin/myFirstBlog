from django.contrib import admin
from django.urls import path, include       #include는 blog의 url로부터 정보를 받아오기 위해 import시켜줌
import blog.views
import portfolio.views
from django.conf import settings            #media를 씌위해 임포트 해줘야 할것들
from django.conf.urls.static import static  #media를 씌위해 임포트 해줘야 할것들  암기!!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('blog/', include('blog.urls')), #blog 앱에 있는 urls.py에 서 값을 받아오고 형식은 -> 사이트 주소/blog/urls 이런식으로 하겠다고 선언
    path('portfolio/',portfolio.views.popol, name ="popol"),
    path('travelAmerica/',portfolio.views.travelAmerica, name ="travelAmerica"),
    path('travelChina/',portfolio.views.travelChina, name ="travelChina"),
    path('travelLaos/',portfolio.views.travelLaos, name ="travelLaos"),
    path('test/',portfolio.views.test, name ="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media를 사용하기 위해 setting 해주는것

# 이런 식으로 선언해줘도 상관없음
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media를 사용하기 위해 setting 해주는것