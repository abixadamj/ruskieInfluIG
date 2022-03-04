from pyexpat.errors import messages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import math
from random import randrange
import sys

class InstagramBot:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.bot = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def login(self):
        print('STARTUJEMY')
        time.sleep(2)
        print("LOGOWANIE...")
        print("Wpisz nazwę użytkownika:")
        usernm = input()
        print("Wpisz hasło:")
        passwd = input()
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(usernm)
        password.send_keys(passwd)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(5)
        try: 
            bot.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except: 
            bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(8)
        

    def write_message(self):

        messages = [
            'В Украине российские солдаты убивают мирных жителей. Не будьте равнодушны и не дайте Путину забрать отцов и мужей украинок!',
            '24 февраля Россия начала вторжение в Украину. Гибнут невинные люди. Я пишу это для того, чтобы российское общество осознало, что Россия является агрессором.',
            'Россия убивает невинных людей в Украине. Я знаю, что в настоящее время в России существует дезинформация, поэтому, пожалуйста, передайте это сообщение!',
            '24 февраля Россия напала на Украину. Уже погибло более 2000 мирных жителей. Перешлите это сообщение, чтобы положить конец дезинформации в России!',
            'Русские друзья! Я пишу вам, чтобы вы знали, что ваша армия начала вторжение в Украину и убивает невинных людей! Пожалуйста, передайте это сообщение!'
        ]   

        print('LOGOWANIE PRZEBIEGŁO POMYŚLNIE')
        time.sleep(3)
        print("Wpisz nazwę na IG osoby do której obserwatorów będziemy pisać:")
        targetName = input()
        print("Wpisz do ilu osób bot ma napisać:")
        peopleAmount = input()
        print("Bot będzie działał teraz w tle. Możesz go zostawić.")
        bot = self.bot
        bot.get('https://www.instagram.com/'+targetName)
        time.sleep(5)
        bot.find_element_by_xpath('//a[@href ="/'+ targetName + '/followers/"]').click()
        time.sleep(5)
        for i in range(1, 10):
            following_list = bot.find_element_by_class_name('isgrP')
            bot.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_list)
            time.sleep(2)
        following = bot.find_elements_by_class_name('_0imsa')
        all_following = [elem.get_attribute('title') for elem in following]

        visitedProfiles = []
        for i in range(1, int(peopleAmount)):
            rand = randrange(len(all_following))
            profile = all_following[rand]
            if profile in visitedProfiles:
                time.sleep(3)
            else:
                bot.get('https://www.instagram.com/direct/new/')
                time.sleep(3)
                person = bot.find_element_by_name('queryBox')
                person.clear()
                person.send_keys(profile)
                time.sleep(3)
                bot.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button').click()
                time.sleep(3)
                bot.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button').click()
                time.sleep(5)

                randomMessageIndex = randrange(5)
                print(messages[randomMessageIndex])
                textArea = bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                textArea.clear()
                textArea.send_keys(messages[randomMessageIndex])
                textArea.send_keys(Keys.RETURN)
                time.sleep(5)

                visitedProfiles.append(profile)


user = InstagramBot()

user.login()

user.write_message()

