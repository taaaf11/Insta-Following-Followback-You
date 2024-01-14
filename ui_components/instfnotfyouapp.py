from backend import get_info, get_info_flet_text_controls
from .searchbar import SearchBar
import flet as ft
import threading


class InstFnotFYouApp(ft.Column):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_picker = ft.FilePicker(on_result=self._get_file_name_from_dialog)

        self.add_file_button = ft.TextButton(icon=ft.icons.FILE_OPEN, text='Add zip file', on_click=self.get_file_name)
        self.submit_button = ft.IconButton(icon=ft.icons.CHECK_SHARP, on_click=self.controls_adder)

        self.file_path = None

        self.prog_bar = None
        self.file_added_confirm = ft.Text(value='File added!', visible=False)

        self.controls = [
            self.add_file_button,
            self.file_added_confirm,
            self.submit_button
        ]

        self.info_ctrls = None
        self.list_view = None
        
        self.alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def get_file_name(self, e):
        self._reset_controls()
        self.page.overlay.append(self.file_picker)
        self.page.update()
        self.file_picker.pick_files()
    
    def _get_file_name_from_dialog(self, e: ft.FilePickerResultEvent):
        self.file_path = e.files[0].path  # We will be working on only one file

        self.file_added_confirm.visible = True
        
        self.update()
    
    def show_progressring(self):
        prog_bar_count = 0
        while not isinstance(self.controls[-1], ft.ListView):
            if prog_bar_count == 1:
                continue
            self.controls.append(
                (prog_bar := ft.ProgressBar(width=self.page.width / 4))
            )
            self.prog_bar = prog_bar
            self.update()
            prog_bar_count = 1
        self.update()
    
    def _reset_controls(self):
        self.file_added_confirm.visible = False
        self.controls = [
            self.add_file_button,
            self.file_added_confirm,
            self.submit_button
        ]
        self.update()
    
    def searcher(self, text):
        self.list_view.controls[0].rows = [ft.DataRow([ft.DataCell(control[0]), ft.DataCell(control[1])]) for control in self.info_ctrls if text in control[0].value]
        self.update()
    
    def show_usernames(self):
        self.info_ctrls = get_info_flet_text_controls(get_info(self.file_path))

        search_bar = SearchBar(func=self.searcher,
                                border_radius=10,
                                width=self.page.width / 2)
        
        self.list_view = ft.ListView([
            ft.DataTable(
                columns=[ft.DataColumn(ft.Text('People')), ft.DataColumn(ft.Text('Follow Date'))],
                rows=[ft.DataRow([ft.DataCell(control[0]), ft.DataCell(control[1])])
                       for control in self.info_ctrls]
            )
        ], height=self.page.height / 2, width=self.page.width)

        self.controls.remove(self.prog_bar)
        self.controls.append(search_bar)
        self.controls.append(self.list_view)
        self.controls.append(
            ft.FilledButton(text='Reset', on_click=lambda _:self._reset_controls())
        )

        self.update()
        # scrolling a small "quantity" to make the user aware
        # about the existence of other items beyond the shown items
        # basically, showing the scroll bar
        self.list_view.scroll_to(delta=0.0000001)  # making it so small that it's negligible (fizics 🤡)
        self.update()
    
    def controls_adder(self, e):
        t1 = threading.Thread(target=self.show_progressring)
        t2 = threading.Thread(target=self.show_usernames)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
