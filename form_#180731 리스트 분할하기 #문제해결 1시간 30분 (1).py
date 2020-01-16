all_td = all_eleSc.findAll('td')

# 리스트를 6개씩 분할하여 출력하기 #어썸썸
start_pos = 0
end_pos = len(list_td)
div = 6

for i in range(start_pos,end_pos+div,div): #i는 왜 사용된지 잘 이해가 안됨.
    out = list_td[start_pos:start_pos+div]
    if out != []:
            print(' / '.join(out)) #리스트를 문자열로 변환
    start_pos = start_pos + div