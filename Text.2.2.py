mport PySimpleGUI as sg
sg.theme("DarkGreen4") #penentuan tema
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.text("TEKNOLOGI" INFORMASI",size=(25,1),justification="center"")],
                            [[sg.text("TEKNOLOGI" INFORMASI",size=(25,1),justification="left"")],
                            [[sg.text("TEKNOLOGI" INFORMASI",size=(25,1),justification="right"")],
                             [[sg.text("TEKNOLOGI" INFORMASI"+" ")* 2, size=(25,2),justification="center"")],
                              [[sg.text("uniska mab banjarmasin",text_color="#AFFCC00")]],
                              size=(400,250),
                              font=("times",18)
window()
window.close()