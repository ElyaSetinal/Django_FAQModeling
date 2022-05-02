# django_mission_03-ElyaSetinal

### Basic 미션 내용 : 고객센터 관리자 페이지 구성하기
- 고객센터 앱의 모델을 관리자페이지에 등록 구성

##

### 요구사항
- 고객센터(`support`) 앱의 자주묻는질문(`Faq`), 1:1문의(`Inquiry`), 답변(`Answer`) 관리자 페이지 등록
  - 자주묻는질문(`Faq`)
    - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
    - 검색 필드 : 제목
    - 필터 필드 : 카테고리
  - 1:1문의(`Inquiry`)
    - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
    - 검색 필드 : 제목, 이메일, 전화번호
    - 필터 필드 : 카테고리
    - 인라인모델 : 답변(`Answer`)
  - 답변(`Answer`)
    - 1:1문의 모델에 인라인모델로 추가
##
### Advenced 미션 내용 : 기본 관리자 페이지의 사용성 개선 및 답변 상태 관리 기능 추가
##
### 요구사항
- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력
        ※ action을 추가 학습을 위한 목적으로 실제 문자, 메일은 발송하지 않습니다.
##
### Mission Status
`Inquiry`의 경우, Basic과 Advenced 모두 표현이 되어 있어서, 결과 사진은 분리하지 않았습니다.
##
#### Basic - `FAQ` admin 화면
- `FAQ` 구성화면
![01](https://user-images.githubusercontent.com/102591378/166178326-73d6273b-f27d-44ca-8897-ca36c209cb54.jpg)
- 제목 검색시
![02](https://user-images.githubusercontent.com/102591378/166178348-c7c7ba2f-98e2-4fad-bfad-f5c69fbe2eb1.jpg)
- 필터 사용
![03](https://user-images.githubusercontent.com/102591378/166178353-488aef94-5c32-4c32-ae4e-98608b0e1b7a.jpg)

#### Basic, Advenced - `Inquiry` admin 화면
- `Inquiry` 구성 화면
![A01](https://user-images.githubusercontent.com/102591378/166178861-772ddd2a-0bfe-4856-9027-28722e41e208.jpg)
- 검색 화면
![A02-horz](https://user-images.githubusercontent.com/102591378/166178869-f6a2f520-f067-438a-ad9b-ef5859481c20.jpg)
- [Basic] 카테고리 필터 사용
![A05](https://user-images.githubusercontent.com/102591378/166178901-ffa6d928-4545-4505-bdd5-8f419c576edc.jpg)
- [Basic] 1:1 답변 Inline

![A06](https://user-images.githubusercontent.com/102591378/166178964-e253d289-9b41-4808-9620-8b1aa96e8fcb.jpg)
- [Advenced] 상태 필터 사용
![A07](https://user-images.githubusercontent.com/102591378/166178916-89d4de32-4f90-4288-9b57-a177e04fffa9.jpg)
- [Advneced] 이메일/SMS 송부(상태가 답변 완료인 경우에만 송부하도록 설정)
![A08](https://user-images.githubusercontent.com/102591378/166178991-370ef97c-8cfe-4ef4-86b0-6f0fad232f99.jpg)
![A11](https://user-images.githubusercontent.com/102591378/166179465-72f9c058-3ba4-4403-9ee0-3d125a97abf0.jpg)

 
