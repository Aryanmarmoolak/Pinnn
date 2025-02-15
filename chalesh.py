from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import * 
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError , PeerIdInvalidError,UserIsBlockedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, events
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.custom import Button
from telethon import functions, types
import random
import sys
import csv
import traceback
from time import sleep
import random as rn
#import socks
import time
import redis
import asyncio
import re

bots= [198626752,175844556]
redis = redis.Redis(host='localhost', port=6379, db=10,password="ICeAyToLa")
#redis = redis.Redis(host='localhost', port=6379, db=2)
admin = [614103169]
admin_white = [614103169,1086867927]
#message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
#token='732629769:AAEyvZOG3SE0bGvSO-FV57-BEHSXeg-OsVQ' #test
token = '1209533581:AAFvjpsqD8KJ_wZfkVCSyyC4Gdz6Hrasxds' #asli
#proxy = (socks.SOCKS5, '127.0.0.1', 9150)
api_id = 947499
api_hash = 'cf6a6c0888208ed996e0700e6725f262'
bot = TelegramClient(token, api_id, api_hash).start(bot_token=token)
phone = input('your phone:')
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        client.sign_in(code=input('Your Code :'))
    except SessionPasswordNeededError:
        client.sign_in(password=input('your Password :'))
client.parse_mode = 'html'
#bot = TelegramClient(token, api_id, api_hash,proxy=proxy).start(bot_token=token)
bot.connect()
bot.parse_mode = 'html'
bot.send_message('aytola','online')
client.send_message('aytola','online')
redis.set('tag_white',str(['off']))
bot_list     = [
    175844556, 198626752,  # ww moderator, ww moderator beta
    618096097, 1029642148,614103169  # black ww, black ww 2
]

emoji = ['🦋','💐','🌹','🌺','🌸','🌼','🌾','☘️','🍏','🍎','🍐','🍊','🍋','🍉','🍇','🍓','🍈','🍒','🍑','🍹','🐶','🐥','🐣','🦄','🌹','🌑','🌈','🌷','💐','🌸','🌺','🌼','🌻','☔️','😻']  
matn = ['جویین شو','بدو بدو','بازی شروع شداااا','کجاااایی پس','جویین بزن','بدووو تا دیر نشده','بدو بازی','واعیییی بازی داریم بیا','کجاااا رفتی بیا','نیای قهرم','جوین شو بکشمت','گرگی علیو بخور','بدو شکار میشی','بیااااااا','کجااااایی','بدو بدو جوین شو گرگی','مرگ گری بیا','نیای بلاکی','فورسه بیا','چیشدی','جوین بزن ادمینی','میدونم میخای جوین شی روت نمیشه','خجالت نکش بیا','خونه خودتونه میتونی جویین بزنی','بدو بدوووووو دیر میشه ها','جوین شو عشقش','عسلش بیا','بیا رل برات پیدا میکنیم','جوین شو شکار رلت میشه','بدو بدو که قراره گرگ شی','بدو قاتلی','یباشکی جویین بزن بقیه نبینن','بدوووو الان فورس میشه','وای بات میگه قراره قاتل شی','نیای از دستت رفته','رلت جوینه جوین بزن','رلت منتظرته ها','بیا بازی دورهمیم','بدو جایزه میگیری','کادو داری','بیا','بدو خسته شدم','ناز نکن بیا','لوس نشو یه جوینه دیه','دست دست دست','بدو بدو بدو','بیا وسط','خل شدم بیا','نیومدی','سریع تر بیا','بدو لاوری ببر','join']


game = {'all_user':[],'role_users':{},'blocked':[],'shekarchi':0,'sv':''}

text_game = '''📃لیست نقش ها : 
‎
<b>[💂🏻‍♀️] {0} : شکارچی</b>

{1}

Join @white_channel
'''

comment = r'/sn|/li|/up|/dl|/ev|/block|/unblock|/sv|/vt|/shekar|/vip|/unvip'
game_finish = r'طول مدت بازی|مدت زمان بازی|مدت بازی|مدت بُکُن بُکُن'
game_list = r'بازیکن های زنده|فراموشکارای زنده|هنرمندای فعال|دانشجوهای مشغول به تحصیل|مسافرای زنده ی توی قطار|بازیکنان زنده|بازیکن های آنلاین|کونده های زنده |بازیکنان درحال بازی|برره ای های زنده|مسافر های زنده:|کشتی گیران سالم|هیولاهای زنده|بازمانده ها'
death = r'مرده|اخراج شده|کنار رفته|آفلاین|تبعید شده|بگا رفته|خارج شده|سقَط شده|فرار کرده|اخراج شده|نفله وشده'

async def main():
    try:
        def game_stats(name):
            bet = redis.get('bet_white_ice')
            if not bet == None:
                bet = eval(bet.decode('utf-8'))
                try:
                    game_number = bet['game_numbers']
                except KeyError:
                    bet['game_numbers'] = 0
                    game_number = bet['game_numbers']
                if game_number == 10:
                    for i in bet['bet_game_zarib']:
                        s = bet['bet_game_zarib'][i]
                        if s == 0:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(5,9)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 1:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(3.2,5)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 2:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(2.8,3.2)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 3:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(2.4,2.8)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 4:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(2.2,2.4)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 5:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(2.08,2.2)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 6:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(1.8,2)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 7:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(1.6,1.8)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 8:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(1.4,1.6)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 9:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(1.2,1.4)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))
                        elif s == 10:
                            bet['bet_game_zarib'][i] = 0
                            x = random.uniform(1.05,1.2)
                            bet[i] = x
                            redis.set('bet_white_ice',str(bet))     
                    bet['game_numbers'] = 0 
                    redis.set('bet_white_ice',str(bet))
                else:
                    game_number += 1
                    bet['game_numbers'] = game_number
                    bet['bet_game_zarib'][name] = bet['bet_game_zarib'][name] + 1
                    redis.set('bet_white_ice',str(bet))
                    try:
                        bot.send_message('aytola','game bet: {0}'.format(game_number))
                    except Exception as e:
                        print(e)
        async def bet_button(userid,team):
            try:
                bet = redis.get('bet_white_ice')
                user_bet = redis.get('{0}bet'.format(userid))
                print(user_bet)
                #print(list_m)
                if not user_bet == None:
                    user_bet = eval(user_bet.decode('utf-8'))
                    if not bet == None:
                        #print(bet)
                        bet = eval(bet.decode('utf-8'))
                        try:
                            if not user_bet['bet_one'] == '':
                                check_games = user_bet['bet_one'].split(':')
                                if int(check_games[1]) < bet['game_number']:
                                    try:
                                        user_bet['game'] = 1
                                        user_bet['bet_one'] = ''
                                        user_bet['bet_one_snow'] = 0
                                        if not user_bet['bet_two'] == '':
                                            check_gamess = user_bet['bet_two'].split(':')
                                            if int(check_gamess[1]) < bet['game_number']:
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 0
                                            else:
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                        else:
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 0
                                        redis.set('{0}bet'.format(userid),str(user_bet))
                                        redis.set('{0}check_ros'.format(userid),team)
                                        await bot.send_message(userid,'چند تا برفـــ❄️ شرط میبندی ؟')
                                    except Exception as e:
                                        print(e)
                                elif int(check_games[1]) >= bet['game_number']:
                                    if user_bet['game'] == 0:
                                        redis.set('{0}check_ros'.format(userid),team)
                                        await bot.send_message(userid,'چند تا برفـــ❄️ شرط میبندی ؟')
                                    elif user_bet['game'] == 1:
                                        redis.set('{0}check_ros'.format(userid),team)
                                        await bot.send_message(userid,'چند تا برفـــ❄️ شرط میبندی ؟')
                                    elif user_bet['game'] == 2:
                                        await bot.send_message(userid,'شما 2️⃣ شــرط رو بستیــن❌. لطفــا صبـ...ـر کنیــد شــرط های شــما اجــــرا بشن🔜')
                            else:
                                user_bet['bet_one'] = ''
                                user_bet['bet_one_snow'] = 0
                                user_bet['bet_two'] = ''
                                user_bet['bet_two_snow'] = 0
                                user_bet['game'] = 0
                                redis.set('{0}bet'.format(userid),str(user_bet))
                                redis.set('{0}check_ros'.format(userid),team)
                                redis.set('{0}check_ros'.format(userid),team)
                                await bot.send_message(userid,'چند تا برفـــ❄️ شرط میبندی ؟')
                        except KeyError as e:
                            print('errors')
                            await bot.send_message(userid,'جهـ↵ـت فعـ✅ـال سـازے قابلیـت شـ💸ـرط بنـدی\nباید 〖１１００〗بـرفـ❄️ پــرداخـ♲ـت کنـی\n\n🖇⦙ هر زمـانـ⏰ که دلـت این هیجـ♨️ـان رو خواسـت به 〖 @Aytola  〗مراجـعه کن و درخواستـ📮 فعال سازے بده .')
                    else:
                        await bot.send_message('aytola','روس شرط بسته نشد مشکل داره')
                else:
                    await bot.send_message(userid,'فعال نیست')
            except Exception as e:
                print(e)

        async def mainsnow(userId,chat_id,text,text_1,text_2,num1,num2): 
            list_m = eval(redis.get(userId).decode('utf-8'))
            print(num1,list_m[text_1])
            if list_m[text_1] > num1:
                list_m[text_1] = list_m[text_1] - num1
                list_m[text_2] = list_m[text_2] + num2
                redis.set(userId,str(list_m))
                await bot.send_message(chat_id,text)
            else :
                print(list_m)
                await bot.send_message(chat_id,'موجودی شما کافی نیست❌')

        async def menu_start(chat_id):
            k1 = Button.inline('👑خرید مقام👨🏻‍💻', b'sell_magham')
            k2 = Button.inline('⚡️خرید قدرت 💪', b'sell_ghodrat')       
            k3 = Button.url('راهنما🧐',b'https://t.me/IcePower_channel')
            k4 = Button.url('کانال ارتباطی ما', b't.me/baron')
            k5 = Button.inline('ثبت اطلاعات شخصی🙋🏻‍♂️',b'sabtetlaat')
            k6 = Button.inline('اتاق جوایز 🗃',b'roomwardbot')
            k7 = Button.inline('🎰شرط بندی💸',b'bet_wolf')
            k8 = Button.inline('❄️⟺⛄️',b'tabdilmony')
            k9 = Button.inline('🛡 شیلد ⏱',b'shildwhite')
            await bot.send_message(chat_id,'ربات چالش لند جهت خرید مقام و قدرت و یا راهنما کلیک کنید',buttons=[[k1,k2],[k3],[k5],[k6],[k7],[k8],[k4]])

        @bot.on(events.CallbackQuery)
        async def callback(event):
            if event.data == b'roomwardbot':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['key'] >= 2:
                    k1 = Button.inline('🎁',b'jyze')
                    k2 = Button.inline('🎁',b'jyze')
                    k3 = Button.inline('🎁',b'jyze')
                    k4 = Button.inline('🎁',b'jyze')
                    k5 = Button.inline('🎁',b'jyze')
                    k6 = Button.inline('🎁',b'jyze')
                    k7 = Button.inline('🎁',b'jyze')
                    k8 = Button.inline('🎁',b'jyze')
                    k9 = Button.inline('🎁',b'jyze')
                    back_click = Button.inline('⬅️برگشت',b'backclick')
                    await event.edit('🥳 تو تونستیـ با موفقیتـ وارد اتاقـ جوایز 🎁 بشیـ🎉\nحالا یکیـ از جعبهـ هارو میتونیـ انتخوابـ کنیـ😉',buttons=[[k1,k2,k3],[k4,k5,k6],[k7,k8,k9]])
                else:
                    await event.answer('کلید کافی ندارید',alert=True)
            elif event.data == b'jyze':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                list_m['key'] = list_m['key'] - 2
                redis.set(event.sender_id,str(list_m))
                x = random.randint(1,10)
                jayzem = str(redis.get('jayze{0}'.format(x)).decode('utf-8'))
                entity_member = await bot.get_entity(event.sender_id)
                await event.edit('تبریکـ🥳ــ👏🏻 شما برنده  {0} شدید\n🎁جوایز شما در اسرع وقت تقدیم خواهد شد💌\nاز بردباری شما سپاسگذاریمـ∞🙏🏻'.format(jayzem))
                await bot.send_message(-1001451143749,'کاربر  {0} \nبرنده جایزه  {1} شد '.format('<a href=tg://user?id='+str(entity_member.id)+'>'+ entity_member.first_name+'</a>',jayzem))
            elif event.data == b'roomkeyopen':
                k1 = Button.inline('ورود به اتاق جوایز',b'roomwardbot')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت باز کردن اتاق جوایز نیاز به 2 کلید دارید و با انتخاب گزینه ورود به اتاق جوایز 2 کلید از شما کسر خواهد شد',buttons=[[k1],[back_click]])
            elif event.data == b'ekhtlaswhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_mafiawhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت اختلاس  10 ⛄️  از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'roomawardswhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_roomawardswhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('خرید توانایی رفتن به اتاق جوایز  100⛄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'holespacewhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_holespacewhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت سیاه چاله 250 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'fetishwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_fetishwhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت طلسم 150❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'mutewhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_mutewhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت انجماد 40 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'spwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_spwhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت سپر 100 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'thiefwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_thiefwhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت دزد 290 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'deletechat':
                kharid_button = Button.inline('خرید 💸',b'kharid_deletechat')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید قدرت دیلیت چت 15❄️  از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'emperorwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_emperor')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام امپراطور 30 ⛄️  از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'smartwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_smartwhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام لند اسمارت 15 ⛄️  از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'tacticianwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_tactician')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام سالار 50❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'herowhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_herow')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام قهرمان 20 ⛄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'kinghtwite':
                kharid_button = Button.inline('خرید 💸',b'kharid_knight')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام شوالیه 10 ⛄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'warlordwhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_warlord')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام سردار  5 ⛄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'whiteone':
                kharid_button = Button.inline('خرید 💸',b'kharid_whiteone')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام لند اولی 10 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'mafiawhite':
                kharid_button = Button.inline('خرید 💸',b'kharid_mafiawhite_mgham')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام مافیای لند🧟‍♀️ ، 50⛄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'whiteplayer':
                kharid_button = Button.inline('خرید 💸',b'kharid_soldier')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('جهت خرید مقام بان 7 ❄️ از شما کسر خواهد شد',buttons=[[kharid_button],[back_click]])
            elif event.data == b'backclick':
                k1 = Button.inline('👑خرید مقام👨🏻‍💻', b'sell_magham')
                k2 = Button.inline('⚡️خرید قدرت 💪', b'sell_ghodrat')       
                k3 = Button.url('راهنما🧐',b'https://t.me/White_Channel/1283')
                k4 = Button.url('کانال ارتباطی ما', b't.me/baron')
                k5 = Button.inline('ثبت اطلاعات شخصی🙋🏻‍♂️',b'sabtetlaat')
                k6 = Button.inline('اتاق جوایز 🗃',b'roomwardbot')
                k7 = Button.inline('🎰شرط بندی💸',b'bet_wolf')
                k8 = Button.inline('❄️⟺⛄️',b'tabdilmony')
                k9 = Button.inline('🛡 شیلد ⏱',b'shildwhite')
                await event.edit('ربات چالش لند جهت خرید مقام و قدرت و یا راهنما کلیک کنید',buttons=[[k1,k2],[k3],[k5],[k6],[k7],[k8],[k4]])         
            elif event.data == b'shoarmember':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_kinghtwhite'] == 1:
                    await event.reply('شعار خود را ثبت کنید\nمثال : شعار باروڼ یعنـۍ صداــے احـ‌سـ‌اس')
                    redis.set(str(event.sender_id)+'motto',1)
                    @bot.on(events.NewMessage(pattern=r'شعار'))
                    async def test(event):  
                        try:
                            if int(redis.get(str(event.sender_id)+'motto').decode('utf-8')) == 1:
                                message = event.text.strip('شعار')
                                if len(message) < 125:
                                    redis.set(str(event.sender_id)+'motto',0)
                                    list_m = eval(redis.get(event.sender_id).decode('utf-8'))
                                    print(list_m)
                                    list_m['motto'] = message
                                    redis.set(event.sender_id,str(list_m))
                                    print('ok')
                                    await event.reply('شعار ثبت شد')
                                    k1 = Button.inline('👑خرید مقام👨🏻‍💻', b'sell_magham')
                                    k2 = Button.inline('⚡️خرید قدرت 💪', b'sell_ghodrat')       
                                    k3 = Button.url('راهنما🧐',b'https://t.me/White_Channel/1283')
                                    k4 = Button.url('کانال ارتباطی ما', b't.me/baron')
                                    k5 = Button.inline('ثبت اطلاعات شخصی🙋🏻‍♂️',b'sabtetlaat')
                                    await bot.send_message(event.sender_id,'ربات چالش لند جهت خرید مقام و قدرت و یا راهنما کلیک کنید',buttons=[[k1,k2],[k3],[k5],[k4]])
                                    
                                else:
                                    await event.answer('شعار باید کمتر از 125 کاراکتر باشه',alert=True)
                                    #await bot.send_message(event.sender_id,'شعار باید کمتر از 125 کاراکتر باشه')
                        except Exception as e:
                            print(e)
                else:
                    await event.answer('شما اول باید مقام شوالیه رو بگیرید',alert=True)
                    #await event.edit('شما اول باید مقام شوالیه رو بگیرید')
                    await menu_start(event.sender_id)   
            elif event.data == b'titlemember':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_warlordwhite'] == 1:
                    await event.reply('لقب خود را ثبت کنید به این صورت \nمثال : لقب پسر مرده')
                    redis.set(str(event.sender_id)+'dubbed',1)
                    @bot.on(events.NewMessage(pattern=r'لقب'))
                    async def test(event):  
                        try:
                            if int(redis.get(str(event.sender_id)+'dubbed').decode('utf-8')) == 1:
                                message = event.text.strip('لقب')
                                if len(message) < 15:
                                    redis.set(str(event.sender_id)+'dubbed',0)
                                    list_m = eval(redis.get(event.sender_id).decode('utf-8'))
                                    print(list_m)
                                    list_m['dubbed'] = message
                                    redis.set(event.sender_id,str(list_m))
                                    print('ok')
                                    await event.reply('لقب ثبت شد')
                                    k1 = Button.inline('👑خرید مقام👨🏻‍💻', b'sell_magham')
                                    k2 = Button.inline('⚡️خرید قدرت 💪', b'sell_ghodrat')       
                                    k3 = Button.url('راهنما🧐',b'https://t.me/White_Channel/1283')
                                    k4 = Button.url('کانال ارتباطی ما', b't.me/baron')
                                    k5 = Button.inline('ثبت اطلاعات شخصی🙋🏻‍♂️',b'sabtetlaat')
                                    await bot.send_message(event.sender_id,'ربات چالش لند جهت خرید مقام و قدرت و یا راهنما کلیک کنید',buttons=[[k1,k2],[k3],[k5],[k4]])  
                                else:
                                    await event.answer('لقب باید کمتر از 15 کاراکتر باشه',alert=True)
                                    #await bot.send_message(event.sender_id,'لقب باید کمتر از 15 کاراکتر باشه')
                        except Exception as e:
                            print(e)
                else:
                    await event.answer('شما اول باید مقام سردار رو بگیرید',alert=True)
                    #await event.edit('شما اول باید مقام سردار رو بگیرید')
                    await menu_start(event.sender_id)  
            elif event.data == b'dateofbirthmember':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_whiteone'] == 1:
                    await event.reply('🎊تاریخ تولد خود را ارسال کنید.\n📌مثال : تاریخ تولد 1375/05/12')
                    redis.set(str(event.sender_id)+'data_of',1)
                    @bot.on(events.NewMessage(pattern=r'تاریخ تولد'))
                    async def test(event):  
                        try:
                            if int(redis.get(str(event.sender_id)+'data_of').decode('utf-8')) == 1:
                                if '/' in event.text:
                                    redis.set(str(event.sender_id)+'data_of',0)
                                    message = event.text.split(' ')
                                    print(message,message[1],message[2])
                                    list_m = eval(redis.get(event.sender_id).decode('utf-8'))
                                    print(list_m)
                                    list_m['dateofbirth'] = message[2]
                                    redis.set(event.sender_id,str(list_m))
                                    print('ok')
                                    await event.reply('تاریخ تولد ثبت شد')
                                    k1 = Button.inline('👑خرید مقام👨🏻‍💻', b'sell_magham')
                                    k2 = Button.inline('⚡️خرید قدرت 💪', b'sell_ghodrat')       
                                    k3 = Button.url('راهنما🧐',b'https://t.me/White_Channel/1283')
                                    k4 = Button.url('کانال ارتباطی ما', b't.me/baron')
                                    k5 = Button.inline('ثبت اطلاعات شخصی🙋🏻‍♂️',b'sabtetlaat')
                                    await bot.send_message(event.sender_id,'ربات چالش لند جهت خرید مقام و قدرت و یا راهنما کلیک کنید',buttons=[[k1,k2],[k3],[k5],[k4]])
                                else:
                                    await event.answer('لطفا درست تاریخ تولد خود را وارد نمایید',alert=True)
                        except Exception as e:
                            print(e)
                else:
                    await event.answer('شما اول باید مقام لند اولی رو بگیرید',alert=True)
                    await menu_start(event.sender_id)    
            elif event.data == b'hashtagmember':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_whiteone'] == 1:
                    await event.reply('📌جهت ساخت هشتگـ# اختصاصی دستور زیر را بر روی متن مورد نظر\nریپلی کنید ...\n🎞| /sh #اسم_هشتگ')
                else:
                    await event.answer('شما اول باید به مقام لند اولی دست پیدا کنید',alert=True)
                    await menu_start(event.sender_id)
            elif event.data == b'sabtetlaat':
                k1 = Button.inline('💃🏻تاریخ تولد🕺🏻',b'dateofbirthmember')
                k2 = Button.inline('🦹🏻‍♀️لقب🦹🏻‍♂️',b'titlemember')
                k3 = Button.inline('#️⃣هشتگ اختصاصی#️⃣',b'hashtagmember')
                k4 = Button.inline('شعار📌',b'shoarmember')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('👩🏻‍💻ثبت هشتگ و تاریخ تولد لقب مورد نظر خود👨🏻‍💻',buttons=[[k1],[k2,k3],[k4],[back_click]])
            elif event.data == b'sell_magham':
                k1 = Button.inline('🧑🏼لند اولی',b'whiteone')
                k2 = Button.inline('👨🏻‍✈سردار لند',b'warlordwhite')
                k3 = Button.inline('⚔️شوالیه لند',b'kinghtwite')
                k4 = Button.inline('🧛🏻‍♂لند اسمارت',b'smartwhite')
                k5 = Button.inline('🦸🏻‍♂️ قهرمان لند',b'herowhite')
                k6 = Button.inline('🤴🏻امپراطور لند',b'emperorwhite')
                k7 = Button.inline('مافیای لند🧟‍♀️',b'mafiawhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('خرید مقام های موجود 🧙🏼‍♀️',buttons=[[k1],[k2,k3],[k4],[k5,k6],[k7],[back_click]]) 
            elif event.data == b'kharid_mafiawhite':
                try:
                    start_time = time.time()
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    try:
                        get_time_m = list_m['time_ekhtlas_sell'][0]
                        get_time_m = start_time - get_time_m
                        get_time_m = round(get_time_m / 60)
                        if get_time_m >= 7199:
                            if list_m['place_mafiawhite'] == 1:
                                if list_m['snowman'] >= 10:
                                    try:
                                        if list_m['powers_ektlas'][0] == 0:
                                            list_powers = list_m['powers']
                                            list_powers.append('اختلاس💰')
                                            list_m['powers'] = list_powers
                                        list_m['powers_ektlas'][0] = 1
                                        list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] + 3
                                        list_m['snowman'] = list_m['snowman'] - 10
                                        list_m['time_ekhtlas_sell'][0] = time.time()
                                        redis.set(event.sender_id,str(list_m))
                                        await event.edit('🖇قابلیت : یکبار به صورت رندوم از 15 الی 20 ادم‌برفیـ⛄️ از هر شخصی اختلاص کنه. \n\n🖇دستور : بخوابونش')
                                        await menu_start(event.sender_id)
                                    except Exception as e:
                                        print(e)
                                else :
                                    await event.answer('موجودی آدم⛄️برفی شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                    await menu_start(event.sender_id)
                            else:
                                await event.answer('شما اول باید مقام مافیا رو فعال کنید',alert=True)
                                #await event.edit('شما اول باید مقام اسمارت را فعال کنید')
                                await menu_start(event.sender_id)
                        else:
                            try:
                                await event.reply('شما قبلا قدرت را در 120 ساعت گذشته خریداری کردید و لطفا {0}  دقیقه دیگر برای خرید اقدام کنید'.format(7199 - int(get_time_m)))
                            except Exception as e:
                                print(e)
                    except Exception as e:
                        print(e)
                        list_m['time_ekhtlas_sell'][0] = [time.time(),0]
                        if list_m['place_mafiawhite'] == 1:
                            if list_m['snowman'] >= 10:
                                try:
                                    if list_m['powers_ektlas'][0] == 0:
                                        list_powers = list_m['powers']
                                        list_powers.append('اختلاس💰')
                                        list_m['powers'] = list_powers
                                    list_m['powers_ektlas'][0] = 1
                                    list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] + 3
                                    list_m['snowman'] = list_m['snowman'] - 10
                                    list_m['time_ekhtlas_sell'][0] = time.time()
                                    redis.set(event.sender_id,str(list_m))
                                    await event.edit('🖇قابلیت : یکبار به صورت رندوم از 15 الی 20 ادم‌برفیـ⛄️ از هر شخصی اختلاص کنه. \n\n🖇دستور : بخوابونش')
                                    await menu_start(event.sender_id)
                                except Exception as e:
                                    print(e)
                            else :
                                await event.answer('موجودی آدم⛄️برفی شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما اول باید مقام مافیا رو فعال کنید',alert=True)
                            #await event.edit('شما اول باید مقام اسمارت را فعال کنید')
                            await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_mafiawhite_mgham':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_mafiawhite'] == 0:
                        if list_m['place_theemperor'] == 1:
                            if list_m['snowman'] >= 50:
                                list_m['place_mafiawhite'] = 1
                                list_m['place'] = 'مافیای لند🧟'
                                list_m['snowman'] = list_m['snowman'] - 50
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام مافیای لند رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                #await event.edit('شما با موفقیت مقام 🤴🏻امپراطور لند را خریدید✔️')
                                await event.answer('شما با موفقیت مقام  مافیای لند🧟 را خریدید✔️',alert=True)
                                await menu_start(event.sender_id) 
                            else :
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما مقام امپراطور لند را هنوز خریداری نکردید',alert=True)
                            #await event.edit('شما مقام قهرمان لند را هنوز خریداری نکردید')
                            await menu_start(event.sender_id)
                    else:
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        #await event.edit('شما از قبل مقام را خریداری کردید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_emperor':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_theemperor'] == 0:
                        if list_m['place_herowhite'] == 1:
                            if list_m['snowman'] >= 30:
                                list_m['place_theemperor'] = 1
                                list_m['place'] = '🤴🏻امپراطور لند'
                                list_m['snowman'] = list_m['snowman'] - 30
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام امپراطور لند رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                #await event.edit('شما با موفقیت مقام 🤴🏻امپراطور لند را خریدید✔️')
                                await event.answer('شما با موفقیت مقام 🤴🏻امپراطور لند را خریدید✔️',alert=True)
                                await menu_start(event.sender_id) 
                            else :
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما مقام قهرمان لند را هنوز خریداری نکردید',alert=True)
                            #await event.edit('شما مقام قهرمان لند را هنوز خریداری نکردید')
                            await menu_start(event.sender_id)
                    else:
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        #await event.edit('شما از قبل مقام را خریداری کردید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_herow':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_herowhite'] == 0:
                        if list_m['place_smartwhite'] == 1:
                            if list_m['snowman'] >= 20:
                                list_m['place_herowhite'] = 1
                                list_m['place'] = '🦸🏻‍♂️قهرمان لند'
                                list_m['snowman'] = list_m['snowman'] - 20
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام قهرمان لند رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.answer('شما با موفقیت مقام 🦸🏻‍♂️قهرمان لند را خریدید✔️',alert=True)
                                await menu_start(event.sender_id)
                            else :
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما مقام لند اسمارت را هنوز خریداری نکردید',alert=True)
                            await menu_start(event.sender_id)
                    else:
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_smartwhite':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_smartwhite'] == 0:
                        if list_m['place_kinghtwhite'] == 1:
                            if list_m['snowman'] >= 15:
                                list_m['place_smartwhite'] = 1
                                list_m['place'] = '🧛🏻‍♂لند اسمارت'
                                list_m['snowman'] = list_m['snowman'] - 15
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام لند اسمارت رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                #await event.edit('شما با موفقیت مقام ⚔️لند اسمارت را خریدید✔️')
                                await event.answer('شما با موفقیت مقام ⚔️لند اسمارت را خریدید✔️',alert=True)
                                await menu_start(event.sender_id) 
                            else :
                                #await event.edit('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁')
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                await menu_start(event.sender_id)
                        else:
                            #await event.edit('شما مقام شوالیه لند را هنوز خریداری نکردید')
                            await event.answer('شما مقام شوالیه لند را هنوز خریداری نکردید',alert=True)
                            await menu_start(event.sender_id)
                    else:
                        #await event.edit('شما از قبل مقام را خریداری کردید')
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_knight':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_kinghtwhite'] == 0:
                        if list_m['place_warlordwhite'] == 1:
                            if list_m['snowman'] >= 10:
                                list_m['place_kinghtwhite'] = 1
                                list_m['place'] = '⚔️شوالیه لند'
                                list_m['snowman'] = list_m['snowman'] - 10
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام شوالیه لند رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                #await event.edit('شما با موفقیت مقام ⚔️شوالیه لند را خریدید✔️')
                                await event.answer('شما با موفقیت مقام ⚔️شوالیه لند را خریدید✔️',alert=True)
                                await menu_start(event.sender_id) 
                            else :
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما مقام سردار لند را هنوز خریداری نکردید',alert=True)
                            #await event.edit('شما مقام سردار لند را هنوز خریداری نکردید')
                            await menu_start(event.sender_id)
                    else:
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        #await event.edit('شما از قبل مقام را خریداری کردید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_warlord':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_warlordwhite'] == 0:
                        if list_m['place_whiteone'] == 1:
                            if list_m['snowman'] >= 5:
                                list_m['place_warlordwhite'] = 1
                                list_m['place'] = '👨🏻‍✈سردار لند'
                                list_m['snowman'] = list_m['snowman'] - 5
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام سردار لند رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                #await event.edit('شما با موفقیت مقام 👨🏻‍✈️سردار لند را خریدید✔️')
                                await event.answer('شما با موفقیت مقام 👨🏻‍✈️سردار لند را خریدید✔️',alert=True)
                                await menu_start(event.sender_id) 
                            else :
                                await event.answer('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی آدم برفیـ☃️  شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما مقام لند اولی را هنوز خریداری نکردید',alert=True)
                            #await event.edit('شما مقام لند اولی را هنوز خریداری نکردید')
                            await menu_start(event.sender_id)
                    else:
                        await event.edit('شما از قبل مقام را خریداری کردید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_whiteone':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_whiteone'] == 0:
                        if list_m['place_whiteplayer'] == 1:
                            if list_m['snow'] >= 10:
                                list_m['place_whiteone'] = 1
                                list_m['place'] = '🧑🏼لند اولی'
                                list_m['snow'] = list_m['snow'] - 10
                                redis.set(event.sender_id,str(list_m))
                                entity_m = await bot.get_entity(event.sender_id)
                                await bot.send_message(int(list_m['group']),'کاربر   {0}   مقام لند اولی رو خریداری کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.edit('شما با موفقیت مقام 🧑🏼لند اولی را خریدید✔️')
                                await menu_start(event.sender_id)
                            else :
                                await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما در گروه لند ولف ثبت نام نکردید لطفا ابتدا ثبت نام کنید🙋🏻‍♂️',alert=True)
                            #await event.edit('شما در گروه لند ولف ثبت نام نکردید لطفا ابتدا ثبت نام کنید🙋🏻‍♂️')
                            await menu_start(event.sender_id)
                    else:
                        await event.answer('شما از قبل مقام را خریداری کردید',alert=True)
                        #await event.edit('شما از قبل مقام را خریداری کردید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_deletechat':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_warlordwhite'] == 1:
                    if list_m['snow'] >= 15:
                        try:
                            print(list_m['powers'])
                            if list_m['powers_delete'][0] == 0:
                                list_powers = list_m['powers']
                                list_powers.append('کلینر(دیلیت چت) 🗯')
                                list_m['powers'] = list_powers
                            try:
                                print(list_m['powers'])
                            except Exception as e:
                                print(e)
                            print(list_m['powers_delete'][0],type(list_m['powers_delete'][0]))
                            list_m['powers_delete'][0] = 1
                            list_m['powers_delete'][1] = list_m['powers_delete'][1] + 3
                            list_m['snow'] = list_m['snow'] - 15
                            redis.set(event.sender_id,str(list_m))
                            await event.edit('📮قدرت کلینر(🗯) با موفقیت خریداری شد\n🖇قابلیت : ۳ بار پاک کردن پیام دلخواه\n📎دستور : دیلیت')
                            await menu_start(event.sender_id)
                        except Exception as e:
                            print(e)
                    else :
                        await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                        #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                        await menu_start(event.sender_id)
                else:
                    await event.answer('شما اول باید مقام سردار را فعال کنید',alert=True)
                    #await event.edit('شما اول باید مقام سردار را فعال کنید')
                    await menu_start(event.sender_id)
            elif event.data == b'kharid_thiefwhite':
                try:
                    start_time = time.time()
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    try:
                        get_time_m = list_m['time_hnif_sell'][0]
                        get_time_m = start_time - get_time_m
                        get_time_m = round(get_time_m / 60)
                        if get_time_m >= 2880:
                            if list_m['place_smartwhite'] == 1:
                                if list_m['snow'] >= 290:
                                    try:
                                        if list_m['powers_hnif'][0] == 0:
                                            list_powers = list_m['powers']
                                            list_powers.append('برف ربا🤡')
                                            list_m['powers'] = list_powers
                                        list_m['powers_hnif'][0] = 1
                                        list_m['powers_hnif'][1] = list_m['powers_hnif'][1] + 3
                                        list_m['snow'] = list_m['snow'] - 290
                                        list_m['time_hnif_sell'][0] = time.time()
                                        redis.set(event.sender_id,str(list_m))
                                        await event.edit('🖇قابلیت : یکبار به صورت رندوم از 100 الی 200 برفـ❄️ از هر شخصی بدزده. \n🖇دستور : خفتش کن')
                                        await menu_start(event.sender_id)
                                    except Exception as e:
                                        print(e)
                                else :
                                    await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                    await menu_start(event.sender_id)
                            else:
                                await event.answer('شما اول باید مقام اسمارت را فعال کنید',alert=True)
                                #await event.edit('شما اول باید مقام اسمارت را فعال کنید')
                                await menu_start(event.sender_id)
                        else:
                            print('test')
                            try:
                                await event.reply('شما قبلا قدرت را در 48 ساعت گذشته خریداری کردید و لطفا {0}  دقیقه دیگر برای خرید اقدام کنید'.format(2880 - int(get_time_m)))
                            except Exception as e:
                                print(e)
                    except Exception as e:
                        print(e)
                        list_m['time_hnif_sell'] = [time.time(),0]
                        if list_m['place_smartwhite'] == 1:
                            if list_m['snow'] >= 290:
                                try:
                                    if list_m['powers_hnif'][0] == 0:
                                        list_powers = list_m['powers']
                                        list_powers.append('برف ربا🤡')
                                        list_m['powers'] = list_powers
                                    list_m['powers_hnif'][0] = 1
                                    list_m['powers_hnif'][1] = list_m['powers_hnif'][1] + 3
                                    list_m['snow'] = list_m['snow'] - 290
                                    list_m['time_hnif_sell'][0] = time.time()
                                    redis.set(event.sender_id,str(list_m))
                                    await event.edit('🖇قابلیت : یکبار به صورت رندوم از 100 الی 200 برفـ❄️ از هر شخصی بدزده. \n🖇دستور : خفتش کن')
                                    await menu_start(event.sender_id)
                                except Exception as e:
                                    print(e)
                            else :
                                await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                                #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                                await menu_start(event.sender_id)
                        else:
                            await event.answer('شما اول باید مقام اسمارت را فعال کنید',alert=True)
                            #await event.edit('شما اول باید مقام اسمارت را فعال کنید')
                            await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'kharid_fetishwhite':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_herowhite'] == 1:
                    if list_m['snow'] >= 150:
                        try:
                            if list_m['powers_hipno'][0] == 0:
                                list_powers = list_m['powers']
                                list_powers.append('طلسم🃏')
                                list_m['powers'] = list_powers
                            list_m['powers_hipno'][0] = 1
                            list_m['powers_hipno'][1] = list_m['powers_hipno'][1] + 3
                            list_m['snow'] = list_m['snow'] - 150
                            redis.set(event.sender_id,str(list_m))
                            await event.edit('💫قدرت (طلسم🃏) با موفقیت خریداری شد ✅\n🖇قابلیت : شخص دارنده این قدرت میتونه افراد دارای قدرت های دیگه رو\nکاری کنه که قدرتشون بک بخوره و روی خودشون اجرا شه')
                            await menu_start(event.sender_id)
                        except Exception as e:
                            print(e)
                    else :
                        #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                        await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                        await menu_start(event.sender_id)
                else:
                    await event.answer('شما اول باید مقام قهرمان را فعال کنید',alert=True)
                    #await event.edit('شما اول باید مقام قهرمان را فعال کنید')
                    await menu_start(event.sender_id)
            elif event.data == b'kharid_mutewhite':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_kinghtwhite'] == 1:
                    if list_m['snow'] >= 40:
                        try:
                            if list_m['powers_mute'][0] == 0:
                                list_powers = list_m['powers']
                                list_powers.append('انجماد🌬')
                                list_m['powers'] = list_powers
                            list_m['powers_mute'][0] = 1
                            list_m['powers_mute'][1] = list_m['powers_mute'][1] + 3
                            list_m['snow'] = list_m['snow'] - 40
                            redis.set(event.sender_id,str(list_m))
                            await event.edit('💫قدرت (انجماد🌬) با موفقیت خریداری شد ✅\n🖇قابلیت : میوت کردن هر شخص حتی ادمین به مدت 2 دقیقه \n🖇دستور : فریز')
                            await menu_start(event.sender_id)
                        except Exception as e:
                            print(e)
                    else :
                        await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                        await menu_start(event.sender_id)
                else:
                    await event.answer('شما اول باید مقام شوالیه رو فعال کنید',alert=True)
                    #await event.edit('شما اول باید مقام شوالیه رو فعال کنید')
                    await menu_start(event.sender_id)
            elif event.data == b'kharid_holespacewhite':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_theemperor'] == 1:
                    if list_m['snow'] >= 250:
                        try:
                            if list_m['powers_chalefazaii'][0] == 0:
                                list_powers = list_m['powers']
                                list_powers.append('سیاه چاله🎇')
                                list_m['powers'] = list_powers
                            list_m['powers_chalefazaii'][0] = 1
                            list_m['powers_chalefazaii'][1] = list_m['powers_chalefazaii'][1] + 2
                            list_m['snow'] = list_m['snow'] - 250
                            redis.set(event.sender_id,str(list_m))
                            await event.edit('💫قدرت (سیاه چاله🎇) با موفقیت خریداری شد ✅\n🖇 قابلیت :توانایی نابودی حداکثر دو قدرت از قدرت های هر شخص ( هر قدرتی به جز دزد❌)\n🖇دستور :نابودش کن')
                            await menu_start(event.sender_id)
                        except Exception as e:
                            print(e)
                    else :
                        await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                        #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                        await menu_start(event.sender_id)
                else:
                    await event.answer('شما اول باید مقام امپراطور را فعال کنید',alert=True)
                    #await event.edit('شما اول باید مقام امپراطور را فعال کنید')
                    await menu_start(event.sender_id)
            elif event.data == b'kharid_spwhite':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_smartwhite'] == 1:
                    if list_m['snow'] >= 100:
                        try:
                            if list_m['powers_spar'][0] == 0:
                                list_powers = list_m['powers']
                                list_powers.append('سپر اتشین 🔥')
                                list_m['powers'] = list_powers
                            list_m['powers_spar'][0] = 1
                            list_m['powers_spar'][1] = list_m['powers_spar'][1] + 3
                            list_m['snow'] = list_m['snow'] - 100
                            redis.set(event.sender_id,str(list_m))
                            await event.edit('💫قدرت (سپر آتشین🔥) با موفقیت خریداری شد ✅\n🖇قابلیت : مقاومت شخص دارنده در مقابل انجماد و کلینر.')
                            await menu_start(event.sender_id)
                        except Exception as e:
                            print(e)
                    else :
                        await event.answer('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁',alert=True)
                        #await event.edit('موجودی برفـ❄️ شما برای خرید 🛍کافی نیستـ🙁')
                        await menu_start(event.sender_id)
                else:
                    await event.answer('شما اول باید مقام اسمارت را فعال کنید',alert=True)
                    #await event.edit('شما اول باید مقام اسمارت را فعال کنید')
                    await menu_start(event.sender_id)
            elif event.data == b'sell_ghodrat':
                k1 = Button.inline('کلینر(دیلیت چت) 🗯',b'deletechat')
                k2 = Button.inline('برف ربا 🤡',b'thiefwhite')
                k3 = Button.inline('سپر اتشین 🔥',b'spwhite')
                k4 = Button.inline(' انجماد🌬️',b'mutewhite')
                k5 = Button.inline('طلسم🃏',b'fetishwhite')
                k6 = Button.inline('سیاه چاله🎇',b'holespacewhite')
                k7 = Button.inline('اختلاس💰',b'ekhtlaswhite')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('🧟‍♀️خرید قدرت های موجود🧟‍♂️',buttons=[[k1],[k2,k3],[k4],[k5,k6],[k7],[back_click]])
            elif event.data == b'help_game ':
                await bot.send_message(event.chat_id,'')
            elif event.data == b'start_one':
                await menu_start(event.sender_id)
            elif event.data == b'tabdilmony':
                try:
                    k1 = Button.inline('❄️⟼⛄️',b'snowtosnowman')
                    k2 = Button.inline('⛄️⟼❄️',b'snowmantownow')
                    back_click = Button.inline('⬅️برگشت',b'backclick')
                    await bot.send_message(event.sender_id,'➰گزینه مورد نظر خود را انتخاب کنید',buttons=[[k1,k2],[back_click]])
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_whiteone'] == 1:
                        print('')
                    else:
                        await event.answer('شما اول باید مقام لند اولی رو بگیرید',alert=True)
                        #await event.reply('شما اول باید مقام لند اولی رو بگیرید')
                        await menu_start(event.sender_id)
                except Exception as e:
                    print(e)
            elif event.data == b'snowtosnowman':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_whiteone'] == 1:
                    k1 = Button.inline('40❄️','snow_to_snowman:40:{0}'.format(event.sender_id))
                    k2 = Button.inline('80❄️','snow_to_snowman:80:{0}'.format(event.sender_id))
                    k3 = Button.inline('120❄️','snow_to_snowman:120:{0}'.format(event.sender_id))
                    k4 = Button.inline('160❄️','snow_to_snowman:160:{0}'.format(event.sender_id))
                    k5 = Button.inline('200❄️','snow_to_snowman:200:{0}'.format(event.sender_id))
                    k6 = Button.inline('240❄️','snow_to_snowman:240:{0}'.format(event.sender_id))
                    k7 = Button.inline('280❄️','snow_to_snowman:280:{0}'.format(event.sender_id))
                    k8 = Button.inline('320❄️','snow_to_snowman:320:{0}'.format(event.sender_id))
                    k9 = Button.inline('360❄️','snow_to_snowman:360:{0}'.format(event.sender_id))
                    k10 = Button.inline('400❄️','snow_to_snowman:400:{0}'.format(event.sender_id))
                    back_click = Button.inline('⬅️برگشت',b'backclick')
                    await event.edit('🖇تعداد برف موردنظر خود را برای تبدیل به ادم برفی انتخاب کنید',buttons=[[k1,k2],[k3,k4],[k5,k6],[k7,k8],[k9,k10],[back_click]])
            elif 'snow_to_snowman' in event.data.decode('utf-8'):
                try:
                    message = event.data.decode('utf-8').split(':')
                except Exception as e:
                    print(e)
                    message = event.data.split(':')
                if message[1] == '40':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),1)
                    except Exception as e:
                        print(e)
                elif message[1] == '80':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),2)
                    except Exception as e:
                        print(e)
                elif message[1] == '120':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),3)
                    except Exception as e:
                        print(e)
                elif message[1] == '160':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),4)
                    except Exception as e:
                        print(e)
                elif message[1] == '200':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),5)
                    except Exception as e:
                        print(e)
                elif message[1] == '240':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),6)
                    except Exception as e:
                        print(e)
                elif message[1] == '280':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),7)
                    except Exception as e:
                        print(e)
                elif message[1] == '320':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),8)
                    except Exception as e:
                        print(e)
                elif message[1] == '360':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),9)
                    except Exception as e:
                        print(e)
                elif message[1] == '400':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snow','snowman',int(message[1]),10)
                    except Exception as e:
                        print(e)
            elif event.data == b'snowmantownow':
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                if list_m['place_whiteone'] == 1:
                    k1 = Button.inline('1⛄️','snowman_to_snow:1:{0}'.format(event.sender_id))
                    k2 = Button.inline('2⛄️','snowman_to_snow:2:{0}'.format(event.sender_id))
                    k3 = Button.inline('3⛄️','snowman_to_snow:3:{0}'.format(event.sender_id))
                    k4 = Button.inline('4⛄️','snowman_to_snow:4:{0}'.format(event.sender_id))
                    k5 = Button.inline('5⛄️','snowman_to_snow:5:{0}'.format(event.sender_id))
                    k6 = Button.inline('6⛄️','snowman_to_snow:6:{0}'.format(event.sender_id))
                    k7 = Button.inline('7⛄️','snowman_to_snow:7:{0}'.format(event.sender_id))
                    k8 = Button.inline('8⛄️','snowman_to_snow:8:{0}'.format(event.sender_id))
                    k9 = Button.inline('9⛄️','snowman_to_snow:9:{0}'.format(event.sender_id))
                    k10 = Button.inline('️10⛄️','snowman_to_snow:400:{0}'.format(event.sender_id))
                    back_click = Button.inline('⬅️برگشت',b'backclick')
                    await event.edit('🖇تعداد برف موردنظر خود را برای تبدیل به ادم برفی انتخاب کنید',buttons=[[k1,k2],[k3,k4],[k5,k6],[k7,k8],[k9,k10],[back_click]])
            elif 'snowman_to_snow' in event.data.decode('utf-8'):
                try:
                    message = event.data.decode('utf-8').split(':')
                except Exception as e:
                    print(e)
                    message = event.data.split(':')
                if message[1] == '1':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),40)
                    except Exception as e:
                        print(e)
                elif message[1] == '2':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),80)
                    except Exception as e:
                        print(e)
                elif message[1] == '3':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),120)
                    except Exception as e:
                        print(e)
                elif message[1] == '4':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),160)
                    except Exception as e:
                        print(e)
                elif message[1] == '5':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),200)
                    except Exception as e:
                        print(e)
                elif message[1] == '6':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),240)
                    except Exception as e:
                        print(e)
                elif message[1] == '7':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),280)
                    except Exception as e:
                        print(e)
                elif message[1] == '8':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),320)
                    except Exception as e:
                        print(e)
                elif message[1] == '9':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),360)
                    except Exception as e:
                        print(e)
                elif message[1] == '10':
                    try:
                        await mainsnow(int(message[2]),event.sender_id,'تبدیل با موفقیت انجام شد✔️','snowman','snow',int(message[1]),400)
                    except Exception as e:
                        print(e)
            elif event.data == b'win_ros':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'ros')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_wolf':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'gorg')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_fire':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'atish')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_thecult':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'ferghe')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_hypocrites':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'monafegh')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_killer':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'ghatel')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'win_lorie':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'atish')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'lose_all':
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bet_button(event.sender_id,'lose')
                else:
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'bet_wolf':
                bet = redis.get('bet_white_ice')
                bet = eval(bet.decode('utf-8'))
                k1 = Button.inline('👨روستا [ضریب {0}]'.format(bet['ros']), b'win_ros')
                k2 = Button.inline('👤فرقه [ضریب {0}]'.format(bet['ferghe']), b'win_thecult')
                k3 = Button.inline('🐺گرگ[ضریب {0}]'.format(bet['gorg']), b'win_wolf')
                k4 = Button.inline('🔪 قاتل‌زنجیره‌ای [ضریب {0}]'.format(bet['ghatel']), b'win_killer')
                k5 = Button.inline('🔥آتش‌زن[ضریب {0}]'.format(bet['atish']), b'win_fire')
                k6 = Button.inline('👺منافق[ضریب {0}]'.format(bet['monafegh']), b'win_hypocrites')
                k7 = Button.inline('💕لاورها[ضریب {0}]'.format(bet['lover']), b'win_lorie')
                k8 = Button.inline('☠️همه میبازن![ضریب {0}]'.format(bet['lose']), b'lose_all')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                check = redis.get('bet_white_check')
                check = check.decode('utf-8')
                if check == 'on':
                    await bot.send_message(event.sender_id,'به به پرو پلیرمون 😌\nاومدی که امروز رو به روز شانست تبدیل کنی🥳\nببینم میتونی برفاتو چند برابر کنی 😈💪🏻\n\nخب خب.!! رو برد کدوم تیم شرط میبندی🧐!؟',buttons=[[k1],[k2],[k3],[k4],[k5],[k6],[k7],[k8],[back_click]])
                else:     
                    await bot.send_message(event.sender_id,'با عرض پوزش شرط بندی غیر فعال شده')
                    await menu_start(event.sender_id)
            elif event.data == b'shildwhite':
                k1 = Button.inline('12 ⏱ 4⛄️',b'shild12')
                k2 = Button.inline('24 ⏱ 8⛄️',b'shild24')
                k3 = Button.inline('36 ⏱ 15⛄️',b'shild36')
                k4 = Button.inline('48 ⏱ 20⛄️',b'shild48')
                k5 = Button.inline('60 ⏱ 25⛄️',b'shild60')
                k6 = Button.inline('72 ⏱ 32⛄️',b'shild72')
                k7 = Button.inline('🛡',b'time_shild')
                back_click = Button.inline('⬅️برگشت',b'backclick')
                await event.edit('خرید سپر زمانی🛡',buttons=[[k1],[k2,k3],[k4],[k5,k6],[k7],[back_click]])
            elif event.data == b'shild12':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 4:
                        list_m['snowman'] = list_m['snowman'] - 4
                        list_m['time_hnif'][0] = time.time() + 720
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(720),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'shild24':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 8:
                        list_m['snowman'] = list_m['snowman'] - 8
                        list_m['time_hnif'][0] = time.time() + 1440
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(1440),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'shild36':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 15:
                        list_m['snowman'] = list_m['snowman'] - 15
                        list_m['time_hnif'][0] = time.time() + 2160
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(2160),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'shild48':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 20:
                        list_m['snowman'] = list_m['snowman'] - 20
                        list_m['time_hnif'][0] = time.time() + 2880
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(2880),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'shild60':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 25:
                        list_m['snowman'] = list_m['snowman'] - 25
                        list_m['time_hnif'][0] = time.time() +3600
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(3600),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'time_shild':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    text_s = '''مدت زمان باقی مانده از سپر زمانی شما {0}'''
                    await event.answer(text_s.format(list_m['time_hnif'][0]),alert=True)
                except Exception as e:
                    print(e)
            elif event.data == b'shild72':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['snowman'] >= 32:
                        list_m['snowman'] = list_m['snowman'] - 32
                        list_m['time_hnif'][0] = time.time() + 4320
                        redis.set(event.sender_id,str(list_m))
                        text_s = '''شیلد شما به مدت {0}  دقیقه فعال شد'''
                        await event.answer(text_s.format(4320),alert=True)
                    else:
                        await event.answer('شما ادم برفی کافی ندارید',alert=True)
                except Exception as e:
                    print(e)
            print(event.data,event.sender_id)

        @bot.on(events.NewMessage(pattern=r'❄️',func=lambda e: e.is_private))
        async def test(event):
            check_ros = redis.get('{0}check_ros'.format(event.sender_id))
            check_ros = check_ros.decode('utf-8')
            list_m = redis.get(event.sender_id)
            list_m = eval(list_m.decode('utf-8'))
            print(check_ros,type(check_ros))
            try:
                message = event.text.split(' ')
                if 10 > list_m['snow']:
                    if int(message[1]) < 1000:
                        if check_ros == 'ros':
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            try:
                                                s = eval(redis.get('all_bet_member').decode('utf-8'))
                                                s.append(event.sender_id)
                                                redis.set('all_bet_member',str(s))
                                                list_m['snow'] = list_m['snow'] - int(message[1])
                                                if user_bet['bet_one'] == bet['game_number']:
                                                    user_bet['bet_two'] = 'ros:{0}'.format(bet['game_number'] + 1)
                                                else:
                                                    user_bet['bet_two'] = 'ros:{0}'.format(bet['game_number'] + 2)
                                                user_bet['bet_two_snow'] = int(message[1])
                                                user_bet['game'] = 2
                                                redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                                redis.set('{0}check_ros'.format(event.sender_id),'')
                                                redis.set(event.sender_id,str(list_m))
                                                await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد روستــا👨\n❆ ضریب {1} 📊'.format(message[1],bet['ros']))
                                                await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                            except Exception as e:
                                                print(e)
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ros:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد روستــا👨\n❆ ضریب {1} 📊'.format(message[1],bet['ros']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'gorg':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'gorg:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'gorg:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد گـــرگ 🐺\n❆ ضریب {1} 📊'.format(message[1],bet['gorg']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'gorg:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد گـــرگ 🐺\n❆ ضریب {1} 📊'.format(message[1],bet['gorg']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'atish':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'atish:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'atish:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد آتــش زن 🔥\n❆ ضریب {1} 📊'.format(message[1],bet['atish']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'atish:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد آتــش زن 🔥\n❆ ضریب {1} 📊'.format(message[1],bet['atish']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'ferghe':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'ferghe:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'ferghe:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد فـــرقه 👤\n❆ ضریب {1} 📊'.format(message[1],bet['ferghe']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ferghe:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد فـــرقه 👤\n❆ ضریب {1} 📊'.format(message[1],bet['ferghe']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'monafegh':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'monafegh:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'monafegh:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد منافق👺\n❆ ضریب {1} 📊'.format(message[1],bet['monafegh']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'monafegh:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد منافق👺\n❆ ضریب {1} 📊'.format(message[1],bet['monafegh']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'ghatel':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'ghatel:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'ghatel:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('ششرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد قــاتل زنــجیـره ای 🔪\n❆ ضریب {1} 📊'.format(message[1],bet['ghatel']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ghatel:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('ششرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد قــاتل زنــجیـره ای 🔪\n❆ ضریب {1} 📊'.format(message[1],bet['ghatel']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'lover':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_two'] = 'lover:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n❆ {0} برفـــــ❄️\n❆ بـــرد لاورها 💕\n❆ ضریب {1} 📊'.format(message[1],bet['lover']))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'lover:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n❆ {0} برفـــــ❄️\n❆ بـــرد لاورها 💕\n❆ ضریب {1} 📊'.format(message[1],bet['lover']))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'lose':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_two'] = 'lose:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ بــاختن هــمه 💀\n❆ ضریب {1} 📊'.format(message[1],bet['lose']))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'lose:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ بــاختن هــمه 💀\n❆ ضریب {1} 📊'.format(message[1],bet['lose']))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                    
                    else :
                        await event.reply('سقف شرط بندی 999 برف هستش')
                else:
                    if int(message[1]) < 200:
                        if check_ros == 'ros':
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            try:
                                                s = eval(redis.get('all_bet_member').decode('utf-8'))
                                                s.append(event.sender_id)
                                                redis.set('all_bet_member',str(s))
                                                list_m['snow'] = list_m['snow'] - int(message[1])
                                                if user_bet['bet_one'] == bet['game_number']:
                                                    user_bet['bet_two'] = 'ros:{0}'.format(bet['game_number'] + 1)
                                                else:
                                                    user_bet['bet_two'] = 'ros:{0}'.format(bet['game_number'] + 2)
                                                user_bet['bet_two_snow'] = int(message[1])
                                                user_bet['game'] = 2
                                                redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                                redis.set('{0}check_ros'.format(event.sender_id),'')
                                                redis.set(event.sender_id,str(list_m))
                                                await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد روستــا👨\n❆ ضریب {1} 📊'.format(message[1],bet['ros']))
                                                await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                            except Exception as e:
                                                print(e)
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ros:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد روستــا👨\n❆ ضریب {1} 📊'.format(message[1],bet['ros']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'gorg':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'gorg:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'gorg:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد گـــرگ 🐺\n❆ ضریب {1} 📊'.format(message[1],bet['gorg']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'gorg:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد گـــرگ 🐺\n❆ ضریب {1} 📊'.format(message[1],bet['gorg']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'atish':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'atish:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'atish:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد آتــش زن 🔥\n❆ ضریب {1} 📊'.format(message[1],bet['atish']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'atish:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد آتــش زن 🔥\n❆ ضریب {1} 📊'.format(message[1],bet['atish']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'ferghe':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'ferghe:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'ferghe:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد فـــرقه 👤\n❆ ضریب {1} 📊'.format(message[1],bet['ferghe']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ferghe:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد فـــرقه 👤\n❆ ضریب {1} 📊'.format(message[1],bet['ferghe']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'monafegh':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'monafegh:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'monafegh:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد منافق👺\n❆ ضریب {1} 📊'.format(message[1],bet['monafegh']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'monafegh:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد منافق👺\n❆ ضریب {1} 📊'.format(message[1],bet['monafegh']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'ghatel':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            if user_bet['bet_one'] == bet['game_number']:
                                                user_bet['bet_two'] = 'ghatel:{0}'.format(bet['game_number'] + 1)
                                            else:
                                                user_bet['bet_two'] = 'ghatel:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('ششرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد قــاتل زنــجیـره ای 🔪\n❆ ضریب {1} 📊'.format(message[1],bet['ghatel']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_two'],message[1]))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'ghatel:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('ششرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ برد قــاتل زنــجیـره ای 🔪\n❆ ضریب {1} 📊'.format(message[1],bet['ghatel']))
                                            await bot.send_message(-1001393884185,'user {0} \nsetbet game :{1} \nsnow :{2}'.format(event.sender_id,user_bet['bet_one'],message[1]))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'lover':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_two'] = 'lover:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n❆ {0} برفـــــ❄️\n❆ بـــرد لاورها 💕\n❆ ضریب {1} 📊'.format(message[1],bet['lover']))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'lover:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n❆ {0} برفـــــ❄️\n❆ بـــرد لاورها 💕\n❆ ضریب {1} 📊'.format(message[1],bet['lover']))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                        elif check_ros == 'lose':
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            user_bet = redis.get('{0}bet'.format(event.sender_id))
                            user_bet = eval(user_bet.decode('utf-8'))
                            message = event.text.split(' ')
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            if int(message[1]) > 1:
                                if int(message[1]) > 1:
                                #if int(list_m['snow']) > int(message[1]):
                                    print('3',user_bet['bet_two'])
                                    try:
                                        if user_bet['game'] == 1:
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_two'] = 'lose:{0}'.format(bet['game_number'] + 2)
                                            user_bet['bet_two_snow'] = int(message[1])
                                            user_bet['game'] = 2
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ بــاختن هــمه 💀\n❆ ضریب {1} 📊'.format(message[1],bet['lose']))
                                        else :
                                            s = eval(redis.get('all_bet_member').decode('utf-8'))
                                            s.append(event.sender_id)
                                            redis.set('all_bet_member',str(s))
                                            list_m['snow'] = list_m['snow'] - int(message[1])
                                            user_bet['bet_one'] = 'lose:{0}'.format(bet['game_number'] + 1)
                                            user_bet['bet_one_snow'] = int(message[1])
                                            user_bet['bet_two'] = ''
                                            user_bet['bet_two_snow'] = 0
                                            user_bet['game'] = 1
                                            redis.set('{0}bet'.format(event.sender_id),str(user_bet))
                                            redis.set('{0}check_ros'.format(event.sender_id),'')
                                            redis.set(event.sender_id,str(list_m))
                                            await event.reply('شرط بندی شما ثبــ✅ــت شد \n\n❆ {0} برفـــــ❄️\n❆ بــاختن هــمه 💀\n❆ ضریب {1} 📊'.format(message[1],bet['lose']))
                                    except Exception as e:
                                        print(e)
                                else :
                                    redis.set('{0}check_ros'.format(event.sender_id),'')
                                    await event.reply('شما برف کافی ندارید')
                    
                    else :
                        await event.reply('سقف شرط بندی 199 برف هست')
            except Exception as e:
                print(e)
                
        @bot.on(events.NewMessage)
        async def game_rozane(event):
            if event.media.emoticon == '🏀':
                if event.message.fwd_from == None:
                    start_time = time.time()
                    list_m1 = redis.get(event.sender_id)
                    list_m1 = eval(list_m1.decode('utf-8'))
                    try:
                        print(list_m1['chalesh_rozane'])
                        get_time_m = list_m1['chalesh_rozane'][0]
                        get_time_m = start_time - get_time_m
                        get_time_m = round(get_time_m / 60)
                        print(get_time_m)
                        if get_time_m >= 1440:
                            print('1')
                            if event.media.emoticon == '🏀':
                                if int(event.media.value) == 4:
                                    list_m1['snow'] = list_m1['snow'] + 30
                                    list_m1['chalesh_rozane'] = [time.time(),0]
                                    redis.set(event.sender_id,str(list_m1))
                                    entity_m = await bot.get_entity(event.sender_id)
                                    text = 'تبریک !🎈 شما برنده ❄️30 شدید📎'
                                    await asyncio.sleep(4)
                                    await event.reply(text)
                                elif int(event.media.value) == 5:
                                    list_m1['snowman'] = list_m1['snowman'] + 1
                                    list_m1['chalesh_rozane'] = [time.time(),0]
                                    redis.set(event.sender_id,str(list_m1))
                                    entity_m = await bot.get_entity(event.sender_id)
                                    text = 'تبریک ! 🥳 شما برنده ⛄️1 شدید 🖇 '
                                    await asyncio.sleep(4)
                                    await event.reply(text)
                                else:
                                    entity_m = await bot.get_entity(event.sender_id)
                                    text = 'متاسفم عزیزم برنده نشدی :(💔\nفردا امتحان کن :)✨🧷'
                                    list_m1['chalesh_rozane'] = [time.time(),0]
                                    redis.set(event.sender_id,str(list_m1))
                                    await asyncio.sleep(4)
                                    await event.reply(text)
                        else:
                            print(list_m1['time_hnif'][0])
                            times = 1440 - get_time_m
                            times = round(times / 60)
                            print(times)
                            await event.reply('-•امــــروز شانستــو امتحــان کردے فردا بیــا•-')
                    except Exception as e:
                        print(e)
                        print('2')
                        list_m1['chalesh_rozane'] = [time.time(),0]
                        if event.media.emoticon == '🏀':
                            if int(event.media.value) == 4:
                                list_m1['snow'] = list_m1['snow'] + 30
                                redis.set(event.sender_id,str(list_m1))
                                entity_m = await bot.get_entity(event.sender_id)
                                text = 'تبریک !🎈 شما برنده ❄️30 شدید📎'
                                await asyncio.sleep(4)
                                await event.reply(text)
                            elif int(event.media.value) == 5:
                                list_m1['snowman'] = list_m1['snowman'] + 1
                                redis.set(event.sender_id,str(list_m1))
                                entity_m = await bot.get_entity(event.sender_id)
                                text = 'تبریک ! 🥳 شما برنده ⛄️1 شدید 🖇 '
                                await asyncio.sleep(4)
                                await event.reply(text)
                            else:
                                entity_m = await bot.get_entity(event.sender_id)
                                text = 'متاسفم عزیزم برنده نشدی :(💔\nفردا امتحان کن :)✨🧷'
                                redis.set(event.sender_id,str(list_m1))
                                await asyncio.sleep(4)
                                await event.reply(text)

        @bot.on(events.NewMessage)
        async def member_stats2(event):
            try:
                list_m = redis.get(event.sender_id)
                list_m = eval(list_m.decode('utf-8'))
                stats_member = redis.get('stats_white_member')
                if not stats_member == None:
                    try:
                        stats_member = eval(stats_member.decode('utf-8'))
                        if not event.sender_id in stats_member:
                            stats_member.append(event.sender_id)
                            redis.set('stats_white_member',str(stats_member))
                            entity_m = await bot.get_entity(event.sender_id)
                            await bot.send_message('aytola','New Member :\t{0}\nAll Member bot :{1}'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',len(stats_member)))
                    except Exception as e:
                        print(e)
                else:
                    list_member = []
                    redis.set('stats_white_member',str(list_member))
                    await bot.send_message('aytola','data reset {0}'.format(event.chat_id))
                try:
                    check_bet = redis.get('{0}bet'.format(event.sender_id))
                    if check_bet == None:
                        message = event.sender_id
                        bet = {'bet_one':'','bet_one_snow':0,'bet_two':'','bet_two_snow':0,'game':0}
                        redis.set('{0}bet'.format(event.sender_id),str(bet))
                        await bot.send_message('aytola','add user for bet {0}'.format(event.sender_id))
                except Exception as e:
                    print(e)
                if '-100' in str(event.chat_id):
                    task_point = redis.get('task{0}'.format(event.chat_id))
                    if not task_point == None:
                        try:
                            task_point = eval(task_point.decode('utf-8'))
                            if not event.sender_id in task_point:
                                task_point[event.sender_id] = {'point':0}
                                redis.set('task{0}'.format(event.chat_id),str(task_point))
                                print('new member{0}'.format(event.sender_id))
                        except Exception as e:
                            print(e)
                    else:
                        list_member = {'rating_high':[]}
                        redis.set('task{0}'.format(event.chat_id),str(list_member))
                        await bot.send_message('aytola','data reset task {0}'.format(event.chat_id))
                if not list_m['gpplay'] == []:
                   # print(event.text)
                   # print(list_m['gpplay'][0])
                    if event.text == str(list_m['gpplay'][0]):
                        try:
                     #       print(1)
                            mes = str(list_m['gpplay'][1])
                    #        print(mes)
                            tes = await event.reply(mes)
                     #       print(tes)
                        except Exception as e:
                            print(e)
                if event.chat_id == list_m['group']:
                    if list_m['time_player'] == 1:
                        get_time_m = list_m['time_hnif'][1]
                        get_time_m = time.time() - get_time_m
                        get_time_m = round(get_time_m / 60)
                        if get_time_m >= 2:
                            list_m['time_hnif'][1] = time.time()
                            list_m['time_player'] = 0
                            redis.set(event.sender_id,str(list_m))
                            await bot.send_message(event.sender_id,'شما از فریز خارج شدید')
                        else:
                            await bot.delete_messages(event.chat_id,event.message.id)
                
            except Exception as e:
                try:
                    if event.chat_id == -1001232594917:
                        if not event.sender_id in bots:
                            list_m = redis.get(event.sender_id)
                            print(list_m)
                            if not list_m == None:
                                list_m = eval(list_m.decode('utf-8'))
                                if list_m['group'] == -1001232594917:
                                    print('bug')
                            else :
                                entity_m = await bot.get_entity(event.sender_id)
                                stat_member = {'group':-1001232594917,'gpplay':[],'place':'👶🏼لند پلیر','place_whiteplayer':1,'place_whiteone':0,'place_warlordwhite':0,
                                                'place_kinghtwhite':0,'place_smartwhite':0,'place_herowhite':0,'place_theemperor':0,'powers':[],
                                                'time_player':0,'powers_chalefazaii':[0,0],'powers_hipno':[0,0],'powers_mute':[0,0],'powers_spar':[0,0],
                                                'powers_hnif':[0,0],'powers_delete':[0,0],'time_hnif':[time.time(),0],'dubbed':'','hashtag':'','dateofbirth':'','motto':'','snow':5,'snowman':0,'key':0}
                                #await bot.send_message(-1001232594917,'🖇کاربر   {0}   در 𓄂ιcε‏⁦ ωσℓғ🐺 ࿐ ثبت نام کرد و 5 برفـ❄️ رایگان دریافت کرد🤩'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>')) 
                                #redis.set(event.sender_id,str(stat_member))
                except Exception as e:
                    print(e)
                print(e)

        @bot.on(events.NewMessage)
        async def member_statsw(event):
            if event.text == '/s':
                    try:
                        message_baner = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                        await bot.forward_messages(event.sender_id, message_baner.id, event.chat_id)
                    except UserIsBlockedError:
                        await event.reply('شما ربات رو بلاک کردید اول از بلاک در بیارید بعد')
                    except PeerIdInvalidError:
                        text_s = '''شما ثبت نام نکردید 
                جهت ثبت نام ارسال کنید 
                /mystats
                سپس سعی به ذخیره پیام ها کنید.'''
                        await event.reply(text_s)
            if event.text.startswith('/sh'):
                try:
                    messages_hash = event.text.split(' ')
                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    if list_m['place_whiteone'] == 1:
                        if messages_hash[1].startswith('#'):
                            list_m['hashtag'] = messages_hash[1]
                            list_m['gpplay'] = []
                            list_m['gpplay'].append(messages_hash[1])
                            list_m['gpplay'].append(message.text)
                            t3 = redis.set(event.sender_id,str(list_m))
                            await event.reply('saved')
                    else:
                        await event.reply('شما اول باید به مقام لند اولی دست پیدا کنید')
                        await menu_start(event.sender_id) 
                        
                    
                except Exception as e:
                    print(e)
            if event.text == 'دیلیت':
                try:
                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                    entity_m = await bot.get_entity(event.sender_id)
                    entity_m1 = await bot.get_entity(message.from_id)
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    try:
                        list_m1 = redis.get(entity_m1.id)
                        list_m1 = eval(list_m1.decode('utf-8'))
                    except Exception as e:
                        print(e)
                    if not event.sender_id in bots:
                        if not event.sender_id == entity_m1.id:
                            if list_m['powers_delete'][0] == 1:
                                try:
                                    if list_m1['powers_spar'][0] == 1:
                                        print('1')
                                        print(list_m1['powers_spar'])
                                        t = list_m1['powers_spar'][1] = list_m1['powers_spar'][1] - 1
                                        t1 = redis.set(entity_m1.id,str(list_m1))
                                        t2 = list_m['powers_delete'][1] = list_m['powers_delete'][1] - 1
                                        t3 = redis.set(entity_m.id,str(list_m))
                                        await bot.send_message(event.chat_id,'{0}  تلاش کرد با قدرت کلینر پیام  {1}  پاک کنه اما غافل از اینکه سپر اتشینـ 🔥 داشت'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>','<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                        print(t,t1,t2,t3)
                                        if list_m['powers_delete'][1] == 0:
                                            print('2')
                                            t = list_m['powers_delete'][0] = 0
                                            s_list = list_m['powers']
                                            s_list.remove('کلینر(دیلیت چت) 🗯')
                                            list_m['powers'] = s_list
                                            t1 = redis.set(entity_m.id,str(list_m))
                                            await bot.send_message(event.sender_id,'قدرت کلینر شما به پایان رسید')
                                            print(t,t1)
                                        if list_m1['powers_spar'][1] == 0:
                                            print('3')
                                            t = list_m1['powers_spar'][0] = 0
                                            s_list = list_m1['powers']
                                            s_list.remove('سپر اتشین 🔥')
                                            list_m1['powers'] = s_list
                                            t1 = redis.set(entity_m1.id,str(list_m1))
                                            await bot.send_message(entity_m1.id,'قدرت سپر آتشین شما به پایان رسید')
                                            print(t,t1)
                                    else:
                                        
                                        await bot.delete_messages(event.chat_id,int(event.message.id))
                                        await bot.delete_messages(event.chat_id,int(message.id))
                                        await bot.send_message(event.chat_id,'عه   {0}   با قدرت کلینرشـ🤫 پیام رو پاک کرد🗑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                        list_m['powers_delete'][1] = list_m['powers_delete'][1] - 1
                                        redis.set(event.sender_id,str(list_m))
                                        print(list_m['powers_delete'][1])
                                        if list_m['powers_delete'][1] - 1 == 0:
                                            s_list = list_m['powers']
                                            s_list.remove('کلینر(دیلیت چت) 🗯')
                                            list_m['powers_delete'][0] = 0
                                            list_m['powers'] = s_list
                                            redis.set(event.sender_id,str(list_m))
                                            await bot.send_message(event.sender_id,'قدرت کلینر شما به اتمام رسید')
                                except Exception as e:
                                    await bot.delete_messages(event.chat_id,int(event.message.id))
                                    await bot.delete_messages(event.chat_id,int(message.id))
                                    await bot.send_message(event.chat_id,'عه   {0}   با قدرت کلینرشـ🤫 پیام رو پاک کرد🗑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                    list_m['powers_delete'][1] = list_m['powers_delete'][1] - 1
                                    redis.set(event.sender_id,str(list_m))
                                    print(list_m['powers_delete'][1])
                                    if list_m['powers_delete'][1] - 1 == 0:
                                        s_list = list_m['powers']
                                        s_list.remove('کلینر(دیلیت چت) 🗯')
                                        list_m['powers_delete'][0] = 0
                                        list_m['powers'] = s_list
                                        redis.set(event.sender_id,str(list_m))
                                        await bot.send_message(event.sender_id,'قدرت کلینر شما به اتمام رسید')
                            else :
                                await bot.send_message(event.sender_id,'شما قدرت رو فعال ندارید لطفا ابتدا فعال کنید')
                except Exception as e:
                    print(e)
            if event.text == 'خفتش کن':
                try:
                    start_time = time.time()
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    print(list_m['powers_hnif'],0)
                    if list_m['powers_hnif'][0] == 1:
                        if list_m['powers_hnif'][1] > 0:
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            entity_m = await bot.get_entity(event.sender_id)
                            entity_m1 = await bot.get_entity(message.from_id)
                            if not event.sender_id == entity_m1.id:
                                list_m1 = redis.get(entity_m1.id)
                                list_m1 = eval(list_m1.decode('utf-8'))
                                if list_m1['place_warlordwhite'] == 1:
                                #if not event.sender_id == entity_m1.id:
                                    if list_m1['powers_ektlas'][0] == 1:
                                        number_hnif = random.randint(1,6)
                                        list_m1['snowman'] = list_m1['snowman'] + number_hnif 
                                        list_m['snowman'] = list_m['snowman'] - number_hnif
                                        list_m['powers_hnif'][0] = 0
                                        list_m['powers_hnif'][1] = 0
                                        s_list = list_m['powers']
                                        s_list.remove('برف ربا🤡')
                                        list_m['powers'] = s_list
                                        t2 = list_m1['powers_ektlas'][1] = list_m1['powers_ektlas'][1] - 1
                                        t1 = redis.set(entity_m1.id,str(list_m1))
                                        t3 = redis.set(entity_m.id,str(list_m))
                                        await bot.send_message(event.sender_id,'قدرت برف ربای شما به اتمام رسید')
                                        texts = '''واییییی {0} خاست  {1}  رو خفت کنه😱اما  {2}  خودش مافیای دزداست 
هاهاهاهاها😹 حالا باید  {3}⛄️ بهش بده تا مافیا زنده اش بزاره😏'''
                                        mafia_name = '<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'
                                        bar_name = '<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'
                                        await bot.send_message(event.chat_id,texts.format(bar_name,mafia_name,mafia_name,number_hnif))
                                        if list_m1['powers_ektlas'][1] == 0:
                                            print('2')
                                            t = list_m1['powers_ektlas'][0] = 0
                                            s_list = list_m1['powers']
                                            s_list.remove('اختلاس💰')
                                            list_m1['powers'] = s_list
                                            t1 = redis.set(entity_m1.id,str(list_m1))
                                            await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                    else:
                                        get_time_m = list_m1['time_hnif'][0]
                                        get_time_m = start_time - get_time_m
                                        get_time_m = round(get_time_m / 60)
                                        if get_time_m >= 1440:
                                            list_m1['time_hnif'][0] = start_time
                                            redis.set(entity_m1.id,str(list_m1))
                                            number_hnif = random.randint(150,250)
                                            list_m1['snow'] = list_m1['snow'] - number_hnif 
                                            list_m['snow'] = list_m['snow'] + number_hnif
                                            t1 = redis.set(entity_m1.id,str(list_m1))
                                            t2 = list_m['powers_hnif'][1] = list_m['powers_hnif'][1] - 1
                                            t3 = redis.set(entity_m.id,str(list_m))
                                            await bot.send_message(event.chat_id,'اوه!  {0} با قدرت برف ربایی که داشت تونست  {1} از  {2}   رو مال خودش کنه😼'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',number_hnif,'<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                            print(t1,t2,t3)
                                            if list_m['powers_hnif'][1] == 0:
                                                print('2')
                                                t = list_m['powers_hnif'][0] = 0
                                                s_list = list_m['powers']
                                                s_list.remove('برف ربا🤡')
                                                list_m['powers'] = s_list
                                                t1 = redis.set(entity_m.id,str(list_m))
                                                await bot.send_message(event.sender_id,'قدرت برف ربای شما به اتمام رسید')
                                        else :
                                            print(list_m1['time_hnif'][0])
                                            times = 1440 - get_time_m
                                            times = round(times / 60)
                                            print(times)
                                            await event.reply('کاربر مورد نظر در 24 ساعت گذشته خفت شده و سپر محافظش   {0}   ساعت فعاله'.format(times))
                                else :
                                    await event.reply('⚠️با توجه به اینکه مقام کاربر مورد نظر کمتر از سردار لند هست شما به کاهدون زدین و برفی کاسب نمیشین‼️😹')
                except Exception as e:
                    print(e)
            if event.text == 'فریز':
                try:
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    print(list_m['powers_mute'],0)
                    if list_m['powers_mute'][0] == 1:
                        if list_m['powers_mute'][1] > 0:
                            print('test')
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            entity_m = await bot.get_entity(event.sender_id)
                            entity_m1 = await bot.get_entity(message.from_id)
                            if not event.sender_id == entity_m1.id:
                                list_m1 = redis.get(entity_m1.id)
                                list_m1 = eval(list_m1.decode('utf-8'))
                                print(list_m1['powers_hipno'])
                                if list_m1['powers_hipno'][0] == 1:
                                    print('1')
                                    start_times = time.time()
                                    list_m['time_hnif'][1] = start_times
                                    list_m['time_player'] = 1
                                    t = list_m1['powers_hipno'][1] = list_m1['powers_hipno'][1] - 1
                                    t1 = redis.set(entity_m1.id,str(list_m1))
                                    t2 = list_m['powers_mute'][1] = list_m['powers_mute'][1] - 1
                                    t3 = redis.set(entity_m.id,str(list_m))
                                    await bot.send_message(event.chat_id,'  {0}  طلسمی در دستـ🔮 داره، گویا با این طلسم تونست قدرتـ   {1}   رو بر\nعلیه خودشـ💫 استفاده کنه و اون رو 2 دقیقه یخ زد🥶'.format('<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                    print(t1,t2,t3)
                                    if list_m['powers_mute'][1] == 0:
                                        print('2')
                                        t = list_m['powers_mute'][0] = 0
                                        s_list = list_m['powers']
                                        s_list.remove('انجماد🌬')
                                        list_m['powers'] = s_list
                                        t1 = redis.set(entity_m.id,str(list_m))
                                        await bot.send_message(event.sender_id,'قدرت فریز شما به اتمام رسید')
                                        print(t,t1)
                                    if list_m1['powers_hipno'][1] == 0:
                                        print('3')
                                        t = list_m1['powers_hipno'][0] = 0
                                        s_list = list_m1['powers']
                                        s_list.remove('طلسم🃏')
                                        list_m1['powers'] = s_list
                                        t1 = redis.set(entity_m1.id,str(list_m1))
                                        await bot.send_message(entity_m1.id,'قدرت طلسم شما به پایان رسید')
                                        print(t,t1)
                                elif list_m1['powers_spar'][0] == 1:
                                    print('1')
                                    print(list_m1['powers_spar'])
                                    t = list_m1['powers_spar'][1] = list_m1['powers_spar'][1] - 1
                                    t1 = redis.set(entity_m1.id,str(list_m1))
                                    t2 = list_m['powers_mute'][1] = list_m['powers_mute'][1] - 1
                                    t3 = redis.set(entity_m.id,str(list_m))
                                    await bot.send_message(event.chat_id,'  {0}    سپر اتشینـ🔥 خودش را در دست گرفت و از خودش در مقابل طوفان سردیـ🌬 که به طرفش می وزید محافظت کرد.'.format('<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                    print(t,t1,t2,t3)
                                    if list_m['powers_mute'][1] == 0:
                                        print('2')
                                        t = list_m['powers_mute'][0] = 0
                                        s_list = list_m['powers']
                                        s_list.remove('انجماد🌬')
                                        list_m['powers'] = s_list
                                        t1 = redis.set(entity_m.id,str(list_m))
                                        await bot.send_message(event.sender_id,'قدرت برف ربای شما به اتمام رسید')
                                        print(t,t1)
                                    if list_m1['powers_spar'][1] == 0:
                                        print('3')
                                        t = list_m1['powers_spar'][0] = 0
                                        s_list = list_m1['powers']
                                        s_list.remove('سپر اتشین 🔥')
                                        list_m1['powers'] = s_list
                                        t1 = redis.set(entity_m1.id,str(list_m1))
                                        await bot.send_message(entity_m1.id,'قدرت سپر آتشین شما به پایان رسید')
                                        print(t,t1)
                                else:
                                    print('1')
                                    start_times = time.time()
                                    list_m1['time_hnif'][1] = start_times
                                    list_m1['time_player'] = 1
                                    t1 = redis.set(entity_m1.id,str(list_m1))
                                    t2 = list_m['powers_mute'][1] = list_m['powers_mute'][1] - 1
                                    t3 = redis.set(entity_m.id,str(list_m))
                                    await bot.send_message(event.chat_id,'شت!   {0}   به مدت 2 دقیقه \n🌬 منجمد شد 🥶 مراقب باشید \n  {1}   میتونه\nشمارو یخ بزنه!\nمی‌تواند دو دقیقه هر شخصیو میوت کنه'.format('<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                    print(t1,t2,t3)
                                    if list_m['powers_mute'][1] == 0:
                                        print('2')
                                        t = list_m['powers_mute'][0] = 0
                                        s_list = list_m['powers']
                                        s_list.remove('انجماد🌬')
                                        list_m['powers'] = s_list
                                        t1 = redis.set(entity_m.id,str(list_m))
                                        await bot.send_message(event.sender_id,'قدرت فریز شما به پایان رسید')           
                            
                    if list_m['powers_mute'][0] == 0:
                        await bot.send_message(event.sender_id,'شما قدرت رو فعال ندارید لطفا ابتدا فعال کنید')
                    elif list_m['powers_mute'][1] == 0:
                        list_m['powers_mute'][0] = 0
                        s_list = list_m['powers']
                        s_list.remove('انجماد🌬')
                        list_m['powers'] = s_list
                        redis.set(event.sender_id,str(list_m))
                        await bot.send_message(event.sender_id,'قدرت برف ربای شما به اتمام رسید')
                except Exception as e:
                    print(e)
            if event.text == 'نابودش کن':
                try:
                    start_time = time.time()
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    print(list_m['powers_chalefazaii'],0)
                    if list_m['powers_chalefazaii'][0] == 1:
                        try:
                            t = 0
                            dele_powe = ''
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            entity_m = await bot.get_entity(event.sender_id)
                            entity_m1 = await bot.get_entity(message.from_id)
                            list_m = redis.get(event.sender_id)
                            list_m = eval(list_m.decode('utf-8'))
                            try:
                                list_m1 = redis.get(entity_m1.id)
                                list_m1 = eval(list_m1.decode('utf-8'))
                            except Exception as e:
                                print(e)
                            if not event.sender_id in bots:
                                if not event.sender_id == entity_m1.id:
                                    powers_list = []
                                    
                                    try:
                                        for i in list_m1['powers']:
                                            powers_list.append(i.strip(' '))
                                    except Exception as e:
                                        print(e)
                                    if not len(powers_list) == 0:
                                        list_m['powers_chalefazaii'][1] = list_m['powers_chalefazaii'][1] - 1
                                        t1 = redis.set(entity_m.id,str(list_m))
                                        list_m = redis.get(event.sender_id)
                                        list_m = eval(list_m.decode('utf-8'))
                                        if list_m['powers_chalefazaii'][1] == 0:
                                            list_m['powers_chalefazaii'][0] = 0
                                            s_list = list_m['powers']
                                            s_list.remove('سیاه چاله🎇')
                                            list_m['powers'] = s_list
                                            t1 = redis.set(entity_m.id,str(list_m))
                                            await bot.send_message(event.sender_id,'قدرت سیاه چاله شما به اتمام رسید')
                                        if 'سپر اتشین 🔥' in powers_list:
                                            if t < 2:
                                                list_m1['powers_spar'][0] = 0
                                                list_m1['powers_spar'][1] = 0
                                                s_list = list_m1['powers']
                                                s_list.remove('سپر اتشین 🔥')
                                                list_m1['powers'] = s_list
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t += 1
                                                dele_powe += ' سپر اتشین 🔥'+' '
                                        if 'انجماد🌬' in powers_list:
                                            if t < 2:
                                                list_m1['powers_mute'][0] = 0
                                                list_m1['powers_mute'][1] = 0
                                                s_list = list_m1['powers']
                                                s_list.remove('انجماد🌬')
                                                list_m1['powers'] = s_list
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t += 1
                                                dele_powe += ' انجماد🌬'+' '
                                        if 'سیاه چاله🎇' in powers_list:
                                            if t < 2:
                                                list_m1['powers_chalefazaii'][0] = 0
                                                list_m1['powers_chalefazaii'][1] = 0
                                                s_list = list_m1['powers']
                                                s_list.remove('سیاه چاله🎇')
                                                list_m1['powers'] = s_list
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t += 1
                                                dele_powe += ' سیاه چاله🎇'+' '
                                        if 'طلسم🃏' in powers_list:
                                            if t < 2:
                                                list_m1['powers_hipno'][0] = 0
                                                list_m1['powers_hipno'][1] = 0
                                                s_list = list_m1['powers']
                                                s_list.remove('طلسم🃏')
                                                list_m1['powers'] = s_list
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t += 1
                                                dele_powe += ' طلسم🃏'+' '
                                        if 'کلینر(دیلیت چت) 🗯' in powers_list:
                                            if t < 2:
                                                list_m1['powers_delete'][0] = 0
                                                list_m1['powers_delete'][1] = 0
                                                s_list = list_m1['powers']
                                                s_list.remove('کلینر(دیلیت چت) 🗯')
                                                list_m1['powers'] = s_list
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t += 1
                                                dele_powe += ' کلینر(دیلیت چت) 🗯'+' '
                                        print(t)
                                        await event.reply('توی لند صدای عجیبی میپیچه😱، چه اتفاقی افتاده؟ اونجارو ببینید   {0}   با قدرت ماورایی خودش تعدادی از قدرت های   {1}   رو نابود کرد☄️،مراقب باشید🤭 قدرت های از بین رفته (  {2}  )'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>','<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>',dele_powe))
                                    else:
                                        await event.reply('شخص مورد نظر هیچ قدرتی ندارد!')
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
            if event.text == 'بخوابونش':
                try:
                    start_time = time.time()
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    print(list_m['powers_ektlas'],0)
                    if list_m['powers_ektlas'][0] == 1:
                        if list_m['powers_ektlas'][1] > 0:
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            entity_m = await bot.get_entity(event.sender_id)
                            entity_m1 = await bot.get_entity(message.from_id)
                            if not event.sender_id == entity_m1.id:
                                list_m1 = redis.get(entity_m1.id)
                                list_m1 = eval(list_m1.decode('utf-8'))
                                get_time_m = list_m1['time_hnif'][0]
                                get_time_m = start_time - get_time_m
                                get_time_m = round(get_time_m / 60)
                                if get_time_m >= 1440:
                                    if list_m1['place_herowhite'] == 1:
                                        if list_m1['powers_ektlas'][0] == 1:
                                            print(list_m['powers_ektlas'][0])
                                            random_mafia = random.randint(0,1)
                                            if random_mafia == 1:
                                                list_m1['time_hnif'][0] = start_time
                                                redis.set(entity_m1.id,str(list_m1))
                                                number_hnif = random.randint(1,6)
                                                list_m1['snowman'] = list_m1['snowman'] + number_hnif 
                                                list_m['snowman'] = list_m['snowman'] - number_hnif
                                                list_m1['powers_ektlas'][1] = list_m1['powers_ektlas'][1] - 1
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                tezt = '''اینجارو نگااا دو تا مافیا افتادن به جون هم😹 مافیای {0} که انگاری بد کسی رو برای اختلاس انتخاب کردی😏 مافیای {1} خودش رئیس مافیاهاست🙀حالا برای جبران این جسارتت قدرت اختلاصت غیر فعال که میشه هیچ....باید {2}⛄️ بدی به رئیس😹‼️'''
                                                await bot.send_message(event.chat_id,tezt.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>','<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>',number_hnif))
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                                if list_m1['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m1['powers_ektlas'][0] = 0
                                                    s_list = list_m1['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m1['powers'] = s_list
                                                    t1 = redis.set(entity_m1.id,str(list_m1))
                                                    await bot.send_message(entity_m1.id,'قدرت اختلاس شما به اتمام رسید')
                                            elif random_mafia == 0:
                                                list_m1['time_hnif'][0] = start_time
                                                redis.set(entity_m1.id,str(list_m1))
                                                number_hnif = random.randint(15,20)
                                                list_m1['snowman'] = list_m1['snowman'] - number_hnif 
                                                list_m['snowman'] = list_m['snowman'] + number_hnif
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                tezt = '''نچ نچ ببین چه خبره :/ مافیا {0} خاسته ادم برفی اختلاص کنه😶اما خبر نداشت ک {1} خودش یه مافیا هست🤫این بار مافیا {0} تونست با استفاده از غفلت مافیا {1} ؛ {2} بزنه به جیب‼️'''
                                                await bot.send_message(event.chat_id,tezt.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>','<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>',number_hnif))
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                        else:
                                            list_m1['time_hnif'][0] = start_time
                                            redis.set(entity_m1.id,str(list_m1))
                                            if list_m1['snowman'] < 5:
                                                number_hnif = random.randint(1,5)
                                                list_m1['snowman'] = list_m1['snowman'] - number_hnif 
                                                list_m['snowman'] = list_m['snowman'] + number_hnif
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                await bot.send_message(event.chat_id,'فاک...‼️ مافیای لند {0} بیدار شده😮 با قدرت خارق العاده اش {1}⛄️رو از {2} اختلاس کرد😑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',number_hnif,'<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                                print(t1,t2,t3)
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                            elif list_m1['snowman'] < 10:
                                                number_hnif = random.randint(5,10)
                                                list_m1['snowman'] = list_m1['snowman'] - number_hnif 
                                                list_m['snowman'] = list_m['snowman'] + number_hnif
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                await bot.send_message(event.chat_id,'فاک...‼️ مافیای لند {0} بیدار شده😮 با قدرت خارق العاده اش {1}⛄️رو از {2} اختلاس کرد😑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',number_hnif,'<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                                print(t1,t2,t3)
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                            elif list_m1['snowman'] < 20:
                                                number_hnif = random.randint(10,15)
                                                list_m1['snowman'] = list_m1['snowman'] - number_hnif 
                                                list_m['snowman'] = list_m['snowman'] + number_hnif
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                await bot.send_message(event.chat_id,'فاک...‼️ مافیای لند {0} بیدار شده😮 با قدرت خارق العاده اش {1}⛄️رو از {2} اختلاس کرد😑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',number_hnif,'<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                                print(t1,t2,t3)
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                            else:
                                                number_hnif = random.randint(15,20)
                                                list_m1['snowman'] = list_m1['snowman'] - number_hnif 
                                                list_m['snowman'] = list_m['snowman'] + number_hnif
                                                t1 = redis.set(entity_m1.id,str(list_m1))
                                                t2 = list_m['powers_ektlas'][1] = list_m['powers_ektlas'][1] - 1
                                                t3 = redis.set(entity_m.id,str(list_m))
                                                await bot.send_message(event.chat_id,'فاک...‼️ مافیای لند {0} بیدار شده😮 با قدرت خارق العاده اش {1}⛄️رو از {2} اختلاس کرد😑'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',number_hnif,'<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                                                print(t1,t2,t3)
                                                if list_m['powers_ektlas'][1] == 0:
                                                    print('2')
                                                    t = list_m['powers_ektlas'][0] = 0
                                                    s_list = list_m['powers']
                                                    s_list.remove('اختلاس💰')
                                                    list_m['powers'] = s_list
                                                    t1 = redis.set(entity_m.id,str(list_m))
                                                    await bot.send_message(event.sender_id,'قدرت اختلاس شما به اتمام رسید')
                                    else :
                                        await event.reply('⚠️عاموووو داری چیکار میکنی ....مافیا هم مافیا های قدیم برو از یکی که هم قد و قواره خودته اختلاص کن🤨  تا به مقام قهرمان لند نرسیده دیگه نزدیکش نشی ها😹❌')
                                else :
                                    print(list_m1['time_hnif'][0])
                                    times = 1440 - get_time_m
                                    times = round(times / 60)
                                    print(times)
                                    await event.reply('کاربر مورد نظر در 24 ساعت گذشته خفت شده و سپر محافظش   {0}   ساعت فعاله'.format(times))
                except Exception as e:
                    print(e)
            if event.text == 'بمالش':
                if redis.get('bmal_white').decode('utf-8') == 'on':
                    list_m = redis.get(event.sender_id)
                    list_m = eval(list_m.decode('utf-8'))
                    try:
                        if list_m['snow'] >= 75:
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            entity_m = await bot.get_entity(event.sender_id)
                            entity_m1 = await bot.get_entity(message.from_id)
                            if not event.sender_id == entity_m1.id:
                                list_m1 = redis.get(entity_m1.id)
                                list_m1 = eval(list_m1.decode('utf-8'))
                                list_m['snow'] = list_m['snow'] - 75
                                list_m1['snow'] = list_m1['snow'] + 75
                                redis.set(event.sender_id,str(list_m))
                                redis.set(entity_m1.id,str(list_m1))
                                text_m = '''🙈اوه اوه {0} مالید چه مالیدنی 🙉
    با مالیدنی که انجام داد 75❄️ به {1} داد💥'''
                                await event.reply(text_m.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>','<a href=tg://user?id='+str(entity_m1.id)+'>'+ entity_m1.first_name+'</a>'))
                        else:
                            await event.reply('درسته که دوست داری بمالی بقیه رو ولی مالیدن که بی مزد نمیشه برو برف جمع کن😒')
                    except Exception as e:
                        print(e)
        @bot.on(events.NewMessage)
        async def member_stats(event):
            try:
                if event.sender_id in admin_white:
                    if event.text.startswith('🎁'):
                        print(2)
                        message = event.text.split('-')
                        print(message)
                        if message[1] == '1':
                            s = redis.set('jayze1',message[2])
                            print(s)
                            await event.reply('جایزه اول ست شد    {0}'.format(message[2]))
                        elif message[1] == '2':
                            redis.set('jayze2',message[2])
                            await event.reply('جایزه دوم ست شد     {0}'.format(message[2]))
                        elif message[1] == '3':
                            redis.set('jayze3',message[2])
                            await event.reply('جایزه سوم ست شد  {0}'.format(message[2]))
                        elif message[1] == '4':
                            redis.set('jayze4',message[2])
                            await event.reply('جایزه چهارم ست شد   {0}'.format(message[2]))
                        elif message[1] == '5':
                            redis.set('jayze5',message[2])
                            await event.reply('جایزه پنجم ست شد   {0}'.format(message[2]))
                        elif message[1] == '6':
                            redis.set('jayze6',message[2])
                            await event.reply('جایزه ششم ست شد   {0}'.format(message[2]))
                        elif message[1] == '7':
                            redis.set('jayze7',message[2])
                            await event.reply('جایزه هفتم ست شد   {0}'.format(message[2]))
                        elif message[1] == '8':
                            redis.set('jayze8',message[2])
                            await event.reply('جایزه هشتم ست شد  {0}'.format(message[2]))
                        elif message[1] == '9':
                            redis.set('jayze9',message[2])
                            await event.reply('جایزه نهم ست شد  {0}'.format(message[2]))
                        elif message[1] == '10':
                            redis.set('jayze10',message[2])
                            await event.reply('جایزه دهم ست شد   {0}'.format(message[2]))
                    if event.text.startswith('/addbetwhite'):
                        try:
                            bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                        'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                        'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                        'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                            redis.set('bet_white_ice',str(bet_zarib))
                            await event.reply('bot add bet')
                        except Exception as e:
                            print(e)
                    if event.text.startswith('/rembetuser'):
                        try:
                            message = event.text.split(' ')
                            bet = {}
                            redis.set('{0}bet'.format(int(message[1])),str(bet))
                            await event.reply('rem user for bet {0}'.format(message[1]))
                            await bot.send_message(-1001393884185,'rem user for bet {0}'.format(message[1]))
                        except Exception as e:
                            print(e)
                    if event.text.startswith('/addbetuser'):
                        try:
                            message = event.text.split(' ')
                            bet = {'bet_one':'','bet_one_snow':0,'bet_two':'','bet_two_snow':0,'game':0}
                            redis.set('{0}bet'.format(int(message[1])),str(bet))
                            await event.reply('add user for bet {0}'.format(message[1]))
                            await bot.send_message(-1001393884185,'add user for bet {0}'.format(message[1]))
                        except Exception as e:
                            print(e)
                    if event.text.startswith('/up_bet'):
                        s = redis.get('bet_white_ice')
                        s = eval(s.decode('utf-8'))
                        s['game_number'] += 1
                        redis.set('bet_white_ice',str(s))
                        await event.reply('up bet {0}'.format(s['game_number']))
                        await bot.send_message(-1001393884185,'up bet {0}'.format(s['game_number']))
                    if event.text.startswith('ضریب'):
                        message = event.text.split(' ')
                        if message[1] == 'روس':
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['ros'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib ros {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ros {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['ros'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib ros {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ros {0}'.format(message[2]))
                        elif message[1] == 'گرگ':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['gorg'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib gorg {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib gorg {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['gorg'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib gorg {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib gorg {0}'.format(message[2]))
                        elif message[1] == 'فرقه':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['ferghe'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib ferghe {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ferghe {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['ferghe'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib ferghe {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ferghe {0}'.format(message[2]))
                        elif message[1] == 'قاتل':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['ghatel'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib ghatel {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ghatel {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['ghatel'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib ghatel {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib ghatel {0}'.format(message[2]))
                        elif message[1] == 'اتیش':
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['atish'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib atish {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib atish {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['atish'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib atish {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib atish {0}'.format(message[2]))
                        elif message[1] == 'منافق':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['monafegh'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib monafegh {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib monafegh {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['monafegh'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib monafegh {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib monafegh {0}'.format(message[2]))
                        elif message[1] == 'لاور':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['lover'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib lover {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib lover {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['lover'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib lover {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib lover {0}'.format(message[2]))
                        elif message[1] == 'باخت':
                            
                            bet = redis.get('bet_white_ice')
                            if not bet == None:
                                bet = eval(bet.decode('utf-8'))
                                bet['lose'] = float(message[2])
                                redis.set('bet_white_ice',str(bet))
                                await event.reply('set zarib lose {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib lose {0}'.format(message[2]))
                            else:
                                bet_zarib = {'ros':0,'ferghe':0,'gorg':0,'ghatel':0,
                                            'atish':0,'lover':0,'monafegh':0,'lose':0,'game_number':0,
                                            'bet_game_zarib':{'ros':0,'ferghe':0,'gorg':0,
                                                            'ghatel':0,'atish':0,'lover':0,'monafegh':0,'lose':0}}
                                bet_zarib['lose'] = float(message[2])
                                redis.set('bet_white_ice',str(bet_zarib))
                                await event.reply('set zarib lose {0}'.format(message[2]))
                                await bot.send_message(-1001393884185,'set zarib lose {0}'.format(message[2]))
                    if event.text.startswith('/bmal'):
                        message = event.text.split(' ')
                        if message[1] == 'on':
                            redis.set('bmal_white','on')
                            await event.reply('مالش ازاد شد')
                            await bot.send_message(-1001393884185,'مالش برای همه باز شد')
                        elif message[1] == 'off':
                            redis.set('bmal_white','off')
                            await event.reply('مالش ممنوع شد')
                            await bot.send_message(-1001393884185,'مالش برای همه ممنوع شد')
                    if event.text.startswith('/betwhite'):
                        message = event.text.split(' ')
                        if message[1] == 'on':
                            redis.set('bet_white_check','on')
                            await event.reply('بت بستن باز شد')
                            await bot.send_message(-1001393884185,'بت برای همه باز شد')
                        elif message[1] == 'off':
                            redis.set('bet_white_check','off')
                            await event.reply('بت بستن برای همه بسته شد')
                            await bot.send_message(-1001393884185,'بت برای همه بسته شد')
                    if event.text.startswith('/forallmemberwhite'):
                        allmember = redis.get('stats_white_member')
                        allmember = eval(allmember.decode("utf-8"))
                        messages = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                        for i in allmember:
                            try:
                                await bot.send_message(int(i),messages.message)
                            except FloodWaitError as ex:
                                print('Flood wait :',ex.seconds)
                                await asyncio.sleep(ex.seconds)
                                await event.reply("Flood wait : "+str(ex.seconds))
                            except Exception as e:
                                print(e)
                        
            except Exception as e:
                print(e)
            if event.text.startswith('/start'):
                try:
                    try:
                        message = event.text.split(' ')
                        print(eval(message[1]))
                        try:
                            list_m = redis.get(event.sender_id)
                            print(list_m)
                            if not list_m == None:
                                list_m = eval(list_m.decode('utf-8'))
                                if list_m['group'] == eval(message[1]):
                                    await bot.send_message(event.sender_id,'شما قبلا در این گروه ثبت نام کرده اید')
                            else :
                                entity_gp = await bot.get_entity(eval(message[1]))
                                entity_m = await bot.get_entity(event.sender_id)
                                await event.reply(entity_gp.title) 
                                stat_member = {'group':eval(message[1]),'gpplay':[],'place':'👶🏼لند پلیر','place_whiteplayer':1,'place_whiteone':0,'place_warlordwhite':0,
                                                'place_kinghtwhite':0,'place_smartwhite':0,'place_herowhite':0,'place_theemperor':0,'place_mafiawhite':0,'powers':[],
                                                'time_player':0,'powers_chalefazaii':[0,0],'powers_hipno':[0,0],'powers_mute':[0,0],'powers_spar':[0,0],
                                                'powers_hnif':[0,0],'powers_ektlas':[0,0],'powers_delete':[0,0],'time_hnif_sell':[time.time(),0],'time_ekhtlas_sell':[time.time(),0],'time_hnif':[time.time(),0],'dubbed':'','hashtag':'','dateofbirth':'','motto':'','snow':5,'snowman':0,'key':0}
                                await bot.send_message(eval(message[1]),'🖇کاربر   {0} در 🌗❆WσlfLαиd❆🌓 ثبت نام کرد و 5❄️ دریافت کرد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>')) 
                                redis.set(event.sender_id,str(stat_member))
                        except Exception as e:
                            print(e)
                        except UserIsBlockedError as e:
                            print(e)
                    except Exception as e:
                        try:
                            await menu_start(event.sender_id)
                        except UserIsBlockedError as e:
                            print(e)
                            await event.reply("شما ربات رو استارت نزدید لطفا اول استارت بزنید سپس اقدام نمایید")
                except Exception as e:
                    print(e)
            if event.text.startswith('/deleteuser'):
                if event.sender_id in admin:
                    try:
                        message = event.text.split(" ")
                        redis.delete(int(message[1]))
                        await event.reply("user Deleted")
                    except Exception as e:
                        print(e)
            if event.text.startswith('/mystats'):
                #print(event)
                entity = await bot.get_entity(event.sender_id)
                #print(entity)
                statmember = redis.get(event.sender_id)
                if statmember == None:
                    try:
                        k3 = Button.url('start', 't.me/icepowerbot?start={0}'.format(event.chat_id))
                        await event.reply('شما ثبت نام نکردید لطفا ابتدا ربات رو استارت بزنید',buttons=[[k3]])
                    except Exception as e:
                        print(e)
                else:
                    try:
                        list_m = eval(redis.get(event.sender_id).decode('utf-8'))
                        powers_list = ""
                        print(list_m['powers'])
                        try:
                            for i in list_m['powers']:
                                powers_list += i+" "
                        except Exception as e:
                            print(e)
                        list_mt = eval(redis.get('task{0}'.format(-1001328443567)).decode('utf-8'))
                        #await event.reply('{0}\n👑مقام :  {1}\n ⚡️قدرت‌ها :  {2}\n   📉امتیاز: {3}\n🎟لقب :  {4}\n 🔰هشتگ اختصاصی : {5}\n 🎉 تاریخ تولد : {6}\n📌شعار : {7}\n{8}\n❄️: {9}\n☃️‌‌: {10}\n🗝: {11}\n'.format(entity.first_name,list_mt[int(i)]['point'],list_m['place'],powers_list,list_m['dubbed'],list_m['hashtag'],list_m['dateofbirth'],list_m['motto'],list_m['key'],str('-'*50),list_m['snow'],list_m['snowman']))
                        await event.reply('{0}\n👑مقام :  {1}\n⚡️قدرت‌ها :  {2}\n📉امتیاز: {3}\n🎟لقب :  {4}\n🔰هشتگ اختصاصی : {5}\n🎉 تاریخ تولد : {6}\n📌شعار : {7}\n{8}\n❄️: {9}\n☃️‌‌: {10}\n🗝: {11}\n'.format(entity.first_name,list_m['place'],powers_list,list_mt[event.sender_id]['point'],list_m['dubbed'],list_m['hashtag'],list_m['dateofbirth'],list_m['motto'],str('-'*50),list_m['snow'],list_m['snowman'],list_m['key']))
                    except Exception as e:
                        print(e)
            
        @bot.on(events.NewMessage)
        async def admin_comment(event):
            if event.sender_id in admin:
                try:
                    if event.text.startswith('/promote'):
                        message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                        redis.set(message.from_id+1024,1)
                        await event.reply('کاربر ادمین شد')
                    if event.text.startswith('/demote'):
                        message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                        redis.set(message.from_id+1024,0)
                        await event.reply('کاربر عزل شد')
                except Exception as e:
                    print(e)
            try: 
                if event.text.startswith('+⛄️'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) <20:
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['snowman'] = list_m['snowman'] + int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  ⛄️اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   ⛄️ به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 20:
                                    
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['snowman'] = list_m['snowman'] + int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  ⛄️اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   ⛄️ به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+❄️'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    print(t)
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) < 2000:
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['snow'] = list_m['snow'] + int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  ❄️اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   ❄️ به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 200 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 2000:
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['snow'] = list_m['snow'] + int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  ❄️اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   ❄️ به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 200 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🗝'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) < 20:
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['key'] = list_m['key'] + int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  🗝اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   🗝 به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 20:
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['key'] = list_m['key'] + int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   به کاربر   {1}   مقدار   {2}  🗝اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   🗝 به کاربر   {0}   اهدا شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('-⛄️'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) < 20:          
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['snowman'] = list_m['snowman'] - int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  ⛄️ کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   ⛄️ از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 20:
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['snowman'] = list_m['snowman'] - int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  ⛄️ کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   ⛄️ از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('-❄️'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) < 2000:
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['snow'] = list_m['snow'] - int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  ❄️ کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   ❄️ از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 2000:
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['snow'] = list_m['snow'] - int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  ❄️ کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   ❄️ از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('-🗝'):
                    t = redis.get(event.sender_id+1024).decode('utf-8')
                    if int(t) == 1:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message_int = event.text.split(' ')
                                if int(message_int[1]) < 20:
                                    message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                    list_m['key'] = list_m['key'] - int(message_int[1])
                                    entity_m = await bot.get_entity(message.from_id)
                                    redis.set(message.from_id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  🗝 کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                    await event.reply('  {1}   🗝 از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message_int[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                if int(message[1]) < 20:
                                    entity_m = await bot.get_entity(message[2].strip('@'))
                                    #print(entity_m)
                                    list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                    list_m['key'] = list_m['key'] - int(message[1])
                                    redis.set(entity_m.id,str(list_m))
                                    entity_admin = await bot.get_entity(event.sender_id)
                                    await bot.send_message(-1001393884185,'ادمین   {0}   از کاربر   {1}   مقدار   {2}  🗝 کم کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                    await event.reply('  {1}   🗝 از کاربر   {0}   کسر شد'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',message[1]))
                                else :
                                    await event.reply('کمتر از 20 امتیاز امکان پذیر است')
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🤡'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_hnif'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('برف ربا🤡')
                                    list_m['powers'] = list_powers
                                list_m['powers_hnif'][0] = 1
                                list_m['powers_hnif'][1] = list_m['powers_hnif'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت برف ربا اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت برف ربا 🤡 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_hnif'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('برف ربا🤡')
                                    list_m['powers'] = list_powers
                                list_m['powers_hnif'][0] = 1
                                list_m['powers_hnif'][1] = list_m['powers_hnif'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت برف ربا اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت برف ربا 🤡 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🃏'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_hipno'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('طلسم🃏')
                                    list_m['powers'] = list_powers
                                list_m['powers_hipno'][0] = 1
                                list_m['powers_hipno'][1] = list_m['powers_hipno'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت طلسم اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر  {0}\nبرنده قدرت طلسم🃏 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_hipno'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('طلسم🃏')
                                    list_m['powers'] = list_powers
                                list_m['powers_hipno'][0] = 1
                                list_m['powers_hipno'][1] = list_m['powers_hipno'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت طلسم اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر  {0}\nبرنده قدرت طلسم🃏 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🌬'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_mute'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('انجماد🌬')
                                    list_m['powers'] = list_powers
                                list_m['powers_mute'][0] = 1
                                list_m['powers_mute'][1] = list_m['powers_mute'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت انجماد اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت انجماد🌬 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_mute'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('انجماد🌬')
                                    list_m['powers'] = list_powers
                                list_m['powers_mute'][0] = 1
                                list_m['powers_mute'][1] = list_m['powers_mute'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت انجماد اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت انجماد🌬 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🗯'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_delete'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('کلینر(دیلیت چت) 🗯')
                                    list_m['powers'] = list_powers
                                list_m['powers_delete'][0] = 1
                                list_m['powers_delete'][1] = list_m['powers_delete'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت دیلیت اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت کلینر🗯 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_delete'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('کلینر(دیلیت چت) 🗯')
                                    list_m['powers'] = list_powers
                                list_m['powers_delete'][0] = 1
                                list_m['powers_delete'][1] = list_m['powers_delete'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت دیلیت اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت کلینر🗯 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🎇'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_chalefazaii'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('سیاه چاله🎇')
                                    list_m['powers'] = list_powers
                                list_m['powers_chalefazaii'][0] = 1
                                list_m['powers_chalefazaii'][1] = list_m['powers_chalefazaii'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت سیاه چاله اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت سیاه چاله 🎇 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_chalefazaii'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('سیاه چاله🎇')
                                    list_m['powers'] = list_powers
                                list_m['powers_chalefazaii'][0] = 1
                                list_m['powers_chalefazaii'][1] = list_m['powers_chalefazaii'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت سیاه چاله اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت سیاه چاله 🎇 شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                elif event.text.startswith('+🔥'):
                    if event.sender_id in admin:
                        f = event.reply_to_msg_id
                        print(f)
                        if not event.reply_to_msg_id == None:
                            try:
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                list_m = eval(redis.get(message.from_id).decode('utf-8'))
                                if list_m['powers_spar'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('سپر اتشین 🔥')
                                    list_m['powers'] = list_powers
                                list_m['powers_spar'][0] = 1
                                list_m['powers_spar'][1] = list_m['powers_spar'][1] + 3
                                entity_m = await bot.get_entity(message.from_id)
                                redis.set(message.from_id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت سپراتشین اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت سپر آتشین🔥شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
                        else:
                            try:
                                message = event.text.split(" ")
                                entity_m = await bot.get_entity(message[1].strip('@'))
                                list_m = eval(redis.get(entity_m.id).decode('utf-8'))
                                if list_m['powers_spar'][0] == 0:
                                    list_powers = list_m['powers']
                                    list_powers.append('سپر اتشین 🔥')
                                    list_m['powers'] = list_powers
                                list_m['powers_spar'][0] = 1
                                list_m['powers_spar'][1] = list_m['powers_spar'][1] + 3
                                redis.set(entity_m.id,str(list_m))
                                entity_admin = await bot.get_entity(event.sender_id)
                                await bot.send_message(-1001393884185,'ادمین  {0} \n به کاربر {1} قدرت سپراتشین اضافه کرد'.format('<a href=tg://user?id='+str(entity_admin.id)+'>'+ entity_admin.first_name+'</a>','<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                                await event.reply('✳️کاربر {0}\n برنده قدرت سپر آتشین🔥شد❗️'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>'))
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)
        
        @bot.on(events.NewMessage)
        async def member_stats22(event):
            try:
                def list_i(i,rating):
                    i = i.split('"')[1].split('"')[0]
                    i = i.split('tg://user?id=')
                    i = int(i[1])
                    check_user = redis.get(int(i))
                    if not check_user == None:
                        list_m = eval(redis.get(int(i)).decode('utf-8'))
                        list_m['snow'] = list_m['snow'] + rating
                        redis.set(int(i),str(list_m))
                        return i
                    else:
                        return None
                if event.text.startswith('/getpoints'):
                    admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                    list_admin_gp = []
                    for i in admin_gp:
                        list_admin_gp.append(i.id)
                    if event.sender_id in list_admin_gp:
                        redis_get = redis.get('chat_{0}_getlist'.format(event.chat_id))
                        if redis_get == None:
                            redis.set('chat_{0}_getlist'.format(event.chat_id),'[{0}]'.format(event.reply_to_msg_id))
                        else :
                            redis_get = redis.get('chat_{0}_getlist'.format(event.chat_id)).decode('utf-8')
                            list_play = eval(redis_get)
                            if event.reply_to_msg_id in list_play:
                                await client.connect()
                                message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                if 'مدت زمان بازی' in message.text:
                                    await event.reply('از قبل امتیازش محاسبه شده')
                            else:
                                if not event.reply_to_msg_id == None:
                                    message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    if 'مدت زمان بازی' in message.text:
                                        if re.search(game_finish,message.text):
                                            game['all_user'] = []
                                            game['role_users'] = {}
                                            game['shekarchi'] = 0
                                            game['sv'] = ''
                                            await event.reply('بازی خوبی بود')
                                        if message.from_id in bots:
                                            if len(list_play) == 150:
                                                list_play = []
                                            list_play.append(event.reply_to_msg_id)
                                            redis.set('chat_{0}_getlist'.format(event.chat_id),'{0}'.format(list_play))
                                            t = message.text
                                            t = t.split('\n')
                                            sw = []
                                            for i in t:
                                                if 'tg://user?id=' in i:
                                                    if 'برنده' in i:
                                                        try:
                                                            if 'روستایی' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'تفنگدار' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'فراماسون' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'مست' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'قاتل زنجیره ای' in i:
                                                                check_user_none = list_i(i,8)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,8])
                                                            elif 'فرقه گرا' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'گرگینه' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'الهه عشق' in i:
                                                                if not list_i(i,1) == None:
                                                                    check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'احمق' in i:
                                                                if not list_i(i,1) == None:
                                                                    check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'پیشگو' in i:
                                                                if not list_i(i,1) == None:
                                                                    sw.append([list_i(i,4),4])
                                                            elif 'پیشگوی نگاتیوی' in i:
                                                                if not list_i(i,1) == None:
                                                                    check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'گرگ نما' in i:
                                                                if not list_i(i,1) == None:
                                                                    check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'ریش سفید' in i:
                                                                if not list_i(i,1) == None:
                                                                    check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'فاحشه' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'ناظر' in i:
                                                                check_user_none = list_i(i,3)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,3])
                                                            elif 'خائن' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'فرشته نگهبان' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'کاراگاه' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'پیشگوی رزرو' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'شکارچی' in i:
                                                                check_user_none = list_i(i,6)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,6])
                                                            elif 'بچه وحشی' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'همزاد' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'کلانتر' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'منافق' in i:
                                                                check_user_none = list_i(i,8)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,8])
                                                            elif 'کدخدا' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'شاهزاده' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'جادوگر' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'پسر گیج' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'آهنگر ' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'گرگ آلفا' in i:
                                                                check_user_none = list_i(i,6)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,6])
                                                            elif 'توله گرگ' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'خواب گذار' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'گرگ ایکس' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'صلح گرا' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'دزد' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'دردسرساز' in i:
                                                                check_user_none = list_i(i,2)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,2])
                                                            elif 'شیمیدان' in i:
                                                                check_user_none = list_i(i,3)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,3])
                                                            elif 'گرگ برفی' in i:
                                                                check_user_none = list_i(i,4)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,4])
                                                            elif 'تش زن' in i:
                                                                check_user_none = list_i(i,8)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,8])
                                                            elif 'رمال' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                            elif 'گورکن ' in i:
                                                                check_user_none = list_i(i,1)
                                                                if not check_user_none == None:
                                                                    sw.append([check_user_none,1])
                                                        except Exception as e:
                                                            print(e)
                                            list_rating = 'جوایز:\n'
                                            for i in sw:
                                                entity_m = await bot.get_entity(int(i[0]))
                                                list_rating += '{0}\t\t{1} ❄️\t\n'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',i[1])
                                            await bot.send_message(event.chat_id,list_rating)
            except Exception as e:
                print(e)
    
        @bot.on(events.NewMessage)
        async def point_task(event):
            try:
                def list_i(i,rating):
                    i = i.split('"')[1].split('"')[0]
                    i = i.split('tg://user?id=')
                    i = int(i[1])
                    check_user = redis.get('task{0}'.format(event.chat_id))
                    if not check_user == None:
                        list_m = eval(redis.get('task{0}'.format(event.chat_id)).decode('utf-8'))
                        list_m[int(i)]['point'] = list_m[int(i)]['point'] + rating
                        redis.set('task{0}'.format(event.chat_id),str(list_m))
                        return i
                    else:
                        return None
                if event.text.startswith('/getpoints'):
                    admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                    list_admin_gp = []
                    for i in admin_gp:
                        list_admin_gp.append(i.id)
                    if event.sender_id in list_admin_gp:
                        redis_get = redis.get('chat_{0}_getlist_task'.format(event.chat_id))
                        if redis_get == None:
                            redis.set('chat_{0}_getlist_task'.format(event.chat_id),'[{0}]'.format(event.reply_to_msg_id))
                        else :
                            redis_get = redis.get('chat_{0}_getlist_task'.format(event.chat_id)).decode('utf-8')
                            list_play = eval(redis_get)
                            if event.reply_to_msg_id in list_play:
                                await client.connect()
                                message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                if 'مدت زمان بازی' in message.text:
                                    print('old message')
                            else:
                                if not event.reply_to_msg_id == None:
                                    message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    if 'مدت زمان بازی' in message.text:
                                        if message.from_id in bots:
                                            if len(list_play) == 150:
                                                list_play = []
                                            list_play.append(event.reply_to_msg_id)
                                            redis.set('chat_{0}_getlist_task'.format(event.chat_id),'{0}'.format(list_play))
                                            t = message.text
                                            t = t.split('\n')
                                            sw = []
                                            for i in t:
                                                if 'tg://user?id=' in i:
                                                    if 'برنده' in i:
                                                        try:
                                                            if 'روستایی' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'تفنگدار' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,100)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,100])
                                                            elif 'فراماسون' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'مست' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'قاتل زنجیره ای' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,500)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,500])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,500)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,400])
                                                            elif 'فرقه گرا' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,350)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,350])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,250)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,250])
                                                            elif 'گرگینه' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'الهه عشق' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,100)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,100])
                                                            elif 'احمق' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,175)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,175])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,75)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,75])
                                                            elif 'پیشگو' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'پیشگوی نگاتیوی' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,100)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,100])
                                                            elif 'گرگ نما' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'ریش سفید' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,100)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,100])
                                                            elif 'فاحشه' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'ناظر' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,250)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,250])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                            elif 'خائن' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,220)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,220])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,120)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,120])
                                                            elif 'فرشته نگهبان' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'کاراگاه' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'پیشگوی رزرو' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,175)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,175])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,75)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,75])
                                                            elif 'شکارچی' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,400)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,400])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                            elif 'بچه وحشی' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,225)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,225])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,125)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,125])
                                                            elif 'همزاد' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,195)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,195])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,95)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,95])
                                                            elif 'کلانتر' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,195)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,195])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,95)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,95])
                                                            elif 'منافق' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,500)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,500])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,400)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,400])
                                                            elif 'کدخدا' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,175)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,175])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,75)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,75])
                                                            elif 'شاهزاده' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'جادوگر' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,250)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,250])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                            elif 'پسر گیج' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'آهنگر ' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,195)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,195])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,95)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,95])
                                                            elif 'گرگ آلفا' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,400)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,400])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                            elif 'توله گرگ' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,350)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,350])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,250)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,250])
                                                            elif 'خواب گذار' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,100)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,100])
                                                            elif 'گرگ ایکس' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,350)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,350])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,250)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,250])
                                                            elif 'صلح گرا' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,175)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,175])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,75)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,75])
                                                            elif 'دزد' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'دردسرساز' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'شیمیدان' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,175)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,175])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,75)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,75])
                                                            elif 'گرگ برفی' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,300)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,300])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,200)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,200])
                                                            elif 'تش زن' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,500)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,500])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,400)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,400])
                                                            elif 'رمال' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                            elif 'گورکن ' in i:
                                                                if 'زنده' in i:
                                                                    check_user_none = list_i(i,150)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,150])
                                                                elif 'مرده' in i:
                                                                    check_user_none = list_i(i,50)
                                                                    if not check_user_none == None:
                                                                        sw.append([check_user_none,50])
                                                        except Exception as e:
                                                            print(e)
                                            list_rating = '📈 آمار بازی:\n'
                                            for i in sw:
                                                entity_m = await bot.get_entity(int(i[0]))
                                                list_rating += '{0} \t \t {1} 🎉\t\n'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',i[1])
                                            await bot.send_message(event.chat_id,list_rating)
            except Exception as e:
                print(e)
   
        @bot.on(events.NewMessage)
        async def role_white(event):
            if re.search(comment,event.message.message):
                print(event.text)
                if event.message.message.startswith('/sn'):
                    try:
                        if event.sender_id in game['all_user']:
                            message = event.message.message.strip('/sn')
                            if event.sender_id in game['blocked']:
                                await event.reply('شما مسدود هستید')
                            else:
                                entity_m = await bot.get_entity(event.sender_id)
                                game['role_users'][event.sender_id] = '‎[👨🏻‍✈️]{0} : {1} \n'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+entity_m.first_name+'</a>',message)
                                await event.reply('نقشت ثبت شد')
                        else :
                            await event.reply('مطمعن شو تو بازی هستی')
                    except Exception as e:
                        print(e)
                elif event.message.message.startswith('/li'):
                    if game['all_user'] == []:
                       await event.reply('بازی ای ثبت نشده')
                    elif game['role_users'] == {}:
                        if not game['shekarchi'] == 0:
                            txt = ''
                            entity_m = await bot.get_entity(game['shekarchi'])
                            await event.reply(text_game.format('{0}'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+entity_m.first_name+'</a>'),txt))
                        else:
                            await event.reply('نقشی ثبت نشده')
                    else:
                        txt = ''
                        for i in game['role_users']:
                            if i in game['all_user']:
                                txt += game['role_users'][i]
                        if game['shekarchi'] == 0:
                            await event.reply(text_game.format('',txt))
                        else :
                            entity_m = await bot.get_entity(game['shekarchi'])
                            await event.reply(text_game.format('{0}'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+entity_m.first_name+'</a>'),txt))
                elif event.message.message.startswith('/sv'):
                    if event.sender_id == game['shekarchi']:
                        message = event.message.message.split('/sv')
                        game['sv'] = message[1]
                        await event.reply('رای ثبت شد')
                elif event.message.message.startswith('/vt'):
                    if event.sender_id == game['shekarchi']:
                        if game['sv'] == '':
                            await event.reply('رای ثبت نشده')
                        else:
                            await bot.send_message(event.chat_id,'🗳رای {0} \n\n\n روستا از شکار اسکی برو⛷'.format(game['sv']))
                            await asyncio.sleep(5)
                            await bot.send_message(event.chat_id,'🗳رای {0} \n\n\n روستا از شکار اسکی برو⛷'.format(game['sv']))
                            await asyncio.sleep(5)
                            await bot.send_message(event.chat_id,'🗳رای {0} \n\n\n روستا از شکار اسکی برو⛷'.format(game['sv']))
                elif event.message.message == '/vip':
                    if event.sender_id in admin:
                        try:
                            s_admin = redis.get('white_role_vip')
                            if s_admin == None:
                                admins = [614103169]
                                redis.set('white_role_vip',str(admins))
                                await event.reply('کاربر وی ای پی شد')
                            else:
                                admins = eval(s_admin.decode('utf-8'))
                                message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                if message.from_id in admins:
                                    await event.reply('کاربر وی ای پی هست')
                                else:
                                    admins.append(message.from_id)
                                    redis.set('white_role_vip',str(admins))
                                    await event.reply('کاربر وی ای پی شد')
                        except Exception as e:
                            print(e)
                elif event.message.message == '/unvip':
                    if event.sender_id in admin:
                        try:
                            s_admin = redis.get('white_role_vip')
                            admins = eval(s_admin.decode('utf-8'))
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            if message.from_id in admins:
                                admins.remove(message.from_id)
                                redis.set('white_role_vip',str(admins))
                                await event.reply('وی ای پی کاربر برداشته شد')
                            else:
                                await event.reply('کاربر وی ای پی نیست')
                        except Exception as e:
                            print(e)       
                else:
                    admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                    list_admin_gp = []
                    for i in admin_gp:
                        list_admin_gp.append(i.id)
                    s_admin = redis.get('white_role_vip')
                    admins = eval(s_admin.decode('utf-8'))
                    for i in admins:
                        list_admin_gp.append(i)
                    if event.sender_id in list_admin_gp:
                        if event.message.message.startswith('/up'):
                            message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            print(message,event.reply_to_msg_id)
                            if re.search(game_finish,message.text):
                                game['all_user'] = []
                                await event.reply('بازی خوبی بود')
                            elif re.search(game_list,message.text):
                                game['all_user'] = []
                                t = message.text
                                t = t.split('\n')
                                for i in t:
                                    print(i)
                                    if 'tg://user?id=' in i:
                                        if 'زنده' in i:
                                            user_id = i.split('"')[1].split('"')[0]
                                            user_id = user_id.split('tg://user?id=')
                                            user_id = int(user_id[1])
                                            game['all_user'].append(user_id)
                                            print(user_id)
                                print(game)
                                await event.reply('لیست آپدیت شد')
                        elif event.message.message.startswith('/block'):
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            if event.sender_id == message.from_id :
                                await event.reply('داداش خودزنی نکن')
                            else:
                                if not message.from_id in game['blocked']:
                                    game['blocked'].append(message.from_id)
                                    await event.reply('کاربر مسدود شد')
                                else:
                                    await event.reply('از قبل مسدود شده')
                        elif event.message.message.startswith('/unblock'):
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            try:
                                s = game['blocked'].remove(message.from_id)
                                await event.reply('کاربر ازاد شد')
                            except ValueError as e:
                                await event.reply('کاربر مسدود نیست')
                        elif event.message.message.startswith('/shekar'):
                            message = await bot.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                            game['shekarchi'] = message.from_id
                            print(message.from_id)
                            await event.reply('شکارچی بازی شد')

        @client.on(events.NewMessage(pattern=r'ایول بازی شروع شد'))
        async def game_play(event):
            if event.sender_id in bots:
                try:
                    s = 0
                    if event.chat_id == -1001328443567:
                        redis.set('tag_white',str(['off']))
                        try:
                            bet = redis.get('bet_white_ice')
                            bet = eval(bet.decode('utf-8'))
                            try:
                                bet['game_number'] = bet['game_number'] + 1
                            except KeyError as e:
                                if KeyError:
                                    await bot.send_message('aytola','{0}\n{1}'.format(str(e),'game number'))
                            redis.set('bet_white_ice',str(bet))
                            await bot.send_message('aytola','game set {0}'.format(bet['game_number']))
                            await bot.send_message(-1001393884185,'game set {0}'.format(bet['game_number']))
                        except Exception as e:
                            await bot.send_message('aytola',str(e))
                            await bot.send_message('aytola','erorr up game')
                        try:
                            s_message_id =  event.message.id - int(redis.get(int(event.chat_id)+1)) + 100
                            get_message = await client.get_messages(event.chat_id,s_message_id)
                        except Exception as e:
                            print(e)
                        for i in get_message:
                            try:
                                if not i.sender_id in bots:
                                    if not 'بازیکن های زنده' in i.text:
                                        if not 'اعدام بشه' in i.text:
                                            if 'tg://user?id=' in i.text:
                                                await bot.delete_messages(event.chat_id,int(i.id))
                                                print(i.text,str(i.id))
                                                s +=1
                                            if i.text.startswith('@'):
                                                await bot.delete_messages(event.chat_id,int(i.id))
                                                print(i.text,str(i.id))
                                                s +=1
                            except Exception as e:
                                print(e)
                                await bot.send_message('aytola',str(e))
                        await bot.send_message(event.chat_id,'{0} tags were identified and removed'.format(s))
                except Exception as e:
                    await bot.send_message("aytola","BOt in gp "+str(event.chat_id)+"off")
                    print(e)

        @bot.on(events.NewMessage(pattern=r'/stop'))
        async def stop_tag(event):
            admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
            list_admin_gp = []
            for i in admin_gp:
                list_admin_gp.append(i.id)
            s_admin = redis.get('white_role_vip')
            admins = eval(s_admin.decode('utf-8'))
            for i in admins:
                list_admin_gp.append(i)
            if event.sender_id in list_admin_gp:
                redis.set('tag_white',str(['off']))
        
        @client.on(events.NewMessage(pattern=r'یک بازی'))
        async def start_game(event):
            if event.sender_id in bots:
                try:
                    if event.chat_id == -1001328443567:
                        try:
                            if "یک بازی توسط" in event.text:
                                redis.set(int(event.chat_id)+1,event.message.id)
                            if "یک بازی با حالت" in event.text:
                                redis.set(int(event.chat_id)+1,event.message.id)
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
        
        @bot.on(events.NewMessage(pattern=r'/get'))
        async def all_list(event):
            if event.sender_id == 614103169:
                try:
                    message = event.message.message.split(' ')
                    stats_member = redis.get('stats_white_member')
                    stats_member = eval(stats_member.decode('utf-8'))
                    print(event.message.message)
                    group_members = await client.get_participants(-1001328443567)
                    group_member =[]
                    for i in group_members:
                        group_member.append(i.id)
                    if message[1] == 'left':
                        await event.reply('صبر کن الان میگردم لیستو میدمت')
                        list_texts = ''
                        num = 0
                        for i in stats_member:
                            if not i in group_member:
                                print(i)
                                try:
                                    if num == 100:
                                        await event.reply(list_texts)
                                        num = 0
                                        list_texts = ''
                                    user = await bot.get_entity(int(i))
                                    list_texts += '<a href=tg://user?id={0}>{1}</a>\n'.format(user.id,user.first_name)
                                    num += 1
                                except Exception as e:
                                    print(e)
                        await event.reply(list_texts)
                    elif message[1] == 'all':
                        await event.reply('صبر کن الان میگردم لیستو میدمت')
                        list_texts = ''
                        num = 0
                        for i in stats_member:
                            try:
                                if num == 100:
                                    await event.reply(list_texts)
                                    num = 0
                                    list_texts = ''
                                user = await bot.get_entity(int(i))
                                list_texts += '<a href=tg://user?id={0}>{1}</a>\n'.format(user.id,user.first_name)
                                num += 1
                            except Exception as e:
                                print(e)
                        await event.reply(list_texts)
                    elif message[1] == 'now':
                        await event.reply('صبر کن الان میگردم لیستو میدمت')
                        list_texts = ''
                        num = 0
                        for i in stats_member:
                            if i in group_member:
                                try:
                                    if num == 100:
                                        await event.reply(list_texts)
                                        num = 0
                                        list_texts = ''
                                    user = await bot.get_entity(int(i))
                                    list_texts += '<a href=tg://user?id={0}>{1}</a>\n'.format(user.id,user.first_name)
                                    num += 1
                                except Exception as e:
                                    print(e)
                        await event.reply(list_texts)
                except Exception as e:
                    print(e)

        @bot.on(events.NewMessage(pattern=r'/tagall'))
        async def tagall_member(event):
            if event.chat_id == -1001328443567:
                admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                list_admin_gp = []
                for i in admin_gp:
                    list_admin_gp.append(i.id)
                s_admin = redis.get('white_role_vip')
                admins = eval(s_admin.decode('utf-8'))
                for i in admins:
                    list_admin_gp.append(i)
                if event.sender_id in list_admin_gp:
                    check_tag = redis.get('tag_white')
                    if check_tag == None:
                        redis.set('tag_white',str(['off']))
                        await bot.send_message('aytola','bot tag reset')
                    else:
                        check_tag = eval(check_tag.decode('utf-8'))
                        await bot.send_message('aytola',str(check_tag))
                        if check_tag[0] == 'off':
                            stats_member = redis.get('stats_white_member')
                            if not stats_member == None:
                                try:
                                    stats_member = eval(stats_member.decode('utf-8'))
                                    redis.set('tag_white',str(['on']))
                                    for i in stats_member:
                                        check_tags = redis.get('tag_white')
                                        check_tags = eval(check_tags.decode('utf-8'))
                                        if check_tags[0] == 'on':
                                            await bot.send_message(event.chat_id,'<a href=tg://user?id='+str(i)+'>'+'عشقم'+"</a> "+matn[random.randint(0,len(matn)-1)]+" "+emoji[random.randint(0,len(emoji)-1)])                                                                         
                                            await asyncio.sleep(1)
                                        elif check_tags[0] == 'off':
                                            await bot.send_message(event.chat_id,'تگ ربات متوقف شد')
                                            break
                                    redis.set('tag_white',str(['off']))
                                except Exception as e:
                                    print(e)
                        elif check_tag[0] == 'on':
                            await bot.send_message(event.chat_id,'داداش دارم تگ میکنم دست از سرم برمیداری یا نه؟')
    
        @client.on(events.NewMessage(pattern=r'بعد از یک مبارزه طولانی حالا آرامش خاصی در روستا حکم فرماست.روستاییان بردن'))
        async def game_1(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('ros')
                    redis.set('game_bord','ros')
        
        @client.on(events.NewMessage(pattern=r'کل روستا پر شده از افراد فرقه گرا!! فرقه گراها بردن'))
        async def game_2(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('ferghe')
                    redis.set('game_bord','ferghe')
        
        @client.on(events.NewMessage(pattern=r'گرگا بردن!'))
        async def game_3(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('gorg')
                    redis.set('game_bord','gorg')
        
        @client.on(events.NewMessage(pattern=r'تنها آتش زن باقی موند که بر روی تپه ای از خاکستر ایستاده. آتش زن برنده شد...'))
        async def game_4(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('atish')
                    redis.set('game_bord','atish')
        
        @client.on(events.NewMessage(pattern=r'فقط قاتل زنجیره ای روانی زنده موند و برنده شد'))
        async def game_5(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('ghatel')
                    redis.set('game_bord','ghatel')

        @client.on(events.NewMessage(pattern=r'عاشقا برنده شدن'))
        async def game_6(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('lover')
                    redis.set('game_bord','lover')

        @client.on(events.NewMessage(pattern=r'ریدین بابا این چه وضعشه! همه مردن و هیشکی برنده نشد'))
        async def game_7(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('lose')
                    redis.set('game_bord','lose')

        @client.on(events.NewMessage(pattern=r'خاک تو سرتون! منافق رو کشتین و اون برنده شد همه باختن'))
        async def game_7(event):
            if event.sender_id in bots:
                if event.chat_id == -1001328443567:
                    game_stats('monafegh')
                    redis.set('game_bord','monafegh')

        @bot.on(events.NewMessage(pattern=r'/getpointbet'))
        async def point_bet(event):
            try:
                def list_i(user):
                    i = user.split('"')[1].split('"')[0]
                    i = i.split('tg://user?id=')
                    i = int(i[1])
                    list_m = redis.get(i)
                    list_m = eval(list_m.decode('utf-8'))
                    game_bord = redis.get('game_bord')
                    game_bord = game_bord.decode('utf-8')
                    user_bet = redis.get('{0}bet'.format(i))
                    user_bet = eval(user_bet.decode('utf-8'))
                    bet = redis.get('bet_white_ice')
                    bet = eval(bet.decode('utf-8'))
                    check_games = user_bet['bet_one'].split(':')
                    if int(check_games[1]) < bet['game_number']:
                        if not user_bet['bet_two'] == '':
                            check_gamess = user_bet['bet_two'].split(':')
                            if int(check_gamess[1]) >= bet['game_number']:
                                user_bet['bet_one'] = user_bet['bet_two']
                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                user_bet['bet_two'] = ''
                                user_bet['bet_two_snow'] = 0
                                user_bet['game'] = 1
                                redis.set('{0}bet'.format(i),str(user_bet))
                            else:
                                user_bet['bet_one'] = ''
                                user_bet['bet_one_snow'] = 0
                                user_bet['bet_two'] = ''
                                user_bet['bet_two_snow'] = 0
                                user_bet['game'] = 0
                                redis.set('{0}bet'.format(i),str(user_bet))
                    if not user_bet == None:
                        if game_bord == 'ros':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'ros':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['ros'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'ferghe':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'ferghe':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['ferghe'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'gorg':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'gorg':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['gorg'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'ghatel':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'ghatel':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['ghatel'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'atish':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'atish':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['atish'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'lover':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'lover':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['lover'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'monafegh':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'monafegh':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['monafegh'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                        elif game_bord == 'lose':
                            if not user_bet['bet_one'] == '':
                                try:
                                    check_games = user_bet['bet_one'].split(':')
                                    if int(check_games[1]) == bet['game_number']:
                                        if check_games[0] == 'lose':
                                            bord = round((int(user_bet['bet_one_snow']) * float(bet['lose'])))
                                            list_m['snow'] = list_m['snow'] + bord
                                            if not user_bet['bet_two'] == '':
                                                user_bet['bet_one'] = user_bet['bet_two']
                                                user_bet['bet_one_snow'] = user_bet['bet_two_snow']
                                                user_bet['bet_two'] = ''
                                                user_bet['bet_two_snow'] = 0
                                                user_bet['game'] = 1
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            else:
                                                user_bet['bet_one'] = ''
                                                user_bet['bet_one_snow'] = 0
                                                user_bet['game'] = 0
                                                redis.set('{0}bet'.format(i),str(user_bet))
                                                test = redis.set(i,str(list_m))
                                            user = [i,bord]
                                            return user
                                except Exception as e:
                                    print(e)
                    else:
                        return None
                if event.text.startswith('/getpointbet'):
                    admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                    list_admin_gp = []
                    for i in admin_gp:
                        list_admin_gp.append(i.id)
                    if event.sender_id in list_admin_gp:
                        redis_get = redis.get('chat_{0}_getlist_task_bet'.format(event.chat_id))
                        if redis_get == None:
                            redis.set('chat_{0}_getlist_task_bet'.format(event.chat_id),'[{0}]'.format(event.reply_to_msg_id))
                        else :
                            redis_get = redis.get('chat_{0}_getlist_task_bet'.format(event.chat_id)).decode('utf-8')
                            list_play = eval(redis_get)
                            if event.reply_to_msg_id in list_play:
                                await client.connect()
                                message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                if 'مدت زمان بازی' in message.text:
                                    print('old message')
                            else:
                                if not event.reply_to_msg_id == None:
                                    message = await client.get_messages(event.chat_id,ids=event.reply_to_msg_id)
                                    if 'مدت زمان بازی' in message.text:
                                        #if message.from_id in bots:
                                        if message.from_id:
                                            if len(list_play) == 150:
                                                list_play = []
                                            list_play.append(event.reply_to_msg_id)
                                            redis.set('chat_{0}_getlist_task_bet'.format(event.chat_id),'{0}'.format(list_play))
                                            t = message.text
                                            t = t.split('\n')
                                            sw = []
                                            for i in t:
                                                if 'tg://user?id=' in i:
                                                    try:
                                                        check_user_none = list_i(i)
                                                        if not check_user_none == None:
                                                            sw.append(check_user_none)
                                                    except Exception as e:
                                                        print(e)
                                            list_rating = 'برنده های شرط بندی 💥\n'
                                            print(1,sw)
                                            for i in sw:
                                                entity_m = await bot.get_entity(int(i[0]))
                                                print(entity_m)
                                                list_rating += '🔥{0} : {1} \n'.format('<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',i[1])
                                            print(3,list_rating)
                                            await bot.send_message(event.chat_id,list_rating) 
                                            await bot.send_message(-1001393884185,list_rating)
            except Exception as e:
                print(e)
        
        @bot.on(events.NewMessage(pattern=r'/betcheck',func=lambda e: e.is_private))
        async def testbetcheck(event):
            bet = redis.get('bet_white_ice')
            bet = eval(bet.decode('utf-8'))
            game_all = bet['game_number']
            user_bet = redis.get('{0}bet'.format(event.sender_id))
            user_bet = eval(user_bet.decode('utf-8'))
            if not user_bet['bet_one'] == '':
                game1 = user_bet['bet_one'].split(':')
                game1_number = game1[1]
                game1_snow = user_bet['bet_one_snow']
                game1_zarib = bet[game1[0]]
                if not user_bet['bet_two'] == '':
                    game2 = user_bet['bet_two'].split(':')
                    game2_number = game2[1]
                    game2_snow = user_bet['bet_two_snow']
                    game2_zarib = bet[game2[0]]
                else:
                    game2_number = 0
                    game2_snow = 0
                    game2_zarib = 0
            else:
                game1_number = 0
                game1_snow = 0
                game1_zarib = 0
                game2_number = 0
                game2_snow = 0
                game2_zarib = 0
            text = '''📌لیست شرط بندی ها
 
♻️بازی کنونی شماره {0}
 
🖇شرط اول : 
بازی {1} ، {2} ❄️، ضریب {3} 
📎 شرط دوم : 
بازی {4} ،{5} ❄️ ، ضریب {6}

Good luck ✨'''
            
            await event.reply(text.format(game_all,game1_number,game1_snow,game1_zarib,game2_number,game2_snow,game2_zarib))
        
        @bot.on(events.NewMessage(pattern=r'/bestsallmember'))
        async def testbestall(event):
            if event.sender_id == 614103169:
                try:
                    list_mt = eval(redis.get('task{0}'.format(-1001328443567)).decode('utf-8'))
                    all_member = {}
                    for i in list_mt:
                        try:
                            all_member[i] = list_mt[i]['point']
                        except Exception as e:
                            print(e)
                    mem = sorted(all_member.items(), key=lambda x: x[1], reverse=True)
                    text_best = '''all member bests:'''
                    number_best = 0
                    number_bests = 1
                    for i in mem:
                        try:
                            entity_m = await bot.get_entity(int(i[0]))
                            if entity_m.first_name:
                                text_best += '\n🙋🏻‍♂️{0}: {1} --->{2}'.format(number_bests,'<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',i[1])
                                number_best += 1
                                number_bests += 1
                                if number_best == 100:
                                    await event.reply(text_best)
                                    number_best = 0
                                    text_best = '''all member bests:'''
                                print(i[0], i[1])
                        except Exception as e:
                            print(e)
                    await event.reply(text_best)
                except Exception as e:
                    print(e)
        
        @bot.on(events.NewMessage(pattern=r'/bests'))
        async def testbewst(event):
            if event.chat_id == -1001328443567:
                admin_gp = await bot.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
                list_admin_gp = []
                for i in admin_gp:
                    list_admin_gp.append(i.id)
                s_admin = redis.get('white_role_vip')
                admins = eval(s_admin.decode('utf-8'))
                for i in admins:
                    list_admin_gp.append(i)
                if event.sender_id in list_admin_gp:
                    list_mt = eval(redis.get('task{0}'.format(-1001328443567)).decode('utf-8'))
                    all_member = {}
                    for i in list_mt:
                        try:
                            all_member[i] = list_mt[i]['point']
                        except Exception as e:
                            print(e)
                    mem = sorted(all_member.items(), key=lambda x: x[1], reverse=True)
                    text_best = '''<b> 🏆لیــست کاربران برتر:</b>\n'''
                    number_best = 1
                    emoji_number = ''
                    emoji_bes = ''
                    for i in mem:
                        if number_best == 6:
                            break 
                        entity_m = await bot.get_entity(int(i[0]))
                        if number_best == 1:
                            emoji_number = '➊'
                            emoji_bes = '🥇'
                        elif number_best == 2:
                            emoji_number = '➋'
                            emoji_bes = '🥈'
                        elif number_best == 3:
                            emoji_number = '➌'
                            emoji_bes = '🥉'
                        elif number_best == 4:
                            emoji_number = '➍'
                            emoji_bes = '🏅'
                        elif number_best == 5:
                            emoji_number = '➎'
                            emoji_bes = '🎖'
                        text_best += '\n {0} ⤳ {1}    {2}  {3}\n'.format(emoji_number,'<a href=tg://user?id='+str(entity_m.id)+'>'+ entity_m.first_name+'</a>',i[1],emoji_bes)
                        number_best += 1
                        print(i[0], i[1])
                    text_best += '\n\n{0}'.format('<b>♛Good luck💜♬</b>')
                    await event.reply(text_best)
        
        @bot.on(events.NewMessage)
        async def mamor(event):
            if event.chat_id == -1001328443567:
                try:
                    time_pl = eval(redis.get('time_police').decode('utf-8'))
                    if time_pl['min'] == 1:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 60:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 2:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 360:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 3:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 1440:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 4:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 4125:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 5:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 7125:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 6:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 17125:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))
                    elif time_pl['min'] == 7:
                        time_now = time_pl['time']
                        if round(time.time() - time_now) >= 87125:
                            if time_pl['check'] == 1:
                                time_pl['check'] = 0
                                redis.set('time_police',str(time_pl))
                                text_plocie = '''🚨🚨🚨
تــوجه کنید 
مامــور ویژه دولت اینجاستـ👮🏻‍♂️
به مدت چهـ۴ـار دقیـقهـ⏳ 
میـزان برف پنـ۵ـج نفـر چک میکنهـ🔍'''
                                await bot.send_message(event.chat_id,text_plocie)
                                
                            if round(time.time() - time_now) >= 240:
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            elif time_pl['num'] >= 5 :
                                times = [1,2,3,4,5,6,7]
                                time_police = {'time':time.time(),'min':rn.choice(times),'num':0,'check':1}
                                redis.set('time_police',str(time_police))
                            else:
                                if not event.sender_id in bot_list:
                                    list_m1 = redis.get(event.sender_id)
                                    list_m1 = eval(list_m1.decode('utf-8'))
                                    time_pl['num'] = time_pl['num'] + 1
                                    redis.set('time_police',str(time_pl))
                                    check_pol = 0
                                    if list_m1['snow'] >= 2000:
                                        list_m1['snow'] = round(list_m1['snow'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if list_m1['snowman'] >= 50:
                                        list_m1['snowman'] = round(list_m1['snowman'] / 2)
                                        redis.set(event.sender_id,str(list_m1))
                                        check_pol = 1
                                    if check_pol == 1:
                                        user = await bot.get_entity(event.sender_id)
                                        text_polic = '''اوه چه روز بدیه براتـ📛
مامور دولت امروز میخاد میزان برف های تورو چک کنهـ⚠️

تعداد برف و ادم برفی  {}  نصف میشهـ👿'''
                                        await event.reply(text_polic.format(' <a href=tg://user?id='+str(user.id)+'>'+user.first_name+"</a> "))

                except:
                    time_police = {'time':time.time(),'min':5,'num':0,'check':0}
                    redis.set('time_police',str(time_police))
        
    except Exception as e:
        print(e)
    


asyncio.run(main())
client.start()
client.run_until_disconnected() 
bot.start()
bot.run_until_disconnected()
