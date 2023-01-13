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

ft.app(target=main)