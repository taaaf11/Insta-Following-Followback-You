from backend.fn import get_info_flet_controls
import flet as ft


class InstFnotFYouApp(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_picker = ft.FilePicker(on_result=self._get_file_name_from_dialog)
        self.add_file_button = ft.IconButton(icon=ft.icons.FILE_OPEN, on_click=self.get_file_name)
        self.submit_button = ft.IconButton(icon=ft.icons.CHECK_SHARP, on_click=self.show_usernames)
        self.file_path = None

        self.controls = [ft.Row([self.add_file_button, self.submit_button], alignment=ft.MainAxisAlignment.CENTER)]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def get_file_name(self, e):
        self.page.overlay.append(self.file_picker)
        self.page.update()
        self.file_picker.pick_files()
    
    def _get_file_name_from_dialog(self, e: ft.FilePickerResultEvent):
        self.file_path = e.files[0].path  # We will work on only one file
    
    # @staticmethod
    # def _get_max_len_in_items(flet_text_controls_list: list[ft.Text]) -> int:
    #     max_ = len(flet_text_controls_list[0].value)
    #     for text_control in flet_text_controls_list:
    #         value_length = len(text_control.value)
    #         if value_length > max_:
    #             max_ = value_length
    #     return max_
    
    def show_usernames(self, e):
        controls = get_info_flet_controls(self.file_path)
        self.controls.append(
            ft.DataTable(
                columns=[ft.DataColumn(ft.Text('People not Following you back'))],
                rows=[ft.DataRow([ft.DataCell(i)]) for i in controls],
                # border=ft.border.all()
            )
        )
        print(self.controls)
        self.update()
