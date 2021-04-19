# TikiTaka Project

목적: `socket.io`를 사용해서 채팅 서비스 구현해보기

- [x] test 코드 짜기
- [ ] 조금 더 구조화 된 코드 아키텍쳐 구상하기

### 명세
https://www.notion.so/API-e9be2b5d5e254abb840f12dc5b585da1

### 유지보수

1) User Model unit test
2) User Model에서 image와 introduction에 server_default 지정, __init__() 명시 -> services/user.py 에서 값 넣어주던거 제거
3) 모든 services 함수에서 함수명 속 get 키워드를 제거

