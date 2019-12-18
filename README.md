# KNU-20192-team1
2019F_소프트웨어 설계 [현대인들을 위한 픽업 서비스, "Take"]

프로젝트 개요 및 상세 설명 -> https://www.notion.so/3febb6fff6234fadbcb2e20a7f0cadcd

## Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.


## Settings

www.python.org에서 Python 3.7이상의 버전으로 Python 다운로드

```bash
python -m venv myvenv # 가상환경명 설정
source myvenv/Scripts/activate # 가상환경 실행
pip install django # Django 설치
python manage.py runserver # Django 서버 작동
```


## Introduction

```bash
* 제공 기능 : 회원가입 및 로그인, 가게 정보 등록, 가게 검색, 즐겨찾기, 음료 주문 및 픽업

1. 회원가입 및 로그인
- 회원의 종류는 크게 사용자, 가게 주인(ex. 키아누/1234), 관리자(ex.admin/admin) 3가지로 나눌 수 있다.
사용자가 Take 측에 가게를 등록하면 가게 주인 계정으로 전환되며, 사용자의 기능과는 차이가 있을 수 있다.

2. 가게 정보 등록
- 가게 등록 : 사용자가 자신의 가게 정보를 등록할 수 있다.
불필요시 삭제를 할 수도 있다; 삭제시 사용자로 종류 전환됨
- 메뉴 등록 : 자신이 등록한 가게에만 메뉴를 등록할 수 있다.
이를 통해 사용자의 주문을 받을 수 있음

3. 가게 검색
- 이름으로 검색 : 사용자는 이름으로 가게를 검색할 수 있다.
- 지도로 검색 : 사용자는 자신의 위치 주변 가게를 검색할 수 있다.
현재는 지도 상 경북대학교 쪽문 근처의 카페만 등록되어 있음

4. 즐겨찾기
- 사용자는 자신이 즐겨찾는 카페를 즐겨찾기 등록할 수 있다.
즐겨찾기로 등록해놓으면 메인 화면에서 손쉽게 접근할 수 있다.

5. 음료 주문 및 픽업
- 사용자는 자신이 원하는 음료를 수량에 맞게 주문할 수 있다. 필요시 삭제도 가능
- 가게 주인은 자신의 가게에 들어온 주문을 확인하고 픽업확인 버튼을 통해 거래를 완료할 수 있다.
```
