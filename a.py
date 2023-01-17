import flet as ft

def main(page: ft.Page):
    page.title="SELECCION DE EQUIPOS"
    EQUIPO=""

    page.add(EQUIPO)
    
    img = ft.Image(src=f"imagenes/{EQUIPO}")

    page.add(img)

ft.app(target=main, assets_dir="imagenes")