from .instfnotfyou import InstaFnotFYou
import flet as ft


class InstFnotFYouApp(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_picker = ft.FilePicker(on_result=self._get_file_name_from_dialog)
        self.add_file_button = ft.IconButton(icon=ft.icons.ABC, on_click=self.get_file_name)
        self.file_path = None

        # self.controls = [self.add_file_button]
    
    def get_file_name(self, e):
        self.page.overlay.append(self.file_picker)
        self.page.update()
        self.file_picker.pick_files()
    
    def _get_file_name_from_dialog(self, e: ft.FilePickerResultEvent):
        self.file_path = e.files[0].path  # We will work on only one file
    
    def build(self):
        return ft.Column([self.add_file_button],
                         alignment=ft.MainAxisAlignment.CENTER,
                         horizontal_alignment=ft.CrossAxisAlignment.CENTER)
