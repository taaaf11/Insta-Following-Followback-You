import flet as ft


class SearchBar(ft.Container):
    def __init__(self, func, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_field = ft.TextField(
            hint_text="Search...",
            border_radius=self.border_radius,
            on_change=self.submit,
            on_submit=self.submit,
        )
        self.text = None
        self.content = self.text_field

        self.func = func

    def submit(self, e):
        self.text = self.text_field.value
        self.func(self.text)
