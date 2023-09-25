from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
import login_info

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)

navegador.get(login_info.website)

navegador.find_element('xpath','//*[@id="txtLogin"]').send_keys(login_info.login)

navegador.find_element('xpath','//*[@id="txtSenha"]').send_keys(login_info.send_keys)

navegador.find_element('xpath','//*[@id="btnEntrar"]').click()

navegador.find_element('xpath', '//*[@id="imagem18"]').click()

navegador.find_element('xpath', '//*[@id="imagem56"]').click()

# Como posso controlar a janela para marcação apropriada do ponto?
