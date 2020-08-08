from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Kauane\Desktop\geckodriver\geckodriver.exe')

    #   //input[@name='username']
    #   //input[@name='password']
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=pt-br')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.usuario)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.senha)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('memesbr')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
                print('Curti + 1')
                time.sleep(19)
            except Exception as e:
                print('deu erro' + str(e))
                time.sleep(5)



RafaelBot = InstagramBot('rafaelvieiral_' , 'hjhhjbh')
RafaelBot.login()
