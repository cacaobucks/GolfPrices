import requests
import os
from bs4 import BeautifulSoup

BASE_URL = "https://golf-jalan.net"

urls = [
"https://golf-jalan.net/search/?prefectureIds=8&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##栃木県
,"https://golf-jalan.net/search/?prefectureIds=12&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##千葉県
,"https://golf-jalan.net/search/?prefectureIds=11&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##埼玉県
,"https://golf-jalan.net/search/?prefectureIds=9&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##群馬県
,"https://golf-jalan.net/search/?prefectureIds=14&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##神奈川県
,"https://golf-jalan.net/search/?prefectureIds=13&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=18&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##東京都
,"https://golf-jalan.net/search/?prefectureIds=10&startingPointDisplay=&startingPointLat=0.0&startingPointLng=0.0&arrivalTime=120&playSchedule=2023%2F09%2F01&playMonth=8&playDate=01&searchYmdTypeAroundDays=16_0&priceFrom=&priceTo=&searchSequency=&highwayId=&searchIcDistance=&searchSortType=1&searchPlanType=1&areaSearchFlg=0&nextMonth=7&nextDate=19&createSearchConditionFlg=1&isSearchHistoryRegistFlg=true&searchTimes="
##茨城県
]
# HTMLファイルを保存するベースディレクトリ
base_directory = './html_files_golf'

#メインの処理関数。指定されたURLからHTMLを取得して、指定のディレクトリに保存する。
def main():
    
    # 各URLをクロールして、HTMLを保存
    for idx, url in enumerate(urls, 1):
        crawl_and_save_url(url, idx)

    print("Crawling completed!")

#指定されたURLをクロールして、得られたHTMLをファイルに保存する関数。
def crawl_and_save_url(url, index):
    """
    Args:
    - url (str): クロールするURL
    - index (int): URLのインデックス番号。保存するディレクトリやファイルの名前に使用される。
    
    Returns:
    - None
    """
    page_num = 1
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
            return
        
        # このURLのサブディレクトリを作成する
        sub_directory = os.path.join(base_directory, f'golf_page_{index}')
        if not os.path.exists(sub_directory):
            os.makedirs(sub_directory)
        
        # 取得したHTMLコンテンツをサブディレクトリ内のファイルに保存する
        file_name = os.path.join(sub_directory, f'page_{page_num}.html')
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f"Saved HTML content to {file_name}")

        soup = BeautifulSoup(response.text, 'html.parser')
        next_link = soup.find("a", string="次へ")
        if next_link and next_link.get('href'):
            url = BASE_URL + next_link.get('href')
            page_num += 1
        else:
            url = None

if __name__ == "__main__":
    main()