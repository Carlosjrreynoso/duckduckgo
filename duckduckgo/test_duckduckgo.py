import unittest
from selenium.webdriver import Chrome


class TestDuckDuckGo(unittest.TestCase):

    def test_duckduckgo(self):
        frase = 'octopus'

        driver = Chrome() # TODO: Remover sentencia y utilizar la sentencia para Windows
        # driver = Chrome(executable_path='./chromedriver.exe')

        driver.get('https://www.duckduckgo.com/')

        search_form_input_homepage = driver.find_element_by_id('search_form_input_homepage')
        search_form_input_homepage.send_keys(frase)

        search_button_homepage = driver.find_element_by_id('search_button_homepage')
        search_button_homepage.click()

        search_form_input = driver.find_element_by_id('search_form_input')
        self.assertEqual(search_form_input.get_attribute('value'), frase)

        links_div = driver.find_elements_by_css_selector('#links > div')
        self.assertGreater(len(links_div), 0)

        xpath = f'//div[@id="links"]//*[contains(text(), "{frase}")]'
        resultados = driver.find_elements_by_xpath(xpath)
        self.assertGreater(len(resultados), 0)

if __name__ == '__main__':
    unittest.main()