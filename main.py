from ui_components import InstFnotFYouApp
import flet as ft


def main(page: ft.Page):
    page.title = "Insta Followback Checker"

    page.theme = ft.Theme(color_scheme_seed='Brown')

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(InstFnotFYouApp())

ft.app(main)
