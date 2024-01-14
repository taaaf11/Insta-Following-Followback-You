import flet as ft


# Created just for developer convenience.
# Can't put size=smth everywhere in source.
class SimpleText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = 15


# solely for the alignment purposes
class LinkButton(ft.Container):
    def __init__(
        self,
        link_text: str | None = None,
        link_addr: str | None = None,
        icon: str | None = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        button = ft.TextButton(
            icon=icon,
            text=link_text,
            on_click=lambda _: self.page.launch_url(link_addr),
        )
        self.content = button


class HelpPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        INSTAGRAM_DOWNLOAD_INFO_HELP_PAGE = "https://help.instagram.com/181231772500920"
        GITHUB_REPO_LINK = "https://github.com/taaaf11/Insta-Following-Followback-You"
        self.controls = [
            SimpleText("1. View steps of downloading data for your profile:"),
            LinkButton(
                icon=ft.icons.INSERT_LINK_ROUNDED,
                link_text="Instagram - Help Page - Request Data Download",
                link_addr=INSTAGRAM_DOWNLOAD_INFO_HELP_PAGE,
                alignment=ft.alignment.center,
            ),
            SimpleText(
                "2. Don't fret, it is the link to official instagram page where you can download your data."
            ),
            SimpleText(
                "3. Navigate through the process, select **Followers and Following** (as this is required by the app)."
            ),
            SimpleText("4. Download the information."),
            SimpleText("5. Give that archive (.zip) file to the app."),
            SimpleText(
                "6. Hurray! Now you can see those people who don't follow you back on Instagram."
                "\n"
            ),
            SimpleText(
                "P.S.: Don't worry about your data! We just work on the followers and followings list from the zip file you provide. If you are worried, you can have a look at the source code..."
            ),
            LinkButton(
                icon=ft.icons.INSERT_LINK_OUTLINED,
                link_text="Source code",
                link_addr=GITHUB_REPO_LINK,
                alignment=ft.alignment.center,
            ),
        ]

    def inc_size(self):
        for control in self.controls:
            if isinstance(control, SimpleText):
                control.size += 1
        self.update()

    def dec_size(self):
        for control in self.controls:
            if isinstance(control, SimpleText):
                control.size -= 1
        self.update()
