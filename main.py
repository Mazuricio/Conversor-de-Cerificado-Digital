import flet
from flet import FilePicker, Text, Row, ElevatedButton, icons, FilePickerResultEvent, TextField
from converter import converter

def main(page: flet.Page):
    page.window_width = 400
    page.window_height = 500
    titulo = flet.Text(value="Conversor de pfx para PEM")
    page.controls.append(titulo)
    page.update()
    status = Text()
    arquivo = None
    def caminho(e: FilePickerResultEvent):
        if not e.files:
            return
        selecionado = e.files[0].path
        selected_files.value = selecionado
        selected_files.update()   
    pick_files_dialog = FilePicker(on_result=caminho)
    selected_files = Text()
    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()
    def bt_convert(e):
        if '.pfx' in selected_files.value:
            tipo_correto = True
        elif '.p12' in selected_files.value:
            tipo_correto = True
        else:
            tipo_correto = False
        if not in_senha.value:
            status.value = "Digite a senha!"
            status.update()
        elif selected_files.value == None:
            status.value = "Escolha um certificado!"
            status.update()
        elif not tipo_correto:
            status.value = "Selecione um arquivo .PFX ou .P12 !!"
            status.update()
        else:
            converter(selected_files.value, in_senha.value, status)
        

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()
    in_senha = TextField(label="Senha")
    bt_converter = ElevatedButton("Converter", on_click=bt_convert)
    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])
    page.add(
        Row([
            Text(value="Arquivo: "),
              ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ))
        ]),
        Row([
        selected_files
        ]),
        Row([
        in_senha]),
        Row([
        bt_converter
        ]),
        Row([
        status
        ])
    )


flet.app(target=main)

#arq = 'novo.pfx'
#senha = '1234'
#converter(arq, senha)