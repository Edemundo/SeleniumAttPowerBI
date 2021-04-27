from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
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
    
    centralvagas_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-virtual-scroll-content-wrapper']"))
    )
    
    dashboards_button = driver.find_elements_by_css_selector(".row.ng-star-inserted")[1] 

    
    action.move_to_element(dashboards_button)

    action.perform()
    
    print("deu bom")
    

    
#     update_button = driver.find_element_by_css_selector(".quick-action-button.ng-star-inserted")
    
    

    buttonatualizarpainel_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@title='Atualizar agora']"))
    )
    
    buttonatualizarpainel_elem.click()

    print("deu bom")

except Exception as e:
    print(e)
    print("deu ruim")
