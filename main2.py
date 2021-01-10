import requests
import random
from time import sleep

tg_token = "TOKEN"
sfw_channel_1 = "@example"
sfw_channel_2 = "@example"
sfw_channel_3 = "@example"
sfw_channel_4 = "@example"
sfw_channel_5 = "@example"
sfw_channel_6 = "@example"


nsfw_channel_1 = "-example"
nsfw_channel_2 = "-example"

while True:
    try:
        def sfwWaifu(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/sfw/waifu").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23waifu")
                sleep(60)
            except BaseException:
                print("Ошибка первой функции")

        def sfwNeko(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/sfw/neko").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23neko")
                sleep(60)
            except BaseException:
                print("Ошибка второй функции")

        def sfwShinobu(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/sfw/shinobu").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23shinobu")
                sleep(60)
            except BaseException:
                print("Ошибка третьей функции")

        def sfwMegumin(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/sfw/megumin").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23megumin")
                sleep(60)
            except BaseException:
                print("Ошибка четвертой функции")

        def sfwKiss(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/sfw/kiss").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/senddocument?chat_id=" + channel + "&document=" + picURL + "&caption=%23kiss")
                sleep(60)
            except BaseException:
                print("Ошибка пятой функции")

        def sfwRandom(channel):
            try:
                picURL = "https://raw.githubusercontent.com/VanXNF/Anime-Dataset/main/Anime/Anime_" + str(random.randint(1, 309)) + ".jpg"
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23random")
                sleep(60)
            except BaseException:
                print("Ошибка шестой функции, git")

        def nsfwWaifu(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/nsfw/waifu").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23waifu")
                sleep(60)
            except BaseException:
                print("Ошибка седьмой функции")

        def nsfwNeko(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/nsfw/neko").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23neko")
                sleep(60)
            except BaseException:
                print("Ошибка восьмой функции")

        def sfwTrap(channel):
            try:
                picURL = requests.get(f"https://waifu.pics/api/nsfw/trap").json()['url']
                r = requests.get(
                    "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL)
                sleep(60)
            except BaseException:
                print("Ошибка девятой функции")

        def sendsfwMega(channel):
            link = requests.get("https://nekos.life/api/v2/img/baka").json()['url']
            lastID = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/senddocument?chat_id=" + channel + "&document=" + link + "&caption=MIKU%20presents%20you%20today%27s%20best%20channels%20(*≧ω≦*)%20Check%20out%20all%20of%20them%20and%20find%20something%20new!%0A••• ••• •••%0A%5B💛%20HENTAI%2018%2B%20(☞˵%20͡°%20͜ʖ%20͡°˵)☞%20💕%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FR8ofgmz2qDt0SCOr)%0A•••%20•••%20•••%20%0A%5B💖🌈LOLI%20HENTAI🍭💖%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FUJaxOdgvjL5txv8w)%0A•••%20•••%20•••%20%0A%5B🌈💦Трапики💦🌈%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FUIMpo9wgMUoFYvI3)%0A•••%20•••%20•••%20%0A🌼%20%5BWaifu%20Land%5D(https%3A%2F%2Ft.me%2FWaifuLandjk)%0A•••%20•••%20•••%20%0A🌼%20%5BNeko%20love%5D(https%3A%2F%2Ft.me%2FNekolovejk)%0A•••%20•••%20•••%20%0A🌼%20%5BSweat%20Nekos%5D(https%3A%2F%2Ft.me%2FSweatNekosjk)%0A•••%20•••%20•••%20%0A🌼%20%5BSenpai%5D(https%3A%2F%2Ft.me%2FSenpaijkearnsl)%0A•••%20•••%20•••%20%0A🌼%20%5BАниме%20Картинки%5D(https%3A%2F%2Ft.me%2Fanimepicjk)%0A•••%20•••%20•••%20%0A🌼%20%5BТвоя%20Вайфу%5D(https%3A%2F%2Ft.me%2Fyourwaifujk)%0A•••%20•••%20•••%20&parse_mode=markdown").json()['result']['message_id']
            sleep(30)
            return lastID


        def delMega(lastid, channel):
            try:
                delete = requests.get(
                    f"https://api.telegram.org/bot" + tg_token + "/deleteMessage?chat_id=" + channel + "&message_id=" + str(lastid))
                sleep(30)
            except BaseException:
                print("Ошибка удаления меги")

        # day
        # NSFW
        lastID_1 = []
        lastID_2 = []
        lastID_3 = []
        lastID_4 = []
        lastID_5 = []
        lastID_6 = []
        lastID_7 = []
        lastID_8 = []

        for i in range(2):
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwWaifu(sfw_channel_1)
            sfwWaifu(sfw_channel_2)
            sfwWaifu(sfw_channel_3)
            sfwWaifu(sfw_channel_4)
            sfwWaifu(sfw_channel_5)
            sfwWaifu(sfw_channel_6)
            print("закончил с SFW")
            sleep(3600)

            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwNeko(sfw_channel_1)
            sfwNeko(sfw_channel_2)
            sfwNeko(sfw_channel_3)
            sfwNeko(sfw_channel_4)
            sfwNeko(sfw_channel_5)
            sfwNeko(sfw_channel_6)
            print("закончил с SFW")
            sleep(3600)

            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwShinobu(sfw_channel_1)
            sfwShinobu(sfw_channel_2)
            sfwShinobu(sfw_channel_3)
            sfwShinobu(sfw_channel_4)
            sfwShinobu(sfw_channel_5)
            sfwShinobu(sfw_channel_6)
            print("закончил с SFW")
            sleep(3600)

            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwMegumin(sfw_channel_1)
            sfwMegumin(sfw_channel_2)
            sfwMegumin(sfw_channel_3)
            sfwMegumin(sfw_channel_4)
            sfwMegumin(sfw_channel_5)
            sfwMegumin(sfw_channel_6)
            print("закончил с SFW")
            sleep(3600)

            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwKiss(sfw_channel_1)
            sfwKiss(sfw_channel_2)
            sfwKiss(sfw_channel_3)
            sfwKiss(sfw_channel_4)
            sfwKiss(sfw_channel_5)
            sfwKiss(sfw_channel_6)
            print("закончил с SFW")
            sleep(3600)

            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sfwRandom(sfw_channel_1)
            sfwRandom(sfw_channel_2)
            sfwRandom(sfw_channel_3)
            sfwRandom(sfw_channel_4)
            sfwRandom(sfw_channel_5)
            sfwRandom(sfw_channel_6)
            print("закончил с SFW")
            # NSFW
            nsfwWaifu(nsfw_channel_1)
            nsfwNeko(nsfw_channel_1)
            sfwTrap(nsfw_channel_2)
            print("закончил с NSFW")
            sleep(3600)
            
            # Мега
            print("Отправляю мегу")
            try:
                lastID_1.append(sendsfwMega(sfw_channel_1))
                lastID_2.append(sendsfwMega(sfw_channel_2))
                lastID_3.append(sendsfwMega(sfw_channel_3))
                lastID_4.append(sendsfwMega(sfw_channel_4))
                lastID_5.append(sendsfwMega(sfw_channel_5))
                lastID_6.append(sendsfwMega(sfw_channel_6))
                lastID_7.append(sendsfwMega(nsfw_channel_1))
                lastID_8.append(sendsfwMega(nsfw_channel_2))
                print("Отправил всю мегу")
            except BaseException:
                print("Ошибка отправки меги")
            # конец меги
            print("Сплю около 4х часов")
            sleep(10800)
        for i in range(2):
            delMega(lastID_1[i], sfw_channel_1)
            delMega(lastID_2[i], sfw_channel_2)
            delMega(lastID_3[i], sfw_channel_3)
            delMega(lastID_4[i], sfw_channel_4)
            delMega(lastID_5[i], sfw_channel_5)
            delMega(lastID_6[i], sfw_channel_6)
            delMega(lastID_7[i], nsfw_channel_1)
            delMega(lastID_8[i], nsfw_channel_2)
        print("Мега удалена")
    except BaseException:
        print("Опять ошибки...Повторяю хаос...")
        sleep(300)
