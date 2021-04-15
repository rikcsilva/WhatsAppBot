# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navegar até whats web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# Definir cotatos e grupos a serem enviados
contatos = ['Bloqued', 'Eita']
mensagem = 'Mensagem de teste WhatsAppBot!'
# buscar grupos ou contatos
def buscar_contato(contato):
	campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
	time.sleep(3)
	campo_pesquisa.click()
	time.sleep(3)
	campo_pesquisa.send_keys(contato)
	time.sleep(3)
	campo_pesquisa.send_keys(Keys.ENTER)
# enviar mensagens
def enviar_mensagem:
	campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
	time.sleep(3)
	#para indexar o segundo campo, pois o endereço é igual para buscar contato e enviar mensagem
	campo_mensagem[1].click()
	time.sleep(3)
	campo_mensagem[1].send_keys(mensagem)
	time.sleep(3)
	campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
	buscar_contato(contato)
	enviar_mensagem(mensagem)
