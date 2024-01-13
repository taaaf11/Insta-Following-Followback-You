from ui_components import InstFnotFYouApp, HelpPage, AboutPage
import flet as ft


GITHUB_PROFILE = 'https://www.github.com/taaaf11'


def main(page: ft.Page):
    page.title = "Insta Followback Checker"

    page.theme = ft.Theme(color_scheme_seed='Brown')

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def navigate_to_page(e):
        selected_page = e.control.selected_index

        # resetting the layout alignment,
        # as it changes when user requests help_view
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.scroll = None
        page.appbar.actions = []

        if selected_page == 0:
            home_view.visible = True
            help_view.visible = False
            about_view.visible = False
        elif selected_page == 1:
            home_view.visible = False
            help_view.visible = True
            about_view.visible = False

            # add buttons to increase or decrease the size of help text
            page.appbar.actions = [
                ft.IconButton(icon=ft.icons.ADD_SHARP, on_click=lambda _: help_view.inc_size()),
                ft.IconButton(icon=ft.icons.REMOVE_SHARP, on_click=lambda _: help_view.dec_size())
            ]

            page.scroll = 'auto'
        elif selected_page == 2:
            home_view.visible = False
            help_view.visible = False
            about_view.visible = True

            # centering the layout to keep the info in center
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
        
        page.update()
    
    page.appbar = ft.AppBar(title=ft.Text(page.title))

    page.drawer = ft.NavigationDrawer(controls=[
        ft.NavigationDrawerDestination(
            icon=ft.icons.HOME_OUTLINED,
            label='Home',
            selected_icon=ft.icons.HOME_SHARP
        ),
        ft.NavigationDrawerDestination(
            icon=ft.icons.HELP_OUTLINE_SHARP,
            label='Help',
            selected_icon=ft.icons.HELP_SHARP
        ),
        ft.Divider(thickness=2),
        ft.NavigationDrawerDestination(
            icon=ft.icons.INFO_OUTLINE,
            label='About',
            selected_icon=ft.icons.INFO_SHARP
        )
    ], selected_index=0, on_change=navigate_to_page)

    home_view = InstFnotFYouApp()
    help_view = HelpPage(visible=False)
    about_view = AboutPage(author_name='Muhammad Altaaf', author_avatar_url=f'{GITHUB_PROFILE}.png?size=120px',
                           source_code_link=f'{GITHUB_PROFILE}/Insta-Following-Followback-You',
                           visible=False)
    page.add(home_view, help_view, about_view)

ft.app(main)
