from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pprint import pprint

driver = webdriver.Chrome('/home/sasha/Рабочий стол/_Dav_/chromedriver')
houses_info_list = []
pages_list = [
	'https://ru.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A483&room_types%5B%5D=Entire%20home%2Fapt&property_type_id%5B%5D=57&property_type_id%5B%5D=4&property_type_id%5B%5D=32&property_type_id%5B%5D=58&property_type_id%5B%5D=18&property_type_id%5B%5D=22&property_type_id%5B%5D=17&property_type_id%5B%5D=23&property_type_id%5B%5D=63&property_type_id%5B%5D=24&property_type_id%5B%5D=12&property_type_id%5B%5D=19&property_type_id%5B%5D=44&property_type_id%5B%5D=66&property_type_id%5B%5D=34&property_type_id%5B%5D=16&property_type_id%5B%5D=6&property_type_id%5B%5D=69&property_type_id%5B%5D=15&title_type=CURATED_PROPERTY_TYPE',
	'https://ru.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A483&room_types%5B%5D=Entire%20home%3Fapt&property_type_id%5B%5D=4&property_type_id%5B%5D=6&property_type_id%5B%5D=12&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=22&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=32&property_type_id%5B%5D=34&property_type_id%5B%5D=44&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=63&property_type_id%5B%5D=66&property_type_id%5B%5D=69&title_type=CURATED_PROPERTY_TYPE&tab_id=home_tab&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&search_type=pagination&federated_search_session_id=467dbe33-b41f-4cb3-a87b-3b2749896c65&items_offset=20&section_offset=1',
	'https://ru.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A483&property_type_id%5B%5D=4&property_type_id%5B%5D=6&property_type_id%5B%5D=12&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=22&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=32&property_type_id%5B%5D=34&property_type_id%5B%5D=44&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=63&property_type_id%5B%5D=66&property_type_id%5B%5D=69&title_type=CURATED_PROPERTY_TYPE&tab_id=home_tab&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&search_type=pagination&federated_search_session_id=467dbe33-b41f-4cb3-a87b-3b2749896c65&items_offset=40&section_offset=1',
	'https://ru.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A483&property_type_id%5B%5D=4&property_type_id%5B%5D=6&property_type_id%5B%5D=12&property_type_id%5B%5D=15&property_type_id%5B%5D=16&property_type_id%5B%5D=17&property_type_id%5B%5D=18&property_type_id%5B%5D=19&property_type_id%5B%5D=22&property_type_id%5B%5D=23&property_type_id%5B%5D=24&property_type_id%5B%5D=32&property_type_id%5B%5D=34&property_type_id%5B%5D=44&property_type_id%5B%5D=57&property_type_id%5B%5D=58&property_type_id%5B%5D=63&property_type_id%5B%5D=66&property_type_id%5B%5D=69&title_type=CURATED_PROPERTY_TYPE&tab_id=home_tab&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&search_type=pagination&federated_search_session_id=467dbe33-b41f-4cb3-a87b-3b2749896c65&items_offset=60&section_offset=1'
]
def find_house_info(page,info_list):
	driver.get(page)
	time.sleep(15)
	response = driver.page_source
	soup = BeautifulSoup(response, 'lxml')
	houses = soup.findAll('div', {'class': '_gig1e7'})

	for hous in houses:
		try:
			house_info_dict = {}
			house_info_dict["salary"] = hous.find('span', {'class': '_olc9rf0'}).text
			house_info_dict["name"] = hous.find('span', {'class': '_bzh5lkq'}).text
			house_info_dict["reiting"] = f"{hous.find('span', {'class': '_18khxk1'})}"[18:46]
			info_list.append(house_info_dict)
		except:
			pass
	return info_list

for pag in pages_list:
	houses_info_list.extend(find_house_info(pag, houses_info_list))

pprint(houses_info_list)

time.sleep(5)
driver.quit()