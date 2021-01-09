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
            picURL = requests.get(f"https://waifu.pics/api/sfw/waifu").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23waifu")


        def sfwNeko(channel):
            picURL = requests.get(f"https://waifu.pics/api/sfw/neko").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23neko")


        def sfwShinobu(channel):
            picURL = requests.get(f"https://waifu.pics/api/sfw/shinobu").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23shinobu")


        def sfwMegumin(channel):
            picURL = requests.get(f"https://waifu.pics/api/sfw/megumin").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23megumin")


        def sfwKiss(channel):
            picURL = requests.get(f"https://waifu.pics/api/sfw/kiss").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/senddocument?chat_id=" + channel + "&document=" + picURL + "&caption=%23kiss")


        def sfwRandom(channel):
            picURL = "https://raw.githubusercontent.com/VanXNF/Anime-Dataset/main/Anime/Anime_" + str(
                random.randint(1, 309)) + ".jpg"
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23random")


        def nsfwWaifu(channel):
            picURL = requests.get(f"https://waifu.pics/api/nsfw/waifu").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23waifu")


        def nsfwNeko(channel):
            picURL = requests.get(f"https://waifu.pics/api/nsfw/neko").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23neko")


        def sfwTrap(channel):
            picURL = requests.get(f"https://waifu.pics/api/nsfw/trap").json()['url']
            r = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL)


        def sendsfwMega(channel):
            link = requests.get("https://nekos.life/api/v2/img/baka").json()['url']
            url = requests.get(
                "https://api.telegram.org/bot" + tg_token + "/senddocument?chat_id=" + channel + "&document=" + link + "&caption=MIKU%20presents%20you%20today%27s%20best%20channels%20(*≧ω≦*)%20Check%20out%20all%20of%20them%20and%20find%20something%20new!%0A••• ••• •••%0A%5B💛%20HENTAI%2018%2B%20(☞˵%20͡°%20͜ʖ%20͡°˵)☞%20💕%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FR8ofgmz2qDt0SCOr)%0A•••%20•••%20•••%20%0A%5B💖🌈LOLI%20HENTAI🍭💖%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FUJaxOdgvjL5txv8w)%0A•••%20•••%20•••%20%0A%5B🌈💦Трапики💦🌈%5D(https%3A%2F%2Ft.me%2Fjoinchat%2FUIMpo9wgMUoFYvI3)%0A•••%20•••%20•••%20%0A🌼%20%5BWaifu%20Land%5D(https%3A%2F%2Ft.me%2FWaifuLandjk)%0A•••%20•••%20•••%20%0A🌼%20%5BNeko%20love%5D(https%3A%2F%2Ft.me%2FNekolovejk)%0A•••%20•••%20•••%20%0A🌼%20%5BSweat%20Nekos%5D(https%3A%2F%2Ft.me%2FSweatNekosjk)%0A•••%20•••%20•••%20%0A🌼%20%5BSenpai%5D(https%3A%2F%2Ft.me%2FSenpaijkearnsl)%0A•••%20•••%20•••%20%0A🌼%20%5BАниме%20Картинки%5D(https%3A%2F%2Ft.me%2Fanimepicjk)%0A•••%20•••%20•••%20%0A🌼%20%5BТвоя%20Вайфу%5D(https%3A%2F%2Ft.me%2Fyourwaifujk)%0A•••%20•••%20•••%20&parse_mode=markdown")


        # day
        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwWaifu(sfw_channel_1)
        sleep(60)
        sfwWaifu(sfw_channel_2)
        sleep(60)
        sfwWaifu(sfw_channel_3)
        sleep(60)
        sfwWaifu(sfw_channel_4)
        sleep(60)
        sfwWaifu(sfw_channel_5)
        sleep(60)
        sfwWaifu(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwNeko(sfw_channel_1)
        sleep(60)
        sfwNeko(sfw_channel_2)
        sleep(60)
        sfwNeko(sfw_channel_3)
        sleep(60)
        sfwNeko(sfw_channel_4)
        sleep(60)
        sfwNeko(sfw_channel_5)
        sleep(60)
        sfwNeko(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwShinobu(sfw_channel_1)
        sleep(60)
        sfwShinobu(sfw_channel_2)
        sleep(60)
        sfwShinobu(sfw_channel_3)
        sleep(60)
        sfwShinobu(sfw_channel_4)
        sleep(60)
        sfwShinobu(sfw_channel_5)
        sleep(60)
        sfwShinobu(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwMegumin(sfw_channel_1)
        sleep(60)
        sfwMegumin(sfw_channel_2)
        sleep(60)
        sfwMegumin(sfw_channel_3)
        sleep(60)
        sfwMegumin(sfw_channel_4)
        sleep(60)
        sfwMegumin(sfw_channel_5)
        sleep(60)
        sfwMegumin(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwKiss(sfw_channel_1)
        sleep(60)
        sfwKiss(sfw_channel_2)
        sleep(60)
        sfwKiss(sfw_channel_3)
        sleep(60)
        sfwKiss(sfw_channel_4)
        sleep(60)
        sfwKiss(sfw_channel_5)
        sleep(60)
        sfwKiss(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        sleep(60)
        print("закончил с NSFW")
        sfwRandom(sfw_channel_1)
        sleep(60)
        sfwRandom(sfw_channel_2)
        sleep(60)
        sfwRandom(sfw_channel_3)
        sleep(60)
        sfwRandom(sfw_channel_4)
        sleep(60)
        sfwRandom(sfw_channel_5)
        sleep(60)
        sfwRandom(sfw_channel_6)
        print("закончил с SFW")
        sleep(3600)

        # NSFW
        nsfwWaifu(nsfw_channel_1)
        sleep(60)
        nsfwNeko(nsfw_channel_1)
        sleep(60)
        sfwTrap(nsfw_channel_2)
        print("закончил с NSFW")
        #Мега
        sleep(60)
        print("Отправляю мегу")
        sendsfwMega(sfw_channel_1)
        sleep(60)
        sendsfwMega(sfw_channel_2)
        sleep(60)
        sendsfwMega(sfw_channel_3)
        sleep(60)
        sendsfwMega(sfw_channel_4)
        sleep(60)
        sendsfwMega(sfw_channel_5)
        sleep(60)
        sendsfwMega(sfw_channel_6)
        sleep(60)
        sendsfwMega(nsfw_channel_1)
        sleep(60)
        sendsfwMega(nsfw_channel_2)
        print("Отправил всю мегу")
        print("Сплю около 3х часов")
        #конец меги
        sleep(8800)
    except BaseException:
        print("Опять ошибки...Повторяю хаос...")
        sleep(300)
