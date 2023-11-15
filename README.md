![golf header](https://github.com/cacaobucks/Golfprices/assets/110584408/42ded78d-e012-4e2b-abe6-ca11598c40d6)


# Golfprices
The objective of this deliverable is to collect information on golf courses in the Kanto region from the Jalan Golf website using scraping and analyze their price ranges. This process is divided into three major steps.
(Note: Playing golf here refers to "going to a golf course and playing a round of golf".

## 1. Crawling 
In this script, the requests library was used to access the Jalan Golf web page and retrieve HTML pages about golf courses in the Kanto region. The regions retrieved were links to pages containing price information for golf courses in the Kanto region (Tochigi, Chiba, Saitama, Gunma, Kanagawa, Tokyo, and Ibaraki).

## 2. Scraping 
Based on the HTML pages obtained, BeautifulSoup was used to extract the necessary data. The data to be scraped includes information on location (prefecture name) and price on golf. This data was saved in CSV format for later analysis.

## 3. Data Analysis 
Analysis was performed in Jupyter notebook, using libraries such as Pandas, Matplotlib, Seaborn, etc. The data saved in CSV files were loaded to perform a statistical analysis on the price range of golf courses in the Kanto region.
The analysis revealed that "for people looking for golf courses in Tokyo, there is a great possibility that they will be able to book golf courses on their desired dates at a lower total cost if they look for golf courses in the surrounding prefectures rather than in Tokyo, even after taking transportation costs to the golf course into account. For example, when looking at the price range of 8,000 to 10,000 yen, while there are 32 available reservations for golf courses in Tokyo, more than 300 reservations are available in Tochigi, Ibaraki, and Gunma prefectures.

The purpose of this project is to provide useful information to new golfers living in Tokyo who are looking for golf courses in Tokyo alone, so that they can understand the price range of golf courses in the Kanto region. This analysis proved that the aforementioned people can play golf on their preferred schedule and at a lower cost by "traveling to other prefectures to play golf rather than playing golf in Tokyo.
