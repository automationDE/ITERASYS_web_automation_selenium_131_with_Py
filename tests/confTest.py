import pytest

#from tests import *
#from tests import .config
from . import *

def pytest_addoption(parser):
    parser.addoption('--baseurl',
                    action='store',
                    default='https://the-internet.herokuapp.com/login'
                    help='endereco dos sites alvo do teste'
    )
    parser.addoption('--host',
                    action = 'store',
                    default = 'saucelabs'
                    help = 'ambiente em que vou executar os testes'
    )
    parser.addoption('--browser',
                    action = 'store',
                    default = 'chrome'
                    help = 'navegador padrao'
    )
    parser.addoption('--browserversion',
                    action = 'store',
                    default = '10.0'
                    help = 'versao do navegador'
    )
    parser.addoption('--platform',
                    action = 'store',
                    default = 'Windows 10'
                    help = 'versao do Sistema Operacional'
    )

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.browser = request.config.getoption('--browser')
    config.browserversion = request.config.getoption('--browserversion')
    config.platform = request.config.getoption('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name   # Adicionar o nome do teste baseado o script
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce_options': {
                'name': test_name,     # nome do teste conforme acima
            }
        }