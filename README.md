# 스파르타 마켓 Backend (Django REST Framework)

## 1. 목표
스파르타 마켓의 백엔드 기능을 Django REST Framework를 사용하여 구현합니다.

## 2. DRF (Django REST Framework) 소개
- DRF는 Django의 확장 패키지로, RESTful API를 쉽게 만들 수 있도록 도와줍니다.
- **REST API**는 클라이언트-서버 간 데이터를 JSON, XML 형식으로 주고받기 위한 방식입니다.
- **Serializer**는 Django 모델을 JSON, XML 등으로 변환하거나 반대로 변환하는 역할을 합니다.

## 3. spartmarket_drf
- 프로젝트명 'spartamarket_drf
- 각 유저는 자신의 물건을 등록할 수 있습니다.
- 지역별 유저는 고려하지 않으며, 구매 기능은 제외하였습니다.
- 프론트엔드 구현 대신, Postman을 사용하여 API를 테스트하였습니다.
## ⏲️ 개발기간
- 2024.09.09(월) ~ 2024.09.10(화)

## 📚️ 기술스택
- 백엔드(Backend) 
    - Python
    - Django

- 데이터베이스(Database)
  	- SQLite

- 기타 도구 및 라이브러리
  	- Git/GitHub
  	- django-extensions

### ✔️ Language
- Python: 백엔드 로직, 데이터 처리 및 API 개발을 위한 언어.
- SQL: 데이터베이스 쿼리 및 관리에 사용.
  
### ✔️ Version Control
- Git: 소스 코드 버전 관리 시스템. 프로젝트의 버전 기록을 유지하고 협업을 지원함.
- GitHub: 원격 저장소 호스팅 서비스, 코드 리뷰 및 협업을 지원.

### ✔️ IDE
- Visual Studio Code: Python의 개발을 위한 통합 개발 환경. 확장성 높은 플러그인 시스템 지원.
  
### ✔️ Framework
- Django: Python 기반의 웹 프레임워크, 모델-뷰-템플릿(MVT) 패턴을 사용하여 효율적인 웹 애플리케이션 개발.

### ✔️  DBMS
- SQLite: 가벼운 관계형 데이터베이스 관리 시스템. 파일 기반의 데이터베이스로, 설정과 유지 관리가 간편하며, 로컬 개발과 작은 규모의 배포에 적합.
  
## 서비스 구조
- 백엔드: 데이터 처리, 비즈니스 로직 및 API를 처리.
- 데이터베이스: SQLite를 사용하여 사용자 및 상품 데이터를 저장 및 관리.
- API: 프론트엔드와 백엔드 간의 데이터 교환을 처리.


## API 명세서

### 1.MVP (Minimum Viable Product)

#### 1.1 회원가입
- **Endpoint**: `/api/accounts`
- **Method**: `POST`
- **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력. 성별, 자기소개는 선택 사항.
- **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증 추가 가능.
- **구현**: 데이터 검증 후 사용자 저장.

#### 1.2 로그인
- **Endpoint**: `/api/accounts/login`
- **Method**: `POST`
- **조건**: 사용자명과 비밀번호 필요.
- **검증**: 입력된 사용자명과 비밀번호가 데이터베이스와 일치해야 함.
- **구현**: 로그인 성공 시 토큰 발급, 실패 시 에러 메시지 반환.

#### 1.3 프로필 조회
- **Endpoint**: `/api/accounts/<str:username>`
- **Method**: `GET`
- **조건**: 로그인 필요.
- **검증**: 로그인한 사용자만 자신의 프로필 조회 가능.
- **구현**: 사용자 정보를 JSON으로 반환.

### 2 상품 관련 기능

#### 2.1 상품 등록
- **Endpoint**: `/api/products`
- **Method**: `POST`
- **조건**: 로그인 상태에서 제목, 내용, 상품 이미지 입력 필요.
- **구현**: 상품 등록 후 데이터베이스에 저장.

#### 2.2 상품 목록 조회
- **Endpoint**: `/api/products`
- **Method**: `GET`
- **조건**: 로그인 필요 없음.
- **구현**: 모든 상품 목록을 페이지네이션으로 반환.

#### 2.3 상품 수정
- **Endpoint**: `/api/products/<int:productId>`
- **Method**: `PUT`
- **조건**: 로그인 상태에서 해당 상품의 작성자만 수정 가능.
- **검증**: 요청자가 작성자인지 확인.
- **구현**: 입력된 정보로 기존 상품 정보 업데이트.

#### 2.4 상품 삭제
- **Endpoint**: `/api/products/<int:productId>`
- **Method**: `DELETE`
- **조건**: 로그인 상태에서 작성자만 삭제 가능.
- **검증**: 요청자가 작성자인지 확인.
- **구현**: 해당 상품을 데이터베이스에서 삭제.

## 3. 선택 기능

### 3.1. MVP (Optional)

#### 3.1.1 로그아웃
- **Endpoint**: `/api/accounts/logout`
- **Method**: `POST`
- **조건**: 로그인 상태.
- **구현**: 토큰 무효화 또는 다른 방법으로 로그아웃 처리.

#### 3.1.2 본인 정보 수정
- **Endpoint**: `/api/accounts/<str:username>`
- **Method**: `PUT`
- **조건**: 이메일, 이름, 닉네임, 생일 필수 입력. 성별, 자기소개는 선택 사항.
- **검증**: 로그인한 사용자만 본인 정보 수정 가능. 이메일과 username 중복 검증.
- **구현**: 입력된 정보를 검증 후 데이터베이스 업데이트.

#### 3.1.3 패스워드 변경
- **Endpoint**: `/api/accounts/password`
- **Method**: `PUT`
- **조건**: 기존 패스워드와 새 패스워드가 달라야 함.
- **검증**: 패스워드 규칙 검증 후 저장.

#### 3.1.4 회원 탈퇴
- **Endpoint**: `/api/accounts`
- **Method**: `DELETE`
- **조건**: 로그인 상태에서 비밀번호 재입력 필요.
- **검증**: 비밀번호가 일치하는지 확인 후 계정 삭제.

## 3.2. 도전 기능 가이드

#### 3.2.1 페이지네이션 및 필터링
- **구현**: 상품 목록 조회 시 페이지네이션 및 필터링(검색 기능) 추가.

## ERD
erDiagram
    User {
        int id
        string username
        string password
        string email
        string name
        string nickname
        date birth
        string gender
        string introduction
    }

    Product {
        int id
        string title
        string description
        string image
        datetime created_at
        datetime updated_at
    }

    User ||--o{ Product : "has many"
    Product {
        int id
        string title
        string description
        string image
        datetime created_at
        datetime updated_at
    }

    Product {
        int id
        string title
        string description
        string image
        datetime created_at
        datetime updated_at
    }

    Product ||--o{ Comment : "has many"
    Comment {
        int id
        text content
        datetime created_at
    }

    User ||--o{ Comment : "has many"
    Product ||--o{ Like : "has many"
    Like {
        int id
        datetime created_at
    }
    
    User ||--o{ Like : "has many"


## 프로젝트 파일 구조

```plaintext
SpartaMarket/
├── accounts/               # 사용자 계정 관련 앱
│   └── *                   # 앱 관련 파일들 
├── media/                  # 미디어 파일 저장소
├── products/               # 제품 관련 앱
│   └── *                   # 앱 관련 파일들
├── spartamarket/           # 프로젝트 설정 디렉터리
│   ├── settings.py         # 프로젝트 설정 파일
│   ├── urls.py             # 전역 URL 패턴 정의
├── manage.py               # Django 관리 커맨드 파일
└── README.md               # 프로젝트 설명서
