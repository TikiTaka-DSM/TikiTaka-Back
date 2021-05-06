# TikiTaka Project

### 명세
https://www.notion.so/API-e9be2b5d5e254abb840f12dc5b585da1

### 유지보수

1) User Model unit test
2) User Model에서 image와 introduction에 server_default 지정, \__init\__() 명시 -> services/user.py 에서 값 넣어주던거 제거
3) service 함수들 중 session 사용하는 함수들 model로 이동
4) Restful API 설계 적용