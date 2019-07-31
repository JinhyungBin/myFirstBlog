from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200) #title 변수에는 models의 char(문자)로 되어있는 데이터를 title로 정의하고 그것의 최대 길이는 200으로 지정하겠다.
    pub_date=models.DateTimeField('date published') #pub_date 변수에 models의 DateTimeField(날자와 시간을 나타네는 데이터)를 처리
    body=models.TextField() #CharField가 짧은 문자열을 나타내면 그보다 조금더 긴 문자열을 TextField라고 한다. 즉 model의 TextFiled를 body로 정의 하겠는말

    def __str__(self):# 글의 제목을 내가 쓴 제목으로 나오게 하는 함수
        return self.title
    
    def summary(self):
        return self.body[:100]

    