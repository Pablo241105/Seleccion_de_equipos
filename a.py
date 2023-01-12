import flet as ft

def main(page: ft.Page):
    page.add(
    ft.Dropdown(label="Color",hint_text="Elige tu equipo",options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ],autofocus=True,))

ft.app(target=main)