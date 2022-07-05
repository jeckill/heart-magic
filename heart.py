from telethon import TelegramClient, events, sync
import time
import random
import numpy as np
#🤍 белое сердце
#❤  красное
#💚 зел
#💙 синее
#🖤 черное
#💜 фиолетовое
#💛 желтое
#🧡 оранж
#api_id полученный ранее.
api_id= 'ВАШ APP_ID'
api_hash= 'ВАШ API_HASH'
chat_id= 'ВАШ CHAT_ID'
colors=["❤","🧡","💛","💚","💙","💜","🖤"]
matrix = [["🤍", "🤍", "🤍", "🤍", "🤍","🤍","🤍","🤍","🤍"], 
         ["🤍", "🤍", "❤", "❤", "🤍","❤","❤","🤍","🤍"],
         ["🤍", "❤", "❤", "❤", "❤","❤","❤","❤","🤍"],
         ["🤍", "❤", "❤", "❤", "❤","❤","❤","❤","🤍"],
         ["🤍", "❤", "❤", "❤", "❤","❤","❤","❤","🤍"],
         ["🤍", "🤍", "❤", "❤", "❤","❤","❤","🤍","🤍"],
         ["🤍", "🤍", "🤍", "❤", "❤","❤","🤍","🤍","🤍"],
         ["🤍", "🤍", "🤍", "🤍", "❤","🤍","🤍","🤍","🤍"],
         ["🤍", "🤍", "🤍", "🤍", "🤍","🤍","🤍","🤍","🤍"]]

def mix_color(heart):
    A=matrix
    A[1][2] = heart
    A[1][3] = heart
    A[1][5] = heart
    A[1][6] = heart
    A[2][1] = heart
    A[2][2] = heart
    A[2][3] = heart
    A[2][4] = heart
    A[2][5] = heart
    A[2][6] = heart
    A[2][7] = heart
    A[3][1] = heart
    A[3][2] = heart
    A[3][3] = heart
    A[3][4] = heart
    A[3][5] = heart
    A[3][6] = heart
    A[3][7] = heart
    A[4][1] = heart
    A[4][2] = heart
    A[4][3] = heart
    A[4][4] = heart
    A[4][5] = heart
    A[4][6] = heart
    A[4][7] = heart
    A[5][2] = heart
    A[5][3] = heart
    A[5][4] = heart
    A[5][5] = heart   
    A[5][6] = heart  
    A[6][3] = heart
    A[6][4] = heart
    A[6][5] = heart
    A[7][4] = heart
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in A])


def random_color():
    A=matrix
    A[1][2] = random.choice(colors)
    A[1][3] = random.choice(colors)
    A[1][5] = random.choice(colors)
    A[1][6] = random.choice(colors)
    A[2][1] = random.choice(colors)
    A[2][2] = random.choice(colors)
    A[2][3] = random.choice(colors)
    A[2][4] = random.choice(colors)
    A[2][5] = random.choice(colors)
    A[2][6] = random.choice(colors)
    A[2][7] = random.choice(colors)
    A[3][1] = random.choice(colors)
    A[3][2] = random.choice(colors)
    A[3][3] = random.choice(colors)
    A[3][4] = random.choice(colors)
    A[3][5] = random.choice(colors)
    A[3][6] = random.choice(colors)
    A[3][7] = random.choice(colors)
    A[4][1] = random.choice(colors)
    A[4][2] = random.choice(colors)
    A[4][3] = random.choice(colors)
    A[4][4] = random.choice(colors)
    A[4][5] = random.choice(colors)
    A[4][6] = random.choice(colors)
    A[4][7] = random.choice(colors)
    A[5][2] = random.choice(colors)
    A[5][3] = random.choice(colors)
    A[5][4] = random.choice(colors)
    A[5][5] = random.choice(colors)   
    A[5][6] = random.choice(colors)  
    A[6][3] = random.choice(colors)
    A[6][4] = random.choice(colors)
    A[6][5] = random.choice(colors)
    A[7][4] = random.choice(colors)
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in A])

async def clear():
    for row in range(9): 
        for x in range(9): 
                   matrix[row][x]="🤍"
async def  fill_color(msg):
   
    await client.edit_message(msg,mix_color("❤"))
    A=matrix
    for row in range(9): 
        for x in range(9): 
               if (A[row][x]!="❤"):
                   A[row][x]="❤"
                   time.sleep(0.050)
                   await client.edit_message(msg,'\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))


with TelegramClient('CLIENT_ID', api_id, api_hash) as client:

   @client.on(events.NewMessage())
   async def handler(event):
      sender = await event.get_sender()
#Если это вы пишете сообщение
      if(sender.id==chat_id):
#И сообщение содержит 

        if("❤️ magic" in event.message.message):
            msg=event.message
            await clear()
            # гирлянда
            for color in colors:
                await client.edit_message(msg,mix_color(color))
                time.sleep(0.3)
            #Рандомный цвет
            i=0
            while i<7:
                await client.edit_message(msg,random_color())
                i=i+1
                time.sleep(0.3)
            #закрашиваем матрицу
            await fill_color(msg);
           # Удаляем столбцы и строки
            A=matrix
            i=0
            while i<8:               
                
                A=np.delete(A, 1, 1)  
                A = np.delete(A, 1, 0)  
                await client.edit_message(msg,'\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))
                time.sleep(0.3)
                i=i+1
            time.sleep(0.5)
            #выводим надпись
            await client.edit_message(msg,"❤ Люблю тебя! ❤")
          
   client.run_until_disconnected()
