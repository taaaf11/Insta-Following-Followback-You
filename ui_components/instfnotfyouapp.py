from backend.fn import get_info_flet_text_controls
import flet as ft


class InstFnotFYouApp(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_picker = ft.FilePicker(on_result=self._get_file_name_from_dialog)

        self.add_file_button = ft.TextButton(icon=ft.icons.FILE_OPEN, text='Add zip file', on_click=self.get_file_name)
        self.submit_button = ft.IconButton(icon=ft.icons.CHECK_SHARP, on_click=self.show_usernames)

        self.file_path = None
        self.file_added_confirm = ft.Text(visible=False)

        self.controls = [
            self.add_file_button,
            self.file_added_confirm,
            self.submit_button
        ]
        
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def get_file_name(self, e):
        self.page.overlay.append(self.file_picker)
        self.page.update()
        self.file_picker.pick_files()
    
    def _get_file_name_from_dialog(self, e: ft.FilePickerResultEvent):
        self.file_path = e.files[0].path  # We will be working on only one file

        self.file_added_confirm.value = 'File added!'
        self.file_added_confirm.visible = True
        
        self.update()
    
    def show_usernames(self, e):
        controls = get_info_flet_text_controls(self.file_path)
        list_view = ft.ListView([
            ft.DataTable(
                columns=[ft.DataColumn(ft.Text('People not Following you back'))],
                rows=[ft.DataRow([ft.DataCell(control)]) for control in controls
            ])
        ], height=self.page.height - 50, width=400)

        if isinstance(self.controls[-1], ft.ListView):
            self.controls[-1] = list_view
        else:
            self.controls.append(list_view)

        self.update()
