import os

# --- Constantes para Nomes de Objetos ---
PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
INFO = 'info'
WARNING = 'warning'
DANGER = 'danger'
LINK = 'link'

# inverse
PRIMARY_INVERSE = 'primary-inverse' 
SECONDARY_INVERSE = 'secondary-inverse' 
SUCCESS_INVERSE = 'success-inverse' 
INFO_INVERSE = 'info-inverse' 
WARNING_INVERSE = 'warning-inverse' 
DANGER_INVERSE = 'danger-inverse' 

PRIMARY_BORDER = 'primary-border' 
SECONDARY_BORDER = 'secondary-border' 
SUCCESS_BORDER = 'success-border' 
INFO_BORDER = 'info-border' 
WARNING_BORDER = 'warning-border' 
DANGER_BORDER = 'danger-border' 

# --- Dicionário de Cores ---
THEME_COLORS = {
    "@primary": "#2a9fd6",
    "@secondary": "#555555",
    "@success": "#77b300",
    "@info": "#9933cc",
    "@warning": "#ff8800",
    "@danger": "#cc0000",
    "@light": "#ADAFAE",
    "@dark": "#222222",
    "@bg": "#060606",
    "@fg": "#ffffff",
    "@selectbg": "#454545",
    "@selectfg": "#ffffff",
    "@border": "#060606",
    "@inputfg": "#ffffff",
    "@inputbg": "#191919"
}

def load_style():
    """Carrega o arquivo QSS e substitui os placeholders de cor."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(script_dir, 'cyborg.qss')
    
    with open(qss_path, 'r', encoding='utf-8') as file:
        stylesheet = file.read()

    # Substitui cada placeholder pelo seu valor correspondente
    for var, color in THEME_COLORS.items():
        stylesheet = stylesheet.replace(var, color)
        
    return stylesheet

if __name__ == '__main__':
    print(load_style())