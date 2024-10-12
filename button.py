import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="contoh button",
                   layout=[[sg.Text("contoh button")]],
                          [sg.Button("button simpapan")]
                          [sg.Button("button keluar")]
                          ],
                    size=(400,200),
                    font=("time", 18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close