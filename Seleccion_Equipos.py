import flet as ft

def main(page: ft.Page):
    page.title="Seleccion de equipos"
    #vEquipos=["Aston Villa","Man-United","Juventus","Real Madrid","Al_Nassr"]
    vEquiposSeleccionados=[]

    def GUARDAR(e):
        sel=ddEquipo.value
        if vEquiposSeleccionados.count(sel)== 0:
            vEquiposSeleccionados.append(sel)
            print(vEquiposSeleccionados)
            lv.controls.append(ft.Text(sel))      
            page.update()       
        else:
            dlg = ft.AlertDialog(title=ft.Text("EQUIPO REPETIDO!!!"))
            page.dialog = dlg
            dlg.open = True
            page.update()

    def cambiar_imagen(e):
        if (ddEquipo.value == "Aston Villa"):
            imagenEquipo.src = "Aston-Villa.png"

        elif (ddEquipo.value == "Man-United"):
            imagenEquipo.src = "imagenes/Man-United.png"
            
        elif (ddEquipo.value == "Juventus"):
            imagenEquipo.src = "imagenes/Juventus.png"
            
        elif (ddEquipo.value == "Real Madrid"):
            imagenEquipo.src = "imagenes/Real Madrid.png"
           
        elif (ddEquipo.value == "Al_Nassar"):
            imagenEquipo.src = "imagenes/Al_Nassr.png"

        else: 
            imagenEquipo.src = "imagenes/Sin_foto.jpg"
        
        page.update()
    
    def cargarEquipos():
        vEquipos = []
        f = open("Cargar_Equipos.txt","r")

        linea = f.readline()
        vEquipos = linea.split(sep=";")

        f.close()
        return vEquipos



    imagenEquipo = ft.Image(src="aa")
    btn_seleccionar_equipo=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=GUARDAR)
    page.add(btn_seleccionar_equipo,lv)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    ddEquipo = ft.Dropdown(label="Equipos",width=500,on_change=cambiar_imagen)

    vEquipos=cargarEquipos()
    print(vEquipos)
    for equipo in vEquipos:
        ddEquipo.options.append(ft.dropdown.Option(equipo))


    page.add (ddEquipo,imagenEquipo,btn_seleccionar_equipo,lv)
ft.app(target=main,assets_dir="imagenes")