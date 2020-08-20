import telegram


# today_brief_bot 토큰
token = '토큰'
bot = telegram.Bot(token=token)

# 봇이 보낸 메세지 출력하기
for i in bot.getUpdates():
    print(i.message)

# 텔레그램 봇으로 상대방에게 메세지 보내기
# bot.sendMessage(chat_id='428116987', text='Hello Wolrd')