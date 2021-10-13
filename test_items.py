import time


def test_is_button_fr_es(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    print(f'=========================={button}')

    assert button, 'NO BUTTON!'
