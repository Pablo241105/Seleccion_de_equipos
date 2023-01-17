import flet as ft

def main(page: ft.Page):
    page.title="SELECCION DE EQUIPOS"
    EQUIPO=""

    def dropdown_changed(e):
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
        on_change=dropdown_changed
    )

    page.add(EQUIPOS)
ft.app(target=main)