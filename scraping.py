from bs4 import BeautifulSoup
import csv
import os
import re
import time
# 必要な変数を設定
base_directory = 'html_files_golf'
options = ["tochigi", "chiba", "saitama","gunma","kanagawa","tokyo","ibaraki"]

def main():
    # 各項目ごとのディレクトリから情報を取得してCSVに保存
    for idx, option_word in enumerate(options, 1):
        dir_path = os.path.join(base_directory, f'golf_page_{idx}')
        all_data_for_option = []
        for filename in os.listdir(dir_path):
            if filename.endswith('.html'):
                full_path = os.path.join(dir_path, filename)
                all_data_for_option.extend(scrape_prices_from_file(full_path, option_word))
        save_to_csv(all_data_for_option, idx)

    print("All data have been saved.")
    time.sleep(5)

    combined_data = []

    # 各CSVファイルからデータを読み込む
    for i in range(1, 8):
        with open(f"prices_{i}.csv", "r") as file:
            reader = csv.reader(file)
            if i == 1:
                combined_data.extend(reader)
            else:
                next(reader)  # ヘッダーをスキップ
                combined_data.extend(reader)

    cleaned_data = []
    cleaned_data.append(combined_data[0])

    for row in combined_data[1:]:
        row[0] = extract_numeric(row[0])
        cleaned_data.append(row)

    cleaned_data = [row for row in cleaned_data if row[0] != 0]
    swapped_data = [(row[1], row[0]) for row in cleaned_data]

    with open("golfprices.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(swapped_data)

    print("Data has been processed and saved to golfprices.csv!")

# ファイル内のHTMLから価格情報をスクレイピングする関数
def scrape_prices_from_file(filepath, option_word):
    """
    Args:
    - filepath (str): 読み込むHTMLファイルのパス
    - option_word (str): 都道府県の情報
    
    Returns:
    - list: 価格と都道府県の情報を持つリスト
    """
    data_list = []
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # 価格情報を取得
        prices = soup.select(".price")  # 仮定のセレクタ
        for price in prices:
            data_list.append([price.get_text(strip=True), option_word])

    return data_list

# データをCSVファイルに保存する関数
def save_to_csv(data_list, index):
    """
    Args:
    - data_list (list): 保存するデータのリスト
    - index (int): ファイルのインデックス番号
    
    Returns:
    - None
    """
    filename = f"prices_{index}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        # ヘッダーを書き込む
        writer.writerow(["Price", "Prefecture"])
        for row_data in data_list:
            writer.writerow(row_data)
    print(f"Saved data to {filename}")

# 文字列から数値を抽出する関数
def extract_numeric(value):
    """
    Args:
    - value (str): 数値を含む文字列
    
    Returns:
    - int: 抽出された数値
    """
    cleaned_value = re.sub(r'[^0-9]', '', value)
    if not cleaned_value:
        return 0
    return int(cleaned_value)

# このスクリプトが直接実行された場合のみ、main() 関数を実行する。
# スクリプトが他のスクリプトやモジュールとしてインポートされた場合、このコードは実行されない。
if __name__ == "__main__":
    main()