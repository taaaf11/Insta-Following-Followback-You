from bs4 import BeautifulSoup as Bs
import flet as ft
import zipfile


def get_data_from_zip(filename) -> tuple[list]:
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
    data_divs = soup.find_all('div', attrs={'class': 'pam _3-95 _2ph- _a6-g uiBoxWhite noborder'})

    for data_div in data_divs:
        data.append(data_div.find('div', attrs={'class': '_a6-p'}).div.div.a.text)
    return data


def get_info(filename) -> list:
    followers, followings = get_data_from_zip(filename=filename)
    # followers = data_followers_following[0]
    # followings = data_followers_following[1]
    
    not_following_you = []

    for following in followings:
        if following not in followers:
            not_following_you.append(following)
    
    return not_following_you


def get_info_flet_controls(filename):
    not_following_you_controls = []
    for not_following_you in get_info(filename):
        not_following_you_controls.append(ft.Text(not_following_you))
    return not_following_you_controls
