import flet as ft

def main(page: ft.Page):
    page.title="SELECCION DE EQUIPOS"

    def cambiar_imagen(e):
        if (EQUIPOS.value == "Aston Villa"):
            EQUIPO = "imagenes/Aston-Villa.png"
            print(f"Aston Villa {EQUIPO}")
        elif (EQUIPOS.value == "Man United"):
            EQUIPO = "imagenes/Man-United.png"
            print(f"Man United {EQUIPO}")
        elif (EQUIPOS.value == "Juventus"):
            EQUIPO = "imagenes/Juventus.png"
            print(f"Juventus {EQUIPO}")
        elif (EQUIPOS.value == "Real Madrid"):
            EQUIPO = "imagenes/Real Madrid.png"
            print(f"Real Madrid {EQUIPO}")
        else:
            EQUIPO = "Al_Nassr.png"
            print(f"Al-Nassr {EQUIPO}")

        page.update()

    EQUIPOS = ft.Dropdown(label="Equipos",width=500,
        options=[
            ft.dropdown.Option("Aston Villa"),
            ft.dropdown.Option("Man United"),
            ft.dropdown.Option("Real Madrid"),
            ft.dropdown.Option("Juventus"),
            ft.dropdown.Option("Al-Nassr"),
        ],
        on_change=cambiar_imagen
    )
    vEquipos= ["Aston Villa", "Man-United", "Juventus", "Real Madrid", "Al_Nassr"]
    menu=ft.Dropdown(hint_text="Selecciona un equipo",width=250,on_change=cambiar_imagen)

    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))

    def GUARDAR():
        cambiar_imagen = ft.dropdown.Option.get()
        vEquipos.append(cambiar_imagen)

    seleccionar_equipo=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=GUARDAR)
    page.add(seleccionar_equipo)
    page.update()

    page.add(EQUIPOS)
ft.app(target=main)