from django.contrib import admin

from .models import Faq, Inquiry, Answer

# Register your models here.

@admin.register(Faq)
class Faqmodeladmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'last_modified_time',) # 목록페이지 출력 필드
    search_fields = ('question',) # 검색 필드
    search_help_text = 'FAQ 질문 검색' # 검색 필드 도움말
    list_filter = ('category',) # 필터 필드
    list_p_page = 20 # 한페이지에 출력될 게시글 수
    readonly_fields = ('created_time', 'last_modified_time') 

class AnswerInline(admin.StackedInline):
    model = Answer # Inline에 연결하는 모델
    max_num = 3 # 최대 갯수
    verbose_name = '답변'
    verbose_name_plural = '답변 목록'

@admin.register(Inquiry)
class Inqmodeladmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time', 'writer', 'answerstate','email_allow', 'sms_allow', ) # 목록 페이지 출력
    #Advenced를 위해 answerstate 추가
    search_fields = ('title', 'emailAddress', 'phonenumber', 'writer__username',) # 검색 필드
    #Advenced를 위해 writer__username을 추가
    #ForeignKey를 가지는 항목은, ['foreign_key__related_fieldname']으로 추가해야한다.
    search_help_text = '질문 제목, 이메일, 전화번호, 작성자 검색' # 검색 필드 도움말
    list_filter = ('category', 'answerstate',) # 필터 필드
    inlines = [AnswerInline] # 인라인 모델

    actions =['answer_send','bar','state_in','state_ready','state_complete',] # admin 페이지에서 사용할 액션 추가
    
    @admin.action(description='Send:작성된 답변을 송부합니다.')
    def answer_send(modeladmin, request, queryset):
        #email_allow, sms_allow, 이메일과 문자 허용하는 모델명
        for item in queryset:
            if item.answerstate == 'RC': # 답변이 완료되어야 작업 시행
                if item.email_allow == 1: print(f"{item.writer}-{item.title}의 E-mail 답변이 발송되었습니다.") # 이메일 허용 여부 확인
                else: print(f"{item.writer}-{item.title}의 작성자가 E-mail을 허용하지 않았습니다.")
                
                if item.sms_allow == 1: print(f"{item.writer}-{item.title}의 SMS 답변이 발송되었습니다.") # SMS 허용 여부 확인
                else: print(f"{item.writer}-{item.title}의 작성자가 SMS을 허용하지 않았습니다.")
            
            else: print(f"{item.writer}-{item.title}의 답변이 없습니다.") # 문의등록, 접수완료시 시행

    @admin.action(description="------------------------------")
    def bar(modeladmin, request, queryset): pass # 구분선 추가. 다른 방법을 찾지 못해서 별도 추가함

    @admin.action(description='상태를 문의등록으로 설정합니다.')
    def state_in(modeladmin, request, queryset): queryset.update(answerstate='ER') # 시연 작업시 편의성을 위한 action용 함수

    @admin.action(description='상태를 접수완료로 설정합니다.')
    def state_ready(modeladmin, request, queryset): queryset.update(answerstate='RP') # 시연 작업시 편의성을 위한 action용 함수

    @admin.action(description='상태를 답변완료로 설정합니다.')
    def state_complete(modeladmin, request, queryset): queryset.update(answerstate='RC') # 시연 작업시 편의성을 위한 action용 함수