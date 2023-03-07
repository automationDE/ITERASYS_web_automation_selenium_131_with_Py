import pytest
import os
import pytest
# um padrao para o Pytest executar no início e no final dos testes
from selenium import webdriver

from pages import login_page
from pages.login_page import LoginPage


# um padrão para o PyTest executar no início e no final dos testes
@pytest.fixture
def login(request):  # deixou de receber a request para receber diretamente a função driver
    # anteriormente apontavamos o Chrome Driver diretamente
    # _chromedriver = 'vendor/chromedriver.exe'
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
    print('O CWD ENCONTRADO É:' + _chromedriver)

    #return login_page.LoginPage(driver)  # instanciando a classe LoginPage e passando a função
    # driver, que é o nosso Selenium turbinado

    # se encontrar o arquivo localmente
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)
    # se nao encontrou localmente
    else:
        # usando o Crhome Driver do Servidor / Servico
        driver_ = webdriver.Chrome()

    loginPage = LoginPage(driver_)

    # funcao finalizacao do teste esta contida na funcao de inicializacao (login)
    def quit():
        driver_.quit()

    # chamar o quit ( a finalizacao)
    request.addfinalizer(quit)
    return loginPage


def testar_login_com_sucesso(login):
    # Faça o login com este usuário e senha
    login.com_('tomsmith', 'SuperSecretPassword!')
    # Validar o resultado = mensagem de sucesso presenta
    assert login.success_message_present()


def testar_login_com_usuario_invalido(login):
    login.com_('juca', 'SuperSecretPassword!')
    assert login.failure_message_present_by_username()


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto1234')
    assert login.failure_message_present_by_username()
