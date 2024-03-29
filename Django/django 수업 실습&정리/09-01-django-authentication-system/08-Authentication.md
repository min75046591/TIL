### AuthenticationForm()
모델폼은 DB에 저장. form은 DB에 저장 x
하지만 로그인 인증에 사용할 데이터를 입력 받는 점은 같음.

view 1. 로그인 페이지 (GET)
view 2. 로그인 로직 진행 (POST)
-> 하나의 view 함수로 합칠 수 있음 (create 처럼)

  
쿠키와 세션을 통해 상태를 유지!

placeholder 속성을 통해 이름을 입력하라는 안내 메시지를 표시