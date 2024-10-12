import PySimpleGUI as sg
susunan=[[sg.VPush(),
          sg.text("UNISKA MAAB",font=("helvetica",24)),
          sg.push()],
          [sg.push(),
           sg.text("BANJARMASIN", font=("courier",18)),
           sg.push()],
           [sg.VPush()]
]
window = sg.window(title="elemen ttext",
                   layout=susunan,
                   size=(430,200))

window.read()      
window.close()    
        
