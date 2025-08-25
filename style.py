import os
from PyQt6.QtGui import QColor

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
class Jcolor:
    PRIMARY = QColor(THEME_COLORS['@primary'])  # '#4ea1ff;',
    SECONDARY = QColor(THEME_COLORS['@secondary']) #555555
    SUCCESS = QColor(THEME_COLORS['@success']) #77b300
    INFO = QColor(THEME_COLORS['@info']) #9933cc
    WARNING = QColor(THEME_COLORS['@warning']) #ff8800
    DANGER = QColor(THEME_COLORS['@danger']) #cc0000
    FGPRIMARY = QColor(THEME_COLORS['@fgprimary']) #ffffff
    FGSECONDARY = QColor(THEME_COLORS['@fgsecondary']) #ffffff
    FGSUCCESS = QColor(THEME_COLORS['@fgsuccess']) #ffffff
    FGINFO = QColor(THEME_COLORS['@fginfo']) #ffffff
    FGWARNING = QColor(THEME_COLORS['@fgwarning']) #000000
    FGDANGER = QColor(THEME_COLORS['@fgdanger']) #ffffff
    


class Color:
    PRIMARYLIGHT = THEME_COLORS['@primarylight'] #85b9ff
    PRIMARY = THEME_COLORS['@primary']  # '#4ea1ff;',
    PRIMARYDARK = THEME_COLORS['@primarydark'] #2675ff
    SECONDARYLIGHT = THEME_COLORS['@secondarylight'] #767676
    SECONDARY = THEME_COLORS['@secondary'] #555555
    SECONDARYDARK = THEME_COLORS['@secondarydark'] #2e2e2e
    SUCCESSLIGHT = THEME_COLORS['@successlight'] #a4d155
    SUCCESS = THEME_COLORS['@success'] #77b300
    SUCCESSDARK = THEME_COLORS['@successdark'] #4f6d00
    INFOLIGHT = THEME_COLORS['@infolight'] #c08ff3
    INFO = THEME_COLORS['@info'] #9933cc
    INFODARK = THEME_COLORS['@infodark'] #661d99
    WARNINGLIGHT = THEME_COLORS['@warninglight'] #ffae33
    WARNING = THEME_COLORS['@warning'] #ff8800
    WARNINGDARK = THEME_COLORS['@warningdark'] #cc6600
    DANGERLIGHT = THEME_COLORS['@dangerlight'] #e16d6d
    DANGER = THEME_COLORS['@danger'] #cc0000
    DANGERDARK = THEME_COLORS['@dangerdark'] #8b0000
    LIGHT = THEME_COLORS['@light'] #ADAFAE
    DARK = THEME_COLORS['@dark'] #222222
    BG = THEME_COLORS['@bg'] #060606
    FG = THEME_COLORS['@fg'] #ffffff
    SELECTBG = THEME_COLORS['@selectbg'] #454545
    SELECTFG = THEME_COLORS['@selectfg'] #ffffff
    BORDER = THEME_COLORS['@border'] #060606
    INPUTFG = THEME_COLORS['@inputfg'] #ffffff
    INPUTBG = THEME_COLORS['@inputbg'] #191919
    PRIMARYDIS = THEME_COLORS['@primarydis'] #7aaeff
    SECONDARYDIS = THEME_COLORS['@secondarydis'] #6e6e6e
    SUCCESSDIS = THEME_COLORS['@successdis'] #90c344
    INFODIS = THEME_COLORS['@infodis'] #b07cd9
    WARNINGDIS = THEME_COLORS['@warningdis'] #e69933
    DANGERDIS = THEME_COLORS['@dangerdis'] #d38080
    LIGHTDIS = THEME_COLORS['@lightdis'] #c0c2c1
    DARKDIS = THEME_COLORS['@darkdis'] #3a3a3a
    FGPRIMARY = THEME_COLORS['@fgprimary'] #ffffff
    FGSECONDARY = THEME_COLORS['@fgsecondary'] #ffffff
    FGSUCCESS = THEME_COLORS['@fgsuccess'] #ffffff
    FGINFO = THEME_COLORS['@fginfo'] #ffffff
    FGWARNING = THEME_COLORS['@fgwarning'] #000000
    FGDANGER = THEME_COLORS['@fgdanger'] #ffffff
    FGLIGHT = THEME_COLORS['@fglight'] #000000
    FGDARK = THEME_COLORS['@fgdark'] #ffffff
    FGPRIMARYDIS = THEME_COLORS['@fgprimarydis'] #e0e0e0
    FGSECONDARYDIS = THEME_COLORS['@fgsecondarydis'] #cccccc
    FGSUCCESSDIS = THEME_COLORS['@fgsuccessdis'] #e0e0e0
    FGINFODIS = THEME_COLORS['@fginfodis'] #e0e0e0
    FGWARNINGDIS = THEME_COLORS['@fgwarningdis'] #333333
    FGDANGERDIS = THEME_COLORS['@fgdangerdis'] #e0e0e0
    FGLIGHTDIS = THEME_COLORS['@fglightdis'] #333333
    FGDARKDIS = THEME_COLORS['@fgdarkdis'] #cccccc


def load_style():
    '''Carrega todos os arquivos QSS, os combina e substitui os placeholders de cor.'''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Lista de arquivos QSS para carregar 
    qss_files = ['./qss/cyborg.qss', 
                 './qss/frame.qss',
                 './qss/label.qss',
                 './qss/lineEdit.qss', 
                 './qss/pushButton.qss', 
                 './qss/comboBoxFill.qss', 
                 './qss/comboBox.qss', 
                 './qss/radioButton.qss', 
                 './qss/checkBox.qss', 
                 './qss/textEdit.qss',
                 './qss/tableWidget.qss',
                 './qss/tableView.qss'
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

        
if __name__ == '__main__':
    print('\n'*20)
    print(Jstyle.BT_PRIMARY)