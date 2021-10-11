import time



def test_is_button_french(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("#login_link")
    # butt_len = len(browser.find_element_by_css_selector("button[value='Ajouter au panier']").text)
    # butt_len = len(browser.find_elements_by_css_selector("button[value='Ajouter au panier']"))# list
    # butt_len = len(browser.find_element_by_xpath(('//button[contains(@value,"Ajouter au panier")]')).text)
    butt_len = len(browser.find_elements_by_xpath(('//button[contains(@value,"Ajouter au panier")]')))
    print(f'=========================={butt_len}')

    assert butt_len > 0, 'NO BUTTON!'
