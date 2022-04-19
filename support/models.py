from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

#Basic
class Faq(models.Model):
    #카테고리 변수 선언
    NORMAL = 'NM'
    ACCOUNT = 'AC'
    ETC = 'ET'

    CATEGORY_CHOICES = [(NORMAL, '일반'), (ACCOUNT, '계정'), (ETC, '기타')]

    question = models.CharField(max_length=100, verbose_name='질문')
    category = models.CharField(max_length=2, choices = CATEGORY_CHOICES, verbose_name='카테고리', null=True, blank=True)
    answer = models.TextField(verbose_name='답변', null=True, blank=True)
    created_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='생성자', null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modify_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='최종 수정자', null=True, blank=True)
    last_modified_time = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True) #공식문서 참조, auto_now는 update에 유용한 옵션

#Advenced
class Inquiry(models.Model):
    INORMAL = 'NM'
    IACCOUNT = 'AC'
    IETC = 'ET'

    CATEGORY_CHOICES = [(INORMAL, '일반'), (IACCOUNT, '계정'), (IETC, '기타')]

    category = models.CharField(max_length=2, choices = CATEGORY_CHOICES, verbose_name='카테고리')
    title = models.CharField(max_length=100, verbose_name='제목')

    emailAddress = models.EmailField(verbose_name='이메일주소')
    email_allow = models.BooleanField(verbose_name='이메일수신여부', default=False)

    phonenumber = models.CharField(max_length=20, verbose_name='전화번호')
    sms_allow = models.BooleanField(verbose_name='문자수신여부', default=False)

    question = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

class Answer(models.Model):
    answer=models.TextField(verbose_name='답변내용')
    post = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)

    created_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='생성자', null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

    last_modify_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='최종 수정자', null=True, blank=True)
    last_modified_time = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True) #공식문서 참조, auto_now는 update에 유용한 옵션