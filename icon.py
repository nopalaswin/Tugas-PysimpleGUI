import PySimpleGUI as sg
susunan=[[sg.text("UNISKA MAAB",font=("helvetica",24))]],
        [[sg.text("BANJARMASIN", font=("courier",18))]]
window = sg.window(title="new icon",
                   layout=susunan,
                   element_justification = "center",
                   icon="favicon,ico"
                   size=(430,200))

window.read()
window.close()