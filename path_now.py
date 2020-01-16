## 스크립트나 파일의 경로 확인하는 법
import os
print (os.getcwd()) # 현재 디렉토리의 경로
print (os.path.realpath(__file__)) # 현재 경로와 파일이름
print (os.path.dirname(os.path.realpath(__file__))) # 해당 파일이 위치한 디렉토리