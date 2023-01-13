import flet as ft

def main(page: ft.Page):
    page.title="SELECCION DE EQUIPOS"
    page.add(
    ft.Dropdown(label="Equipos",hint_text="Elige tu equipo",options=[
            ft.dropdown.Option("Aston Villa"),
            ft.dropdown.Option("Man United"),
            ft.dropdown.Option("Real Madrid"),
            ft.dropdown.Option("Juventus"),
            ft.dropdown.Option("Al-Nassr"),
            ],autofocus=True,))

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