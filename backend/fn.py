from bs4 import BeautifulSoup as Bs
from collections import namedtuple
import flet as ft
import threading
import zipfile


# for both followers and followings
FollowData = namedtuple("FollowData", "name date")

# *** all the function names starting with "opt" will be used in multi-threading ***


def get_data_from_zip(filename: str) -> tuple[list]:
    with zipfile.ZipFile(filename) as data:
        with data.open(
            "connections/followers_and_following/followers_1.html"
        ) as followers_file:
            followers_data = followers_file.read()
        with data.open(
            "connections/followers_and_following/following.html"
        ) as following_file:
            following_data = following_file.read()

    followers = parse_html_data(followers_data)
    followings = parse_html_data(following_data)

    return followers, followings


def do_mul_thread(datas: list, function, *args):  # todo: add multi-threading tasks here
    three_datas = [
        datas[: len(datas) // 4],
        datas[len(datas) // 4 : 2 * len(datas) // 4],
        datas[2 * len(datas) // 4 : 3 * len(datas) // 4],
        datas[3 * len(datas) // 4 :],
    ]

    result_1 = [None]
    result_2 = [None]
    result_3 = [None]
    result_4 = [None]

    parse_t1 = threading.Thread(target=function, args=(three_datas[0], result_1, *args))
    parse_t2 = threading.Thread(target=function, args=(three_datas[1], result_2, *args))
    parse_t3 = threading.Thread(target=function, args=(three_datas[2], result_3, *args))
    parse_t4 = threading.Thread(target=function, args=(three_datas[3], result_4, *args))

    parse_t1.start()
    parse_t1.join()
    parse_t2.start()
    parse_t2.join()
    parse_t3.start()
    parse_t3.join()
    parse_t4.start()
    parse_t4.join()

    return result_1[0] + result_2[0] + result_3[0] + result_4[0]


def parse_html_data(html_string: str):
    soup = Bs(html_string, "html.parser")
    data_divs = soup.find_all("div", attrs={"class": "_a6-p"})

    return do_mul_thread(data_divs, opt_get_data_html)


def opt_get_data_html(datas_list: list, ret_val: list) -> list:
    data = []
    for data_div in datas_list:
        name_and_date = data_div.div.find_all("div")
        name = name_and_date[0].a.text
        time = name_and_date[1].text
        data.append(FollowData(name, time))
    ret_val[0] = data


def opt_get_names(followers_list: list, ret_val: list):
    ret_val[0] = [follower.name for follower in followers_list]


def opt_get_data(followings_list: list, ret_val: list, followers_list: list):
    ret_val[0] = [
        following
        for following in followings_list
        if following.name not in followers_list
    ]


def opt_controls(list_controls: list, ret_val: list):
    not_following_you_controls = []
    for not_following_you in list_controls:
        not_following_you_controls.append(
            (ft.Text(not_following_you.name), ft.Text(not_following_you.date))
        )
    ret_val[0] = not_following_you_controls


def get_info(filename: str) -> list[namedtuple]:
    followers, followings = get_data_from_zip(filename=filename)

    followers_list = do_mul_thread(followers, opt_get_names)

    return do_mul_thread(followings, opt_get_data, followers_list)


def get_info_flet_text_controls(list_controls: list) -> list[ft.Text]:
    return do_mul_thread(list_controls, opt_controls)
