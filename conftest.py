import pytest
from final_practise.driver_factory import create_driver

@pytest.fixture(scope='function')
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
