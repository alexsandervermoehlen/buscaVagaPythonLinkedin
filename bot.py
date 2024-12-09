import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# instancia o chromedriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL a ser chamada no navegador chrome
browser.get('https://www.linkedin.com/login')

# preenche email
input_email = browser.find_element(By.ID, "username")
input_email.send_keys("teste@teste.com") # insira o email da sua conmta do linkedin

# Preenche senha
input_senha = browser.find_element(By.ID, "password")
input_senha.send_keys("teste") #insira a senha da sua conta

# desmarca para manter conectado
remember = browser.find_element(By.CSS_SELECTOR, "label[for='rememberMeOptIn-checkbox']")
remember.click()

# Clica no botão para logar
time.sleep(5)
btn_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
btn_login.click()

# Efetua busca de vagas
busca = browser.find_element(By.CSS_SELECTOR,"input[placeholder='Pesquisar']")
busca.send_keys("Python") #insira o item da vaga que deseja procurar
busca.send_keys(Keys.RETURN)

# filtra vagas clicando no botão vagas
time.sleep(5)
filtro_vagas = browser.find_element(By.CSS_SELECTOR, "button[aria-pressed='false']")
filtro_vagas.click()

# apenas mantem um input para que o programa nãi s eencerre sozinho
input('')