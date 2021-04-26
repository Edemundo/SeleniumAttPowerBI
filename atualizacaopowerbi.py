from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
email = "paineldevagas@prefeitura.sp.gov.br"
senha = "C#p4$21V"

driver.get("https://app.powerbi.com/")
action = ActionChains(driver)

try:
    entrar_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Entrar"))
    )
    entrar_elem.click()

    username_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='loginfmt']"))
    )
    username_elem.clear()
    username_elem.send_keys(email)

    avancar_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Avançar']"))
    )
    avancar_elem.click()

    senha_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']"))
    )
    senha_elem.clear()
    senha_elem.send_keys(senha)

    entrar2_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Entrar']"))
    )
    entrar2_elem.click()

    naoconectar_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Não']"))
    )
    naoconectar_elem.click()

    workspaces_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='workspacesPaneExpander switcher' "
                                        + "and @aria-label='Workspaces']"))
    )
    workspaces_elem.click()

    centralvagas_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='CENTRAL DE VAGAS']"))
    )
    centralvagas_elem.click()

    buttonatualizarpainel_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Atualizar agora']"))
    )

    action.move_to_element(buttonatualizarpainel_elem).click_and_hold().perform().click().perform()

    print("tudo certo")

except Exception as e:
    print(e)
    print("deu ruim")
