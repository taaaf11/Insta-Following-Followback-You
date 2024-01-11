import flet as ft


# Created just for developer convenience.
# Can't put size=smth everywhere in source.
class SimpleText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = 15

class HelpPage(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls = [
            ft.Row([SimpleText('1. View steps of downloading data for your profile:'), ft.TextButton('https://help.instagram.com/181231772500920')]),
            SimpleText('2. Don\'t fret, it is the link to official instagram page where you can download your data.'),
            SimpleText('3. Navigate through the process, select **Followers and Following** (as this is required by the app).'),
            SimpleText('4. Download the information.'),
            SimpleText('5. Give that archive (.zip) file to the app.'),
            SimpleText('6. Hurray! Now you can see those people who don\'t follow you back on Instagram.'
                       '\n'),

            SimpleText('P.S.: Don\'t worry about your data! We just work on the followers and followings list from the zip file you provide. If you are worried, you can have a look at the source code...'),
            ft.TextButton(icon=ft.icons.INSERT_LINK_OUTLINED, text='Source code on GitHub')
        ]
    
    def inc_size(self):
        self.controls[0].controls[0].size += 1
        for text in self.controls[1:-1]:
            text.size += 1
        self.update()
    
    def dec_size(self):
        self.controls[0].controls[0].size -= 1
        for text in self.controls[1:-1]:
            text.size -= 1
        self.update()
