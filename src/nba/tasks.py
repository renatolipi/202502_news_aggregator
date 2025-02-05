

from bs4 import BeautifulSoup as BS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC


CLASS_NAME = 'TransactionSingle_desc__uG447'


def _get_specific_ajax_content():
    URL = 'https://www.nba.com/players/transactions'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(URL)
    answer = ''

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, CLASS_NAME))
        )
        answer = driver.page_source
    finally:
        driver.quit()

    return answer


def get_players_transactions():
    response = _get_specific_ajax_content()
    if not response:
        # TODO
        # log
        print(f'Nothing was found: {response}')
        return

    soup = BS(response, 'html.parser')
    transactions_html = soup.find_all('div', class_=CLASS_NAME)
    transactions_headlines = []

    for transaction in transactions_html:
        transactions_headlines.append(transaction.get_text(strip=True))

    # TODO
    # Save it all on database or send it somewhere else.
    print(transactions_headlines)
