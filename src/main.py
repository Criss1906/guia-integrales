from nicegui import ui, app
import os
from estilo import add_custom_styles
from navbar import create_navbar



def main():
    ui.page_title('Integrales - Guía Completa')
    add_custom_styles()

    # Barra de navegación fija en la parte superior
    create_navbar()

    # Contenedor principal para todas las secciones
    with ui.column().classes('main-content-container'):
        # Puedes añadir una sección de bienvenida aquí si quieres
        with ui.element('div').classes('hero-section q-pa-xl text-center'):
            ui.label('Integrales: Teoría y Práctica').classes('text-6xl font-bold mb-4 gradient-text')
            ui.label('Una guía completa para entender y resolver integrales, paso a paso.').classes('text-xl text-gray-700 opacity-90 mb-8')
            ui.html('<p class="text-lg">Explora los diferentes métodos:</p>').classes('text-gray-600')
            with ui.row().classes('justify-center q-gutter-md q-mt-md'):
                ui.button('Empezar', on_click=lambda: ui.run_javascript('window.location.hash = "#contexto";')).classes('q-py-md q-px-lg rounded-full text-white font-bold bg-blue-500 hover:bg-blue-600 transition-all shadow-lg')


        # --- Secciones de Contenido ---
        # Cada sección ahora es una función que se llama aquí, y se le asigna un ID.

        contexto_section()
        indefinidas_section()
        definidas_section()
        cambio_variables_section()
        partes_section()
        trigonometricas_section()
        sustitucion_trig_section()
        fracciones_parciales_section()
        area_bajo_curva_section()
        volumen_solidos_revolucion_section() 
        longitud_arco_section() 
        ley_hooke_section()
        

    with ui.footer().classes('footer'):
        ui.label('© 2025 Guía de Integrales. Todos los derechos reservados.').classes('text-sm opacity-80')

# --- DEFINICIÓN DE CADA SECCIÓN ---
# Cada una de estas funciones crea el contenido de una sección
# y lo envuelve en un div con un ID para la navegación con anclas.

def contexto_section():
    with ui.element('div').classes('section-card').props('id="contexto"'):
        ui.label('Contexto de las Integrales').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=500&h=300&fit=crop').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        Las integrales son una herramienta fundamental en el cálculo que nos permite 
                        resolver dos problemas centrales: el cálculo de <strong>áreas bajo curvas</strong> y el 
                        problema inverso de la derivación, es decir, encontrar una función a partir 
                        de su derivada (la <strong>antiderivada</strong>).
                    </p>
                    <p class="section-text">
                        Históricamente, la necesidad de calcular áreas de formas irregulares llevó 
                        al desarrollo de conceptos como la suma de Riemann, que aproxima el área 
                        dividiendo la región en rectángulos delgados. A medida que el número de 
                        rectángulos tiende a infinito y su ancho tiende a cero, esta suma se convierte 
                        en la integral definida.
                    </p>
                    <p class="section-text">
                        El <strong>Teorema Fundamental del Cálculo</strong> estableció la conexión profunda 
                        entre la derivación y la integración, revolucionando las matemáticas al 
                        proporcionar un método eficiente para calcular integrales definidas 
                        utilizando antiderivadas.
                    </p>
                ''')

def indefinidas_section():
    with ui.element('div').classes('section-card').props('id="indefinidas"'):
        ui.label('Integrales Indefinidas').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://images.unsplash.com/photo-1509228468518-180dd4864904?w=500&h=300&fit=crop').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        Una <strong>integral indefinida</strong> representa la familia de todas las antiderivadas 
                        de una función. Se caracteriza por no tener límites de integración y siempre incluir 
                        una constante arbitraria C.
                    </p>
                    <div class="formula-box">∫f(x)dx = F(x) + C</div>
                    <h4 style="color: #667eea; margin-top: 20px;">Integrales Básicas:</h4>
                    <div class="formula-box">
                        ∫xⁿ dx = (xⁿ⁺¹)/(n+1) + C, n ≠ -1<br>
                        ∫1/x dx = ln|x| + C<br>
                        ∫eˣ dx = eˣ + C<br>
                        ∫sin(x) dx = -cos(x) + C<br>
                        ∫cos(x) dx = sin(x) + C
                    </div>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integral Indefinida</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫(3x² + 2x - 5)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Aplicar la propiedad de linealidad')
                ui.html('<div class="formula-box">∫(3x² + 2x - 5)dx = ∫3x²dx + ∫2xdx - ∫5dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Sacar las constantes')
                ui.html('<div class="formula-box">= 3∫x²dx + 2∫xdx - 5∫1dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Aplicar las fórmulas básicas')
                ui.html('<div class="formula-box">= 3(x³/3) + 2(x²/2) - 5x + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Simplificar')
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>= x³ + x² - 5x + C</strong></div>')

def definidas_section():
    with ui.element('div').classes('section-card').props('id="definidas"'):
        ui.label('Integrales Definidas').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('data:image/png;base64,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').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        Una <strong>integral definida</strong> representa el área neta bajo la curva de una función 
                        en un intervalo específico [a, b]. A diferencia de las integrales indefinidas, 
                        produce un valor numérico y no incluye la constante de integración.
                    </p>
                    <div class="formula-box">∫<sub>a</sub><sup>b</sup> f(x)dx = F(b) - F(a)</div>
                    <h4 style="color: #667eea; margin-top: 20px;">Propiedades Clave:</h4>
                    <ul class="section-text" style="list-style-type: disc; margin-left: 20px;">
                        <li>Si a = b, entonces ∫<sub>a</sub><sup>a</sup> f(x)dx = 0</li>
                        <li>∫<sub>a</sub><sup>b</sup> f(x)dx = -∫<sub>b</sub><sup>a</sup> f(x)dx</li>
                        <li>∫<sub>a</sub><sup>b</sup> kf(x)dx = k∫<sub>a</sub><sup>b</sup> f(x)dx</li>
                        <li>∫<sub>a</sub><sup>b</sup> [f(x) ± g(x)]dx = ∫<sub>a</sub><sup>b</sup> f(x)dx ± ∫<sub>a</sub><sup>b</sup> g(x)dx</li>
                    </ul>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integral Definida</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫<sub>0</sub><sup>2</sup> (x² + 1)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Encontrar la antiderivada de f(x) = x² + 1')
                ui.html('<div class="formula-box">F(x) = ∫(x² + 1)dx = x³/3 + x</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Evaluar F(b) - F(a)')
                ui.html('<div class="formula-box">F(2) - F(0) = (2³/3 + 2) - (0³/3 + 0)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Simplificar')
                ui.html('<div class="formula-box">= (8/3 + 6/3) - 0 = 14/3</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>∫<sub>0</sub><sup>2</sup> (x² + 1)dx = 14/3</strong></div>')

def cambio_variables_section():
    with ui.element('div').classes('section-card').props('id="cambio_variables"'):
        ui.label('Método por Cambio de Variables').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOctJz8S49oN8BrjJ5yoI9g6pptm2Z2-iTig&s').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        El <strong>método por cambio de variables</strong> (o sustitución) es una técnica 
                        para simplificar integrales complejas transformándolas en formas más fáciles 
                        de integrar. Se basa en la regla de la cadena para derivadas.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Fórmula General:</h4>
                    <div class="formula-box">∫f(g(x))g'(x)dx = ∫f(u)du</div>
                    <p class="section-text">
                        Donde <strong>u = g(x)</strong> y <strong>du = g'(x)dx</strong>.
                        El objetivo es identificar una parte de la integral (g(x)) cuya derivada (g'(x)) 
                        también esté presente, o pueda ser ajustada con una constante.
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Cambio de Variables</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫x(x² + 3)⁵dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Identificar u y du')
                ui.html('<div class="formula-box">Sea u = x² + 3<br>Entonces, du = 2xdx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Ajustar du para que coincida con la integral')
                ui.html('<div class="formula-box">Necesitamos xdx, así que (1/2)du = xdx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Sustituir en la integral')
                ui.html('<div class="formula-box">∫(x² + 3)⁵ * xdx = ∫u⁵ * (1/2)du = (1/2)∫u⁵du</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Integrar respecto a u')
                ui.html('<div class="formula-box">= (1/2) * (u⁶/6) + C = u⁶/12 + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 5:</strong> Revertir la sustitución')
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>= (x² + 3)⁶/12 + C</strong></div>')

def partes_section():
    with ui.element('div').classes('section-card').props('id="partes"'):
        ui.label('Método por Partes').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://pbs.twimg.com/media/D7LH5j6WsAAuOap.jpg').classes('section-image') # Tu imagen de la vaca
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        El <strong>método por partes</strong> se utiliza para integrar productos de funciones, 
                        especialmente cuando no pueden resolverse con una sustitución simple. Se basa 
                        en la regla del producto para derivadas, y su fórmula es:
                    </p>
                    <div class="formula-box">∫udv = uv - ∫vdu</div>
                    <h4 style="color: #667eea; margin-top: 20px;">Criterio ILATE:</h4>
                    <p class="section-text">
                        Para elegir quién es 'u' y quién es 'dv', se puede usar la regla mnemotécnica 
                        <strong>ILATE</strong>, que indica el orden de preferencia para 'u':
                    </p>
                    <ul class="section-text" style="list-style-type: disc; margin-left: 20px;">
                        <li><strong>I</strong>nversas trigonométricas (arcsin, arctan, etc.)</li>
                        <li><strong>L</strong>ogorítmicas (ln x, log x, etc.)</li>
                        <li><strong>A</strong>lgebraicas (x², 3x, etc.)</li>
                        <li><strong>T</strong>rigonométricas (sin x, cos x, etc.)</li>
                        <li><strong>E</strong>xponenciales (eˣ, aˣ, etc.)</li>
                    </ul>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integración por Partes</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫x sin(x)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Elegir u y dv (usando ILATE, x es Algebraica, sin(x) es Trigonométrica)')
                ui.html('<div class="formula-box">u = x &nbsp;&nbsp;&nbsp;&nbsp; dv = sin(x)dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Calcular du y v')
                ui.html('<div class="formula-box">du = dx &nbsp;&nbsp;&nbsp;&nbsp; v = ∫sin(x)dx = -cos(x)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Aplicar la fórmula ∫udv = uv - ∫vdu')
                ui.html('<div class="formula-box">= x(-cos(x)) - ∫(-cos(x))dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Simplificar y resolver la integral restante')
                ui.html('<div class="formula-box">= -x cos(x) + ∫cos(x)dx<br>= -x cos(x) + sin(x) + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>∫x sin(x)dx = -x cos(x) + sin(x) + C</strong></div>')

def trigonometricas_section():
    with ui.element('div').classes('section-card').props('id="trigonometricas"'):
        ui.label('Integrales Trigonométricas').classes('section-title')
        ui.html('''
            <p class="section-text">
                Las <strong>integrales trigonométricas</strong> implican funciones como seno, coseno, tangente, etc. 
                Su resolución a menudo requiere el uso de identidades trigonométricas para simplificar 
                la expresión antes de integrar.
            </p>
            <p class="section-text">
                A continuación, se presentan estrategias comunes para integrales de la forma 
                ∫sinⁿ(x)cosᵐ(x)dx y ∫tanⁿ(x)secᵐ(x)dx.
            </p>
        ''')
        ui.html('<h3 style="color: #667eea; text-align: center; margin-top: 30px;">Caso 1: sinⁿ(x)cosᵐ(x)dx cuando n es impar o m es impar</h3>')
        ui.html('''
            <p class="section-text">
                Si la potencia de seno (n) es impar, separamos un sin(x) y convertimos los senos restantes 
                a cosenos usando sin²(x) = 1 - cos²(x). Luego, hacemos u = cos(x).
                Si la potencia de coseno (m) es impar, separamos un cos(x) y convertimos los cosenos 
                restantes a senos usando cos²(x) = 1 - sin²(x). Luego, hacemos u = sin(x).
            </p>
            <div class="formula-box">
                Ej. ∫sin³(x)cos²(x)dx = ∫sin²(x)cos²(x)sin(x)dx<br>
                = ∫(1 - cos²(x))cos²(x)sin(x)dx.  Sea u = cos(x), du = -sin(x)dx.
            </div>
        ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integral Trigonométrica (n impar)</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫sin³(x)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Separar un sin(x) y usar identidad')
                ui.html('<div class="formula-box">∫sin²(x)sin(x)dx = ∫(1 - cos²(x))sin(x)dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Sustitución: u = cos(x), du = -sin(x)dx')
                ui.html('<div class="formula-box">= ∫(1 - u²)(-du) = ∫(u² - 1)du</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Integrar y reemplazar u')
                ui.html('<div class="formula-box">= u³/3 - u + C = cos³(x)/3 - cos(x) + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>∫sin³(x)dx = cos³(x)/3 - cos(x) + C</strong></div>')

        ui.html('<h3 style="color: #667eea; text-align: center; margin-top: 30px;">Caso 2: sinⁿ(x)cosᵐ(x)dx cuando n y m son pares</h3>')
        ui.html('''
            <p class="section-text">
                Si ambas potencias son pares, se usan las identidades de reducción de potencia:
            </p>
            <div class="formula-box">
                sin²(x) = (1 - cos(2x))/2<br>
                cos²(x) = (1 + cos(2x))/2
            </div>
            <p class="section-text">
                Esto eleva el argumento a 2x y reduce las potencias, posiblemente requiriendo varias aplicaciones.
            </p>
        ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integral Trigonométrica (n y m pares)</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫sin²(x)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Usar la identidad de reducción de potencia')
                ui.html('<div class="formula-box">∫sin²(x)dx = ∫(1 - cos(2x))/2 dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Separar la integral')
                ui.html('<div class="formula-box">= (1/2)∫(1 - cos(2x))dx = (1/2)[∫1dx - ∫cos(2x)dx]</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Integrar (recordar u=2x para cos(2x))')
                ui.html('<div class="formula-box">= (1/2)[x - (sin(2x))/2] + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>∫sin²(x)dx = x/2 - (sin(2x))/4 + C</strong></div>')

        ui.html('<h3 style="color: #667eea; text-align: center; margin-top: 30px;">Caso 3: Integrales con tanⁿ(x)secᵐ(x)dx</h3>')
        ui.html('''
            <p class="section-text">
                Para integrales de la forma ∫tanⁿ(x)secᵐ(x)dx, las estrategias varían dependiendo 
                de las potencias de secante (m) y tangente (n).
            </p>
            <ul class="section-text" style="list-style-type: disc; margin-left: 20px;">
                <li><strong>Si m es par y m ≥ 2:</strong> Separar sec²(x) y convertir las secantes restantes a tangentes (sec²(x) = tan²(x) + 1). Usar u = tan(x), du = sec²(x)dx.</li>
                <li><strong>Si n es impar y n ≥ 1:</strong> Separar sec(x)tan(x) y convertir las tangentes restantes a secantes (tan²(x) = sec²(x) - 1). Usar u = sec(x), du = sec(x)tan(x)dx.</li>
                <li><strong>Otros casos:</strong> A veces requieren identidades de potencia o integración por partes.</li>
            </ul>
        ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Integral con Tangente y Secante</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫tan²(x)sec⁴(x)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Potencia de secante es par, separar sec²(x)')
                ui.html('<div class="formula-box">∫tan²(x)sec²(x)sec²(x)dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Convertir las secantes restantes a tangentes')
                ui.html('<div class="formula-box">= ∫tan²(x)(tan²(x) + 1)sec²(x)dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Sustitución: u = tan(x), du = sec²(x)dx')
                ui.html('<div class="formula-box">= ∫u²(u² + 1)du = ∫(u⁴ + u²)du</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Integrar y reemplazar u')
                ui.html('<div class="formula-box">= u⁵/5 + u³/3 + C = tan⁵(x)/5 + tan³(x)/3 + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>∫tan²(x)sec⁴(x)dx = tan⁵(x)/5 + tan³(x)/3 + C</strong></div>')

def sustitucion_trig_section():
    with ui.element('div').classes('section-card').props('id="sustitucion_trig"'):
        ui.label('Método por Sustitución Trigonométrica').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://cienciayt.com/wp-content/uploads/matematicas/calculo-integral/sustitucion-trigonometrica-a.png').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        La <strong>sustitución trigonométrica</strong> es un método usado para resolver integrales 
                        que contienen expresiones de la forma <strong>√(a² ± x²)</strong> o <strong>√(x² - a²)</strong>, 
                        transformándolas en integrales trigonométricas más sencillas. Se basa en las 
                        identidades pitagóricas.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Casos Comunes:</h4>
                    <ul class="section-text" style="list-style-type: disc; margin-left: 20px;">
                        <li><strong>Para √(a² - x²):</strong> Hacer x = a sin(θ). Implica √(a²cos²(θ)) = a|cos(θ)|.</li>
                        <li><strong>Para √(a² + x²):</strong> Hacer x = a tan(θ). Implica √(a²sec²(θ)) = a|sec(θ)|.</li>
                        <li><strong>Para √(x² - a²):</strong> Hacer x = a sec(θ). Implica √(a²tan²(θ)) = a|tan(θ)|.</li>
                    </ul>
                    <p class="section-text">
                        Después de la integración, es crucial volver a sustituir θ en términos de x, 
                        usando un triángulo rectángulo de referencia.
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Sustitución Trigonométrica</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫√(9 - x²)dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Identificar el tipo (a² - x²) y hacer la sustitución')
                ui.html('<div class="formula-box">a = 3. Sea x = 3sin(θ) &nbsp;&nbsp;&nbsp;&nbsp; dx = 3cos(θ)dθ</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Sustituir en la expresión √(9 - x²)')
                ui.html('<div class="formula-box">√(9 - (3sin(θ))²) = √(9 - 9sin²(θ)) = √(9(1 - sin²(θ))) = √(9cos²(θ)) = 3|cos(θ)|</div>')
                ui.html('<p class="section-text">Asumimos que cos(θ) ≥ 0, por lo que 3cos(θ).</p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Sustituir todo en la integral')
                ui.html('<div class="formula-box">∫(3cos(θ))(3cos(θ))dθ = ∫9cos²(θ)dθ</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Usar identidad de reducción de potencia para cos²(θ)')
                ui.html('<div class="formula-box">= 9∫(1 + cos(2θ))/2 dθ = (9/2)∫(1 + cos(2θ))dθ<br>= (9/2)[θ + (sin(2θ))/2] + C</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 5:</strong> Revertir a x (usar sin(2θ) = 2sin(θ)cos(θ) y triángulo de referencia)')
                ui.html('<p class="section-text">De x = 3sin(θ), tenemos sin(θ) = x/3. En un triángulo, lado opuesto = x, hipotenusa = 3. Lado adyacente = √(9 - x²).</p>')
                ui.html('<div class="formula-box">θ = arcsin(x/3)<br>cos(θ) = √(9 - x²)/3<br>sin(2θ) = 2(x/3)(√(9 - x²)/3) = 2x√(9 - x²)/9</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 6:</strong> Sustituir los valores en la integral final')
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>= (9/2)[arcsin(x/3) + (2x√(9 - x²))/18] + C<br>= (9/2)arcsin(x/3) + x√(9 - x²)/2 + C</strong></div>')

def fracciones_parciales_section():
    with ui.element('div').classes('section-card').props('id="fracciones_parciales"'):
        ui.label('Método por Fracciones Parciales').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('data:image/png;base64,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').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        El <strong>método de fracciones parciales</strong> se usa para integrar funciones racionales 
                        (polinomios divididos por polinomios) cuando el grado del numerador es menor que 
                        el grado del denominador. Consiste en descomponer la fracción original en una suma 
                        de fracciones más simples que son fáciles de integrar.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Casos de Descomposición:</h4>
                    <ul class="section-text" style="list-style-type: disc; margin-left: 20px;">
                        <li><strong>Factores lineales no repetidos:</strong> A/(ax+b)</li>
                        <li><strong>Factores lineales repetidos:</strong> A/(ax+b) + B/(ax+b)² + ...</li>
                        <li><strong>Factores cuadráticos irreducibles no repetidos:</strong> (Ax+B)/(ax²+bx+c)</li>
                        <li><strong>Factores cuadráticos irreducibles repetidos:</strong> (Ax+B)/(ax²+bx+c) + (Cx+D)/(ax²+bx+c)² + ...</li>
                    </ul>
                    <p class="section-text">
                        Una vez descompuesta, cada término se integra usando logaritmos o arctangentes.
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Fracciones Parciales</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular: ∫(1 / (x² - 1))dx</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Factorizar el denominador')
                ui.html('<div class="formula-box">x² - 1 = (x - 1)(x + 1)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Descomponer en fracciones parciales')
                ui.html('<div class="formula-box">1 / ((x - 1)(x + 1)) = A/(x - 1) + B/(x + 1)</div>')
                ui.html('<p class="section-text">Multiplicar por (x-1)(x+1): 1 = A(x+1) + B(x-1)</p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Encontrar A y B')
                ui.html('<p class="section-text">Si x = 1: 1 = A(1+1) => 1 = 2A => A = 1/2</p>')
                ui.html('<p class="section-text">Si x = -1: 1 = B(-1-1) => 1 = -2B => B = -1/2</p>')
                ui.html('<div class="formula-box">Entonces: 1 / (x² - 1) = (1/2)/(x - 1) - (1/2)/(x + 1)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Integrar cada fracción')
                ui.html('<div class="formula-box">∫[(1/2)/(x - 1) - (1/2)/(x + 1)]dx = (1/2)∫1/(x - 1)dx - (1/2)∫1/(x + 1)dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 5:</strong> Resolver las integrales (usando ∫1/u du = ln|u|)')
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>= (1/2)ln|x - 1| - (1/2)ln|x + 1| + C<br>= (1/2)ln|(x - 1)/(x + 1)| + C</strong></div>')

def area_bajo_curva_section():
    with ui.element('div').classes('section-card').props('id="area_bajo_curva"'):
        ui.label('Área Bajo la Curva').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGPNupihiTxTFJHnYdPcBLQiJumYpJj3yiag&s').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        El <strong>área bajo la curva</strong> es una de las aplicaciones más directas y visuales 
                        de la integral definida. Representa la acumulación de la función en un intervalo 
                        dado, y gráficamente, es el área de la región acotada por la función, el eje X 
                        y las líneas verticales en los límites de integración.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Fórmula:</h4>
                    <div class="formula-box">Área = ∫<sub>a</sub><sup>b</sup> f(x)dx</div>
                    <p class="section-text">
                        Es importante recordar que si la función f(x) es negativa en parte del intervalo, 
                        la integral dará un valor negativo para esa área. Si se busca el área "total" 
                        (siempre positiva), se debe tomar el valor absoluto de la función o dividir la 
                        integral en secciones donde la función cambia de signo.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Área entre dos curvas:</h4>
                    <div class="formula-box">Área = ∫<sub>a</sub><sup>b</sup> [f(x) - g(x)]dx</div>
                    <p class="section-text">
                        Donde f(x) es la función "superior" y g(x) es la función "inferior" en el intervalo [a, b].
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Área Bajo la Curva</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular el área bajo la curva f(x) = x² desde x = 0 hasta x = 2.</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Establecer la integral definida')
                ui.html('<div class="formula-box">Área = ∫<sub>0</sub><sup>2</sup> x² dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Encontrar la antiderivada de x²')
                ui.html('<div class="formula-box">F(x) = x³/3</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Evaluar la antiderivada en los límites')
                ui.html('<div class="formula-box">Área = F(2) - F(0) = (2³/3) - (0³/3)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>Área = 8/3 unidades cuadradas</strong></div>')

def volumen_solidos_revolucion_section():
    with ui.element('div').classes('section-card').props('id="volumen_solidos_revolucion"'):
        ui.label('Volumen de Sólidos de Revolución').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                # Puedes cambiar esta imagen por una más representativa si encuentras una mejor
                ui.image('data:image/jpeg;base64,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').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        Las integrales también nos permiten calcular el volumen de sólidos que se forman 
                        al girar una región plana alrededor de un eje. Los métodos principales son el 
                        <strong>método del disco/arandela</strong> y el <strong>método de los cascarones cilíndricos</strong>.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Método del Disco/Arandela:</h4>
                    <p class="section-text">
                        Se usa cuando la región se gira y no hay espacio entre la región y el eje de rotación 
                        (disco), o cuando sí hay un espacio (arandela).
                    </p>
                    <div class="formula-box">
                        <strong>Eje X:</strong> V = ∫<sub>a</sub><sup>b</sup> π [f(x)]² dx (Disco)<br>
                        <strong>Eje X:</strong> V = ∫<sub>a</sub><sup>b</sup> π ([R(x)]² - [r(x)]²) dx (Arandela, R(x) radio exterior, r(x) radio interior)<br>
                        <strong>Eje Y:</strong> V = ∫<sub>c</sub><sup>d</sup> π [g(y)]² dy (Disco)
                    </div>
                    <h4 style="color: #667eea; margin-top: 20px;">Método de Cascarones Cilíndricos:</h4>
                    <p class="section-text">
                        Se usa cuando el eje de rotación es paralelo al eje de integración, formando "cilindros" huecos.
                    </p>
                    <div class="formula-box">
                        <strong>Eje Y:</strong> V = ∫<sub>a</sub><sup>b</sup> 2πx f(x) dx<br>
                        <strong>Eje X:</strong> V = ∫<sub>c</sub><sup>d</sup> 2πy g(y) dy
                    </div>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Volumen por Disco</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular el volumen del sólido formado al girar y = x² desde x=0 hasta x=2 alrededor del eje X.</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Identificar el método y la fórmula (Disco, eje X)')
                ui.html('<div class="formula-box">V = ∫<sub>a</sub><sup>b</sup> π [f(x)]² dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Establecer la integral')
                ui.html('<div class="formula-box">V = ∫<sub>0</sub><sup>2</sup> π (x²)² dx = π ∫<sub>0</sub><sup>2</sup> x⁴ dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Encontrar la antiderivada e integrar')
                ui.html('<div class="formula-box">π [x⁵/5]<sub>0</sub><sup>2</sup></div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Evaluar en los límites')
                ui.html('<div class="formula-box">V = π [(2⁵/5) - (0⁵/5)] = π (32/5)</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>V = 32π/5 unidades cúbicas</strong></div>')


def longitud_arco_section():
    with ui.element('div').classes('section-card').props('id="longitud_arco"'):
        ui.label('Longitud de Arco').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                # Puedes cambiar esta imagen por una más representativa si encuentras una mejor
                ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh3XLds-cLYYLs9RwqP6K1LNyQMoRxkSFh-Q&s').classes('section-image')
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        La <strong>longitud de arco</strong> nos permite calcular la distancia a lo largo de una curva 
                        suave en un intervalo dado. Es una aplicación directa de las integrales definidas 
                        y se deriva del teorema de Pitágoras aplicado a pequeños segmentos de la curva.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Fórmula General (en función de x):</h4>
                    <div class="formula-box">L = ∫<sub>a</sub><sup>b</sup> √(1 + [f'(x)]²) dx</div>
                    <p class="section-text">
                        Donde f'(x) es la derivada de la función f(x) con respecto a x.
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Fórmula General (en función de y):</h4>
                    <div class="formula-box">L = ∫<sub>c</sub><sup>d</sup> √(1 + [g'(y)]²) dy</div>
                    <p class="section-text">
                        Donde g'(y) es la derivada de la función g(y) con respecto a y.
                        La clave para aplicar esta fórmula es poder calcular la derivada y que la integral resultante sea manejable.
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Longitud de Arco</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Calcular la longitud de arco de y = x³/² desde x = 0 hasta x = 4.</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Calcular la derivada de la función')
                ui.html('<div class="formula-box">f(x) = x³/²<br>f\'(x) = (3/2)x¹/²</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Calcular [f\'(x)]²')
                ui.html('<div class="formula-box">[f\'(x)]² = ((3/2)x¹/²)² = (9/4)x</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Sustituir en la fórmula de longitud de arco')
                ui.html('<div class="formula-box">L = ∫<sub>0</sub><sup>4</sup> √(1 + (9/4)x) dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Resolver la integral (usar sustitución u = 1 + (9/4)x, du = (9/4)dx)')
                ui.html('<div class="formula-box">Si u = 1 + (9/4)x, entonces du = (9/4)dx => dx = (4/9)du<br>Límites: x=0 => u=1; x=4 => u=1+9 = 10<br>L = ∫<sub>1</sub><sup>10</sup> √u (4/9)du = (4/9)∫<sub>1</sub><sup>10</sup> u¹/²du</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 5:</strong> Integrar y evaluar')
                ui.html('<div class="formula-box">= (4/9) [ (u³/²) / (3/2) ]<sub>1</sub><sup>10</sup> = (4/9) * (2/3) [u³/²]<sub>1</sub><sup>10</sup><br>= (8/27) [10³/² - 1³/²] = (8/27) [10√10 - 1]</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>L = (8/27)(10√10 - 1) unidades de longitud</strong></div>')

def ley_hooke_section():
    with ui.element('div').classes('section-card').props('id="ley_hooke"'):
        ui.label('Ley de Hooke y Trabajo').classes('section-title')
        with ui.row().classes('w-full gap-8 items-center'):
            with ui.column().classes('flex-1'):
                ui.image('data:image/jpeg;base64,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').classes('section-image') # Puedes cambiar la imagen por una de un resorte
            with ui.column().classes('flex-1'):
                ui.html('''
                    <p class="section-text">
                        La <strong>Ley de Hooke</strong> establece que la fuerza (F) necesaria para extender 
                        o comprimir un resorte una cierta distancia (x) desde su posición de equilibrio 
                        es directamente proporcional a esa distancia.
                    </p>
                    <div class="formula-box">F = kx</div>
                    <p class="section-text">
                        Donde:
                        <ul>
                            <li><strong>F</strong> es la fuerza aplicada.</li>
                            <li><strong>k</strong> es la constante del resorte (o constante de elasticidad), 
                                que mide la rigidez del resorte. Un valor alto de 'k' significa un resorte más rígido.</li>
                            <li><strong>x</strong> es la distancia de estiramiento o compresión desde la posición de equilibrio.</li>
                        </ul>
                    </p>
                    <h4 style="color: #667eea; margin-top: 20px;">Cálculo del Trabajo (mediante Integrales):</h4>
                    <p class="section-text">
                        Cuando la fuerza no es constante, como en el caso de un resorte, el trabajo (W) 
                        realizado para estirar o comprimir el resorte se calcula mediante una integral. 
                        Dado que la fuerza F(x) = kx varía con la distancia, integramos la fuerza con 
                        respecto a la distancia.
                    </p>
                    <div class="formula-box">W = ∫<sub>a</sub><sup>b</sup> F(x)dx = ∫<sub>a</sub><sup>b</sup> kx dx</div>
                    <p class="section-text">
                        Donde 'a' es la posición inicial y 'b' es la posición final.
                    </p>
                ''')
        with ui.element('div').classes('exercise-box'):
            ui.html('<h3 style="color: #667eea; text-align: center;">📝 Ejercicio: Trabajo usando Ley de Hooke</h3>')
            ui.html('<p style="text-align: center; font-size: 1.2em;"><strong>Un resorte tiene una constante k = 200 N/m. Calcular el trabajo necesario para estirarlo de 0.1 m a 0.3 m desde su posición de equilibrio.</strong></p>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 1:</strong> Identificar la función de fuerza y los límites de integración')
                ui.html('<div class="formula-box">F(x) = kx = 200x<br>Límites: a = 0.1 m, b = 0.3 m</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 2:</strong> Establecer la integral del trabajo')
                ui.html('<div class="formula-box">W = ∫<sub>0.1</sub><sup>0.3</sup> 200x dx</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 3:</strong> Encontrar la antiderivada e integrar')
                ui.html('<div class="formula-box">= 200 [x²/2]<sub>0.1</sub><sup>0.3</sup> = 100 [x²]<sub>0.1</sub><sup>0.3</sup></div>')
            with ui.element('div').classes('step-box'):
                ui.html('<strong>Paso 4:</strong> Evaluar en los límites')
                ui.html('<div class="formula-box">W = 100 [(0.3)² - (0.1)²]<br>= 100 [0.09 - 0.01]<br>= 100 [0.08]</div>')
            with ui.element('div').classes('step-box'):
                ui.html('<div class="formula-box" style="background: #e8f5e8; border-left-color: #28a745;"><strong>W = 8 Joules (J)</strong></div>')

if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(title='Integrales - Guía Completa', favicon='∫', dark=False, port=int(os.environ.get('PORT', 8080)), host='0.0.0.0')
