from bs4 import BeautifulSoup as Bs
from collections import namedtuple
import flet as ft
import zipfile


# for both followers and followings
FollowData = namedtuple('FollowingData', 'name date')


def get_data_from_zip(filename: str) -> tuple[list]:
    with zipfile.ZipFile(filename) as data:
        with data.open('connections/followers_and_following/followers_1.html') as followers_file:
            followers_data = followers_file.read()
        with data.open('connections/followers_and_following/following.html') as following_file:
            following_data = following_file.read()
    
    followers = parse_html_data(followers_data)
    followings = parse_html_data(following_data)

    return followers, followings


def parse_html_data(html_string: str):
    data = []
    soup = Bs(html_string, 'html.parser')
    data_divs = soup.find_all('div', attrs={'class': '_a6-p'})

    for data_div in data_divs:
        name_and_date = data_div.div.find_all('div')
        name = name_and_date[0].a.text
        time = name_and_date[1].text
        data.append(FollowData(name, time))
    return data


def get_info(filename: str) -> list[namedtuple]:
    followers, followings = get_data_from_zip(filename=filename)

    followers_names = [follower.name for follower in followers]

    return [following for following in followings if following.name not in followers_names]


def get_info_flet_text_controls(filename: str) -> list[ft.Text]:
    not_following_you_controls = []
    for not_following_you in get_info(filename):
        not_following_you_controls.append(
            (ft.Text(not_following_you.name), ft.Text(not_following_you.date))
        )
    return not_following_you_controls
