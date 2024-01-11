import flet as ft


# Created just for developer convenience.
# Can't put size=smth everywhere in source.
class SimpleText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = 25

class HelpPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            ft.Row([SimpleText('1. Click on this link:'), ft.TextButton('https://accountscenter.instagram.com/info_and_permissions/dyi')]),
            SimpleText('2. Don\'t fret, it is the link to official instagram page where you can download your data.'),
            SimpleText('3. Navigate through the process, select **Followers and Following** (as this is required by the app).'),
            SimpleText('4. Download the information.'),
            SimpleText('5. Give that archive (.zip) file to the app.'),
            SimpleText('6. Hurray! Now you can see those people who don\'t follow you back on Instagram.'
                       '\n'),

            SimpleText('P.S.: If you are worried about your data, you can view the source of this app...'),
            ft.TextButton(icon=ft.icons.INSERT_LINK_OUTLINED, text='Source code on GitHub')
        ]
    
    def inc_size(self):
        for text in self.controls:
            text.size += 1
        self.update()
    
    def dec_size(self):
        for text in self.controls:
            text.size -= 1
        self.update()
