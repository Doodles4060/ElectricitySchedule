from selenium import webdriver

from time import time, sleep


def wait_for_element(element):
    start = time()
    while True:
        # I'm pretty sure that is the if statement could be flipped
        if element.get_attribute('disabled') == 'true':
            continue
        else:
            print('The element is here!')
            break
    print(f'Data is loaded: {time() - start:.3f}ms')


class ElectricitySchedule:
    def __init__(self, city: str, street: str, house_num: str, url='https://www.dtek-dnem.com.ua/ua/shutdowns') -> None:
        self.url = url
        self.city = city
        self.street = street
        self.house = house_num

    def get_page(self, wb, url=None) -> None:
        if url is None:
            url = self.url

        wb.get(url)
        sleep(10)

    def set_up_page(self, wb) -> None:
        city_elem = wb.find_element('name', 'city')
        street_elem = wb.find_element('name', 'street')
        house_num_elem = wb.find_element('name', 'house_num')

        city_elem.send_keys(self.city)

        dropdown_city = wb.find_element('xpath', '//*[@id="cityautocomplete-list"]/div')
        dropdown_city.click()

        wait_for_element(street_elem)
        street_elem.send_keys(self.street)

        dropdown_street = wb.find_element('xpath', '//*[@id="streetautocomplete-list"]/div')
        dropdown_street.click()

        wait_for_element(house_num_elem)
        house_num_elem.send_keys(self.house)

        dropdown_house_num = wb.find_element('xpath', '//*[@id="house_numautocomplete-list"]/div')
        dropdown_house_num.click()


def main() -> None:
    driver = webdriver.Chrome()

    city = input('Enter city: ')
    street = input('Enter street: ')
    house_num = input('Enter house number: ')
    schedule = ElectricitySchedule(city, street, house_num)
    schedule.get_page(driver)

    schedule.set_up_page(driver)

    driver.execute_script("window.scrollTo(0, 150)")
    driver.get_screenshot_as_png()
    driver.save_screenshot('ElectricitySchedule.png')

    driver.quit()


if __name__ == '__main__':
    main()
