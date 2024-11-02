import PySimpleGUI as sg
sg.theme("DarkGreen3")
sg.theme_text_color("#E0EEEE")
window = sg.Window(title="Latihan Pertama", layout=[
    [sg.Text("SELAMAT DATANG GAN", font=("Arial",15,"italic","bold","underline"))],
    [sg.Text("NPM          : 2210010630")],
    [sg.Text("Nama         : Muhammad Aditya Oscar")],
    [sg.Text("Kelas        : 5A Nonreg Banjarmasin")],
    [sg.Text("Matkul       : Pemrograman Visual 3")]
    ],
    size=(400,200),
    font=("Times", 11))
window()
window.close()