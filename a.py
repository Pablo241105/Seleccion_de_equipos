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


        img.src=f"{EQUIPO}"
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
    
    img = ft.Image(src=f"imagenes/{EQUIPO}")

    page.add(img)

<<<<<<< Updated upstream
imagenes= ""

def dropdown_changed(e):
        if (main.value == "Aston Villa"):
            imagenes = "imagenes/Aston-Villa.png"
            print(f"fresa al poder {imagenes}")
        elif (main.value == "Man United"):
            imagenes = "imagenes/Man-United.png"
            print("platano al poder")
        elif (main.value == "Real Madrid"):
            imagenes = "imagenes/Real Madrid.png"
            print("platano al poder")
        elif (main.value == "Juventus"):
            imagenes = "imagenes/Juventus.png"
            print("platano al poder")
        elif (main.value == "Al-Nassr"):
            imagenes = "imagenes/Al_Nassr.png"
            print("platano al poder")
        imagenes.src=f"{imagenes}"
        page.update()

ft.app(target=main,assets_dir="imagenes")
=======
ft.app(target=main, assets_dir="imagenes")
>>>>>>> Stashed changes
