# 1. 스크립트로 변환: 파일명의 확장자를 *.command로 바꾸자.
#      ex) mycode.command
#
# 2. 스크립트 인터프리터 설정: 첫줄에 shebang line을 "#!/usr/bin/env python"와 같이 추가한다. 이 의미는 python으로 이 스크립트를 실행하라는 의미이다.
#
# 3. 실행파일로 변환: chmod를 사용하여 스크립트를 실행파일로 속성변경한다.
#      ex) chmod +x mycode.command