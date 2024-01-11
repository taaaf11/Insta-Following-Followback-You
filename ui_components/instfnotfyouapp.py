from backend.fn import get_info_flet_controls
import flet as ft


class InstFnotFYouApp(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_picker = ft.FilePicker(on_result=self._get_file_name_from_dialog)
        self.add_file_button = ft.TextButton(icon=ft.icons.FILE_OPEN, on_click=self.get_file_name)
        self.submit_button = ft.TextButton(icon=ft.icons.CHECK_SHARP, on_click=self.show_usernames)

        self.file_path = None
        self.file_path_field = ft.TextField(hint_text='File Path', disabled=True)
        
        self.controls = [ft.Row([self.file_path_field, self.add_file_button], alignment=ft.MainAxisAlignment.CENTER), self.submit_button]
        
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def get_file_name(self, e):
        self.page.overlay.append(self.file_picker)
        self.page.update()
        self.file_picker.pick_files()
    
    def _get_file_name_from_dialog(self, e: ft.FilePickerResultEvent):
        self.file_path = e.files[0].path  # We will work on only one file
        self.file_path_field.value = self.file_path
        self.update()
    
    def show_usernames(self, e):
        controls = get_info_flet_controls(self.file_path)
        self.controls.append(
            ft.Container(
                ft.ListView([
                    ft.DataTable(
                        columns=[ft.DataColumn(ft.Text('People not Following you back'))],
                        rows=[ft.DataRow([ft.DataCell(i)]) for i in controls])
                    ],
                height=300, width=400),
            border=ft.border.all(width=1, color=self.page.theme.color_scheme_seed)
        ))
        self.update()
