from nicegui import ui

def create_navbar():
    with ui.header().classes('navbar-header'):
        with ui.row().classes('w-full items-center justify-between'):
            ui.label('Guía de Integrales').classes('text-2xl font-bold text-white')
            with ui.row():
                ui.link('Inicio', '/#').classes('nav-button')
                ui.link('Contexto', '/#contexto').classes('nav-button')
                ui.link('Indefinidas', '/#indefinidas').classes('nav-button')
                ui.link('Definidas', '/#definidas').classes('nav-button')
                ui.link('Cambio de Variables', '/#cambio_variables').classes('nav-button')
                ui.link('Partes', '/#partes').classes('nav-button')
                ui.link('Trigonométricas', '/#trigonometricas').classes('nav-button')
                ui.link('Sust. Trigonométrica', '/#sustitucion_trig').classes('nav-button')
                ui.link('Fracciones Parciales', '/#fracciones_parciales').classes('nav-button')
                ui.link('Área Bajo Curva', '/#area_bajo_curva').classes('nav-button')
                ui.link('Volumen Sólidos', '/#volumen_solidos_revolucion').classes('nav-button')
                ui.link('Longitud de Arco', '/#longitud_arco').classes('nav-button')
                ui.link('Ley de Hooke', '/#ley_hooke').classes('nav-button')