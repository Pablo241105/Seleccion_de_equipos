import flet as ft

def main(page: ft.Page):
    page.title="SELECCION De Equipo"

    def cambiar_imagen(e):
        if (ddEquipo.value == "Aston Villa"):
            imagenEquipo.src = "Aston-Villa.png"
        elif (ddEquipo.value == "Man United"):
            imagenEquipo.src = "imagenes/Man-United.png"
            
        elif (ddEquipo.value == "Juventus"):
            imagenEquipo.src = "imagenes/Juventus.png"
            
        elif (ddEquipo.value == "Real Madrid"):
            imagenEquipo.src = "imagenes/Real Madrid.png"
           
        else:
            imagenEquipo.src = "Al_Nassr.png"
          
        page.update()
    
    
    ddEquipo = ft.Dropdown(label="Equipos",width=500,
        options=[
            ft.dropdown.Option("Aston Villa"),
            ft.dropdown.Option("Man United"),
            ft.dropdown.Option("Real Madrid"),
            ft.dropdown.Option("Juventus"),
            ft.dropdown.Option("Al-Nassr"),
        ],
        on_change=cambiar_imagen
    )

    imagenEquipo = ft.Image(src="aa")


    page.add (ddEquipo,imagenEquipo)


    #vEquipos= ["Aston Villa", "Man-United", "Juventus", "Real Madrid", "Al_Nassr"]
    #menu=ft.Dropdown(hint_text="Selecciona un equipo",width=250,on_change=cambiar_imagen)
    '''
    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))

    def GUARDAR():
        cambiar_imagen = ft.dropdown.Option.get()
        vEquipos.append(cambiar_imagen)
    '''

    #seleccionar_equipo=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=GUARDAR)
    #page.add(seleccionar_equipo)
    
    


ft.app(target=main,assets_dir="imagenes")