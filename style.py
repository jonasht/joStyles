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
 
# --- Border ---
PRIMARY_BORDER = 'primary-border' 
SECONDARY_BORDER = 'secondary-border' 
SUCCESS_BORDER = 'success-border' 
INFO_BORDER = 'info-border' 
WARNING_BORDER = 'warning-border' 
DANGER_BORDER = 'danger-border' 
# outline
PRIMARY_OUTLINE = 'primary-outline'
SECONDARY_OUTLINE = 'secondary-outline'
SUCCESS_OUTLINE = 'success-outline'
INFO_OUTLINE = 'info-outline'
WARNING_OUTLINE = 'warning-outline'
DANGER_OUTLINE = 'danger-outline'

# --- link ---
PRIMARY_LINK = 'primary-link'
SECONDARY_LINK = 'secondary-link'
SUCCESS_LINK = 'success-link'
INFO_LINK = 'info-link'
WARNING_LINK = 'warning-link'
DANGER_LINK = 'danger-link'

# --- fill ---
PRIMARY_FILL = 'primary-fill'
SECONDARY_FILL = 'secondary-fill'
SUCCESS_FILL = 'success-fill'
INFO_FILL = 'info-fill'
WARNING_FILL = 'warning-fill'
DANGER_FILL = 'danger-fill'



    # cor old de primary: "@primary": "#2a9fd6", bak
# --- Dicionário de Cores ---
THEME_COLORS = {
        '@primarylight':'#85b9ff',
        '@primary':'#4ea1ff',
        '@primarydark':'#2675ff',
        '@secondarylight':'#767676',
        '@secondary':'#555555',
        '@secondarydark':'#2e2e2e',
        '@successlight':'#a4d155',
        '@success':'#77b300',
        '@successdark':'#4f6d00',
        '@infolight':'#c08ff3',
        '@info':'#9933cc',
        '@infodark':'#661d99',
        '@warninglight':'#ffae33',
        '@warning':'#ff8800',
        '@warningdark':'#cc6600',
        '@dangerlight':'#e16d6d',
        '@danger':'#cc0000',
        '@dangerdark':'#8b0000',
        '@light':'#ADAFAE',
        '@dark':'#222222',
        '@bg':'#060606',
        '@fg':'#ffffff',
        '@selectbg':'#454545',
        '@selectfg':'#ffffff',
        '@border':'#060606',
        '@inputfg':'#ffffff',
        '@inputbg':'#191919',
        '@primarydis':'#7aaeff',
        '@secondarydis':'#6e6e6e',
        '@successdis':'#90c344',
        '@infodis':'#b07cd9',
        '@warningdis':'#e69933',
        '@dangerdis':'#d38080',
        '@lightdis':'#c0c2c1',
        '@darkdis':'#3a3a3a',
        '@fgprimary':'#ffffff',
        '@fgsecondary':'#ffffff',
        '@fgsuccess':'#ffffff',
        '@fginfo':'#ffffff',
        '@fgwarning':'#000000',
        '@fgdanger':'#ffffff',
        '@fglight':'#000000',
        '@fgdark':'#ffffff',
        '@fgprimarydis':'#e0e0e0',
        '@fgsecondarydis':'#cccccc',
        '@fgsuccessdis':'#e0e0e0',
        '@fginfodis':'#e0e0e0',
        '@fgwarningdis':'#333333',
        '@fgdangerdis':'#e0e0e0',
        '@fglightdis':'#333333',
        '@fgdarkdis':'#cccccc',
}
        
'''
    | Categoria     | Foreground normal | Foreground disabled |
    | _------------ | ----------------- | ------------------- |
    | **primary**   | `#ffffff`         | `#e0e0e0`           |
    | **secondary** | `#ffffff`         | `#cccccc`           |
    | **success**   | `#ffffff`         | `#e0e0e0`           |
    | **info**      | `#ffffff`         | `#e0e0e0`           |
    | **warning**   | `#000000`         | `#333333`           |
    | **danger**    | `#ffffff`         | `#e0e0e0`           |
    | **light**     | `#000000`         | `#333333`           |
    | **dark**      | `#ffffff`         | `#cccccc`           |
'''


def load_style():
    '''Carrega todos os arquivos QSS, os combina e substitui os placeholders de cor.'''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Lista de arquivos QSS para carregar 
    qss_files = ['cyborg.qss', 
                 'frame.qss',
                 'label.qss',
                 'lineEdit.qss', 
                 'pushButton.qss', 
                 'comboBoxFill.qss', 
                 'comboBox.qss', 
                 'radioButton.qss', 
                 'checkBox.qss', 
                 'textEdit.qss'
                 ]

                 
    
    stylesheet = ''
    for qss_file in qss_files:
        qss_path = os.path.join(script_dir, qss_file)
        try:
            with open(qss_path, 'r', encoding='utf-8') as file:
                stylesheet += file.read() + "\n"
        except FileNotFoundError:
            print(f"Aviso: O arquivo de estilo '{qss_path}' não foi encontrado.")

    # Substitui cada placeholder pelo seu valor correspondente
    for var, color in THEME_COLORS.items():
        stylesheet = stylesheet.replace(var+';', color+';')
        
    # escrever stylesheet
    with open('style.qss', 'w') as file:
        file.write(stylesheet)

def get_style():
    load_style()
    with open('style.qss', 'r', encoding='utf-8') as file:
        return file.read()

def load_styleTest():
    '''Carrega todos os arquivos QSS, os combina e substitui os placeholders de cor.'''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Lista de arquivos QSS para carregar em ordem
    qss_files = ['cyborg.qss', 
                 'label.qss',
                 'lineEdit.qss', 
                 'pushButton.qss', 
                 'frame.qss',
                 'comboBoxFill.qss', 
                 'comboBox.qss', 
                 'radioButton.qss', 
                 'checkBox.qss', 
                 ]

    stylesheet = ''
    for qss_file in qss_files:
        qss_path = os.path.join(script_dir, qss_file)
        try:
            with open(qss_path, 'r', encoding='utf-8') as file:
                stylesheet += file.read() + "\n"
        except FileNotFoundError:
            print(f"Aviso: O arquivo de estilo '{qss_path}' não foi encontrado.")

    # Substitui cada placeholder pelo seu valor correspondente
    for var, color in THEME_COLORS.items():
        stylesheet = stylesheet.replace(var+';', color+';')
        
    with open('styleSheet.css', 'w') as file:
        file.write(stylesheet)
        
if __name__ == '__main__':
    load_styleTest()
    load_style()
