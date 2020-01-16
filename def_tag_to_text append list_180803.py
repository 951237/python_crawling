# 태그를 텍스트로 바꾸어서 리스트로 변환

def tag_to_text():
    list_td = []

    for td in all_td:
        td_text = td.text.replace('\n','').strip()
        list_td.append(td_text) #결과값을 리스트에 추가하기

    return list_td