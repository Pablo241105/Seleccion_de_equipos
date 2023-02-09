import flet as ft

def main(page: ft.Page):
    page.title="Seleccion de equipos"
    #vEquipos=["Aston Villa","Man-United","Juventus","Real Madrid","Al_Nassr"]
    vEquiposSeleccionados=[]

    def seleccionar(e):
        sel=ddEquipo.value
        if vEquiposSeleccionados.count(sel)== 0:
            vEquiposSeleccionados.append(sel)
            print(vEquiposSeleccionados)

            fila = ft.Row(controls=[ft.Text(sel),ft.Image(src=imagenEquipo.src,width=50,height=50)])
            lv.controls.append(fila)      
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
           
        elif (ddEquipo.value == "Al_Nassr"):
            imagenEquipo.src = "imagenes/Al_Nassr.png"

        else: 
            imagenEquipo.src = "imagenes/Sin_foto.jpg"
        
        page.update()

    def GUARDAR(a):
        f = open("seleccionados.txt","w")

        for i in vEquiposSeleccionados:
            f.write(i+"\n")

        f.close()
        

    def cargarEquipos():
        vEquipos = []
        f = open("Equipos.txt","r")

        linea = f.readline()
        vEquipos = linea.split(sep=";")

        f.close()
        
        return vEquipos


    imagenEquipo = ft.Image(src="aa")
    btn_seleccionar_equipo=ft.ElevatedButton(text="Seleccionar equipo",on_click=seleccionar)
    btn_guardar=ft.FloatingActionButton(text="Guardar",on_click=GUARDAR,width=100)
    ddEquipo = ft.Dropdown(label="Equipos",width=500,on_change=cambiar_imagen)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True) 

    vEquipos=cargarEquipos()
    print(vEquipos)
    for equipo in vEquipos:
        ddEquipo.options.append(ft.dropdown.Option(equipo))


    page.add (ddEquipo,imagenEquipo,btn_seleccionar_equipo,lv,btn_guardar)
ft.app(target=main,assets_dir="imagenes")