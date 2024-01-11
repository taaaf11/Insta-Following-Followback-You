from ui_components import InstFnotFYouApp
import flet as ft


def main(page: ft.Page):
    page.title = "Insta people not following you back"

    page.theme = ft.Theme(color_scheme_seed='#01666f')

    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(InstFnotFYouApp())

ft.app(main)

