from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

#Basic
class Faq(models.Model):
    #필요 모델명 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종수정자, 최종수정일시
    #카테고리 변수 선언
    NORMAL = 'NM'
    ACCOUNT = 'AC'
    ETC = 'ET'

    CATEGORY_CHOICES = [(NORMAL, '일반'), (ACCOUNT, '계정'), (ETC, '기타')] #choices 사용을 위한 tuple 선언
    #Tuple의 내용=(변수명, 사용자에게 보이는 이름)

    question = models.CharField(max_length=100, verbose_name='질문')
    #TextField는 html의 textarea와 유사한 구조를 가지며, 제목의 길이가 보통 한 문장이기 때문에 textarea는 그 구조가 과다하다고 보임
    category = models.CharField(max_length=2, choices = CATEGORY_CHOICES, verbose_name='카테고리', null=True, blank=True)
    #공식문서 참조, choices를 사용하기 위해 class 최상단에 변수명 선언 및 tuple 사용
    answer = models.TextField(verbose_name='답변', null=True, blank=True)
    created_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='생성자', null=True, blank=True)
    #역방향 관계 방지를 위해서 related_name 추가
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modify_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='최종 수정자', null=True, blank=True)
    last_modified_time = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True) #공식문서 참조, auto_now는 update에 유용한 옵션

#Advenced
class Inquiry(models.Model):
    #필요 모델명 : 카테고리, 제목, 이메일, 이메일수신여부, 전화번호, sms수신여부, 질문내용, 이미지, 생성자, 생성일시
    INORMAL = 'NM'
    IACCOUNT = 'AC'
    IETC = 'ET'

    CATEGORY_CHOICES = [(INORMAL, '일반'), (IACCOUNT, '계정'), (IETC, '기타')]

    category = models.CharField(max_length=2, choices = CATEGORY_CHOICES, verbose_name='카테고리')
    title = models.CharField(max_length=100, verbose_name='제목')

    emailAddress = models.EmailField(verbose_name='이메일주소')
    email_allow = models.BooleanField(verbose_name='이메일수신여부', default=False)
    #True가 되면 이메일 수신하는것, 기본은 False

    phonenumber = models.CharField(max_length=20, verbose_name='전화번호')
    sms_allow = models.BooleanField(verbose_name='문자수신여부', default=False)

    question = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

class Answer(models.Model):
    #필요 모델명 : 답변, 참조게시글, 생성자, 생성일시, 최종 수정자, 최종 수정일시
    answer=models.TextField(verbose_name='답변내용')
    post = models.ForeignKey(to='Inquiry', on_delete=models.CASCADE)

    created_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='생성자', null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)

    last_modify_person = models.ForeignKey(to=User, related_name='+', on_delete=models.CASCADE, verbose_name='최종 수정자', null=True, blank=True)
    last_modified_time = models.DateTimeField(verbose_name='최종 수정일시', auto_now=True) #공식문서 참조, auto_now는 update에 유용한 옵션