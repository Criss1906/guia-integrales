from nicegui import ui

def add_custom_styles():
    ui.add_head_html('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

            body {
                font-family: 'Poppins', sans-serif;
                background-color: #f0f2f5; /* Light gray background */
                color: #333;
                margin: 0;
                padding: 0;
            }
            .navbar-header {
                background: linear-gradient(90deg, #667eea, #764ba2); /* Gradient from purple to blue */
                color: white;
                padding: 15px 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                position: fixed;
                width: 100%;
                top: 0;
                left: 0;
                z-index: 1000;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .nav-button {
                background-color: transparent !important;
                color: white !important;
                border: none !important;
                font-weight: 600;
                padding: 8px 15px;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .nav-button:hover {
                background-color: rgba(255, 255, 255, 0.2) !important;
                transform: translateY(-2px);
            }
            .main-content-container {
                padding-top: 80px; /* Ajusta el padding para el header fijo */
                max-width: 1000px; /* Un poco más ancho para el contenido */
                margin: 0 auto;
                padding-left: 20px;
                padding-right: 20px;
            }
            .hero-section {
                background: linear-gradient(135deg, #e0f7fa, #bbdefb); /* Light blue gradient */
                border-radius: 15px;
                margin-top: 20px;
                margin-bottom: 40px;
                padding: 50px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            }
            .section-card {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 30px;
                margin-bottom: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.08);
                border-left: 6px solid #667eea;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                scroll-margin-top: 100px; /* IMPORTANTE: Para que la ancla no quede bajo el header fijo */
            }
            .section-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 25px rgba(0,0,0,0.15);
            }
            .section-title {
                font-size: 2.5em;
                font-weight: 700;
                color: #4a5568;
                margin-bottom: 25px;
                text-align: center;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 15px;
            }
            .section-text {
                font-size: 1.1em;
                line-height: 1.7;
                color: #555;
                margin-bottom: 20px;
                text-align: justify;
            }
            .formula-box {
                background-color: #e0f2f7; /* Light blue for formulas */
                border-left: 4px solid #039be5;
                padding: 15px;
                margin: 20px 0;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 1.1em;
                color: #212121;
                border-radius: 5px;
                overflow-x: auto; /* For long formulas */
            }
            .exercise-box {
                background-color: #fffde7; /* Light yellow for exercises */
                border: 2px dashed #ffc107;
                padding: 25px;
                margin-top: 30px;
                border-radius: 10px;
            }
            .step-box {
                background-color: #e8f5e8; /* Light green for steps */
                border-left: 4px solid #28a745;
                padding: 15px;
                margin-top: 15px;
                border-radius: 5px;
            }
            .step-box strong {
                color: #1e7e34;
            }
            .section-image {
                border-radius: 8px;
                max-width: 100%;
                height: auto;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }
            .footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 20px;
                width: 100%;
                position: relative;
                bottom: 0;
                left: 0;
                box-shadow: 0 -2px 8px rgba(0,0,0,0.2);
            }
            .gradient-text {
                background: linear-gradient(90deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            /* Estilo para los enlaces de ancla en la barra de navegación */
            .nav-button {
                text-decoration: none !important;
                color: white !important;
                font-weight: 600;
                padding: 8px 15px;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .nav-button:hover {
                background-color: rgba(255, 255, 255, 0.2) !important;
                transform: translateY(-2px);
            }
        </style>
    ''')