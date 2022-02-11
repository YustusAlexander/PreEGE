#https://www.youtube.com/watch?v=ak8Nl1Stba4&list=PLqGS6O1-DZLprgEaEeKn9BWKZBvzVi_la&index=7
import os
import re

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}




def get_data():

    global headers
    for page in tqdm(range(1, 2)):
        url = f"http://xn--24-6kct3an.xn--p1ai/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%BD%D0%B8%D0%BA_%D0%BF%D0%BE_%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B5_10-11_%D0%BA%D0%BB%D0%B0%D1%81%D1%81_%D0%A0%D1%8B%D0%BC%D0%BA%D0%B5%D0%B2%D0%B8%D1%87/{page}.html"
        if os.path.exists(f"pages/{page}.html") == False:
            req = requests.get(url + str(page), headers=headers)
            src = req.text
            with open(f"pages/{page}.html", "w", encoding="UTF-8") as file:
                 file.write(src)
        else:
            print(f"файл {page}.html уже существует!")

def scrap_tasks():
    global headers
    exercises_dict = {}
    exercise_id = 100

    # search info
    all_task = []
    for page in tqdm(range(1, 54)):
        url = f"http://xn--24-6kct3an.xn--p1ai/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%BD%D0%B8%D0%BA_%D0%BF%D0%BE_%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B5_10-11_%D0%BA%D0%BB%D0%B0%D1%81%D1%81_%D0%A0%D1%8B%D0%BC%D0%BA%D0%B5%D0%B2%D0%B8%D1%87/{page}.html"
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        all_row = soup.find_all("p")
        # print(all_row)

        for item in all_row:
            task_str = item.text
            rep = ["\n", "\xa0", "Продолжение >>>", "Главная >> Задачник по физике 10-11 класс. Рымкевич", "Окончание >>>", "Ответы >>>"]
            for sym in rep:
                if sym in task_str:
                    task_str = task_str.replace(sym, "")

            if task_str.strip():
                all_task.append(task_str)
    # print(all_task)


    with open("output/all_text.txt", "w", encoding="UTF-8") as file:
        for line in all_task:
            file.writelines(f'{line}\n')


def covert_to_dict():
    with open("output/all_text.txt", encoding="UTF-8") as file:
        all_task = file.readlines()
    print(all_task)
    all_task_dict = {}

    # ПОИСК по началу заданий 1. 2. 3. после нахождения инкремент счётчика и всё что между найденным - в значение словаря


def main():
    # get_data()
    #scrap_tasks()
    covert_to_dict()


if __name__ == '__main__':
    main()