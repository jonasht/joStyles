from style import Color
import re

class Jstyle:
    
 
    # QPushButton {
        # color: @fg;
        # background-color: @secondary;
        # border: 1.5px solid @secondary;
        # border-radius: 8px;
        # font-size: 16px;
        # padding: 7px 22px;
        # font-weight: 500;
    # }
    # QPushButton:hover {
        # background-color: @secondarylight;
    # }
    # QPushButton:pressed {
        # background-color: @secondarydark;
    # }

    BT_PRIMARY = f'''
    QPushButton {{
        background-color: {Color.PRIMARY};
        border: 1.5px solid {Color.PRIMARY};
    }}
    QPushButton:hover {{
        background-color: {Color.PRIMARYLIGHT};
    }}
    QPushButton:pressed {{
        background-color: {Color.PRIMARYDARK};
    }}
    QPushButton:disabled {{
    background-color: {Color.PRIMARYDIS};
    color: {Color.FGPRIMARYDIS};
    border-color: {Color.PRIMARYDIS};
}}
    '''

    BT_SECONDARY = f'''QPushButton {{
                        background-color: {Color.SECONDARY};
                        border: 1.5px solid {Color.SECONDARY};
                    }}
                    QPushButton:hover {{
                        background-color: {Color.SECONDARYLIGHT};
                    }}
                    QPushButton:pressed {{
                        background-color: {Color.SECONDARYDARK};
                    }}
'''
                    # QPushButton#secondary:disabled {{
    # background-color: #6e6e6e;
    # color: #cccccc;
    # border-color: #6e6e6e;
# }}
    BT_SUCCESS = f'''QPushButton {{
                    background-color: {Color.SUCCESS};
                    border: 1.5px solid {Color.SUCCESS};
                    }}
                    QPushButton:hover {{
                    background-color: {Color.SUCCESSLIGHT};
                    }}
                    QPushButton:pressed {{
                    background-color: {Color.SUCCESSDARK};
                    }}
                    '''
                    # QPushButton#success:disabled {{
    # background-color: #90c344;
    # color: #e0e0e0;
    # border-color: #90c344;
# }}

    BT_INFO = f'''QPushButton {{
                        background-color: {Color.INFO};
                        border: 1.5px solid {Color.INFO};
                    }}
                    QPushButton:hover {{
                        background-color: {Color.INFOLIGHT};
                    }}
                    QPushButton:pressed {{
                        background-color: {Color.INFODARK};
                    }}
                    '''
                    # QPushButton#info:disabled {{
    # background-color: #b07cd9;
    # color: #e0e0e0;
    # border-color: #b07cd9;
# }}

    BT_WARNING = f'''QPushButton {{
                    background-color: {Color.WARNING};
                    border: 1.5px solid {Color.WARNING};
                }}
                QPushButton:hover {{
                    background-color: {Color.WARNINGLIGHT};
                }}
                QPushButton:pressed {{
                    background-color: {Color.WARNINGDARK};
                }}'''

    BT_DANGER = f'''QPushButton {{
                    background-color: {Color.DANGER};
                    border: 1.5px solid {Color.DANGER};
                }}
                QPushButton:hover {{
                    background-color: {Color.DANGERLIGHT};
                }}
                QPushButton:pressed {{
                    background-color: {Color.DANGERDARK};
                }}'''

    BT_LINK = f'''QPushButton#link {{
                    background: transparent;
                    border: none;
                    color: {Color.PRIMARY};
                    font-size: 15px;
                    text-align: left;
                    padding: 0;
                    font-weight: 500;
                    text-decoration: none;
                }}
                QPushButton#link:hover {{
                    color: {Color.INFO};
                    text-decoration: underline;
                }}
                QPushButton#link:pressed {{
                    color: {Color.WARNING};
                }}'''
                
# /* QPushButton disabled */
# QPushButton#warning:disabled {
    # background-color: #e69933;
    # color: #333333;
    # border-color: #e69933;
# }
# QPushButton#danger:disabled {
    # background-color: #d38080;
    # color: #e0e0e0;
    # border-color: #d38080;
# }
# 
# 
# /* button outline ---------------------------*/
    BT_PRIMARY_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            color: {Color.PRIMARY};
            border: 1.5px solid {Color.PRIMARY};
        }}
        QPushButton:hover {{
            color: {Color.FGPRIMARY};
            background-color: {Color.PRIMARY};
        }}
        QPushButton:pressed {{
            color: {Color.FGPRIMARY};
            background-color: {Color.PRIMARYDARK};
        }}
        '''
# 
    BT_SECONDARY_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            border: 1.5px solid {Color.SECONDARY};
            color: {Color.SECONDARY};
        }}
        QPushButton:hover {{
            color: {Color.FGSECONDARY};
            background-color: {Color.SECONDARY};
        
        }}
        QPushButton:pressed {{
            color: {Color.FGSECONDARY};
            background-color: {Color.SECONDARYDARK};
        }}
        '''
# 
    BT_SUCCESS_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            border: 1.5px solid {Color.SUCCESS};
            color: {Color.SUCCESS};
        }}
        QPushButton:hover {{
            color: {Color.FGSUCCESS};
            background-color: {Color.SUCCESS};
        }}
        QPushButton:pressed {{
            color: {Color.FGSUCCESS};
            background-color: {Color.SUCCESSDARK};
        }}
#       '''
    BT_INFO_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            border: 1.5px solid {Color.INFO};
            color: {Color.INFO};
        }}
        QPushButton:hover {{
            color: {Color.FGINFO};
            background-color: {Color.INFO};
        }}
        QPushButton:pressed {{
            color: {Color.FGINFO};
            background-color: {Color.INFODARK};
        }}
        '''
        
    BT_WARNING_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            border: 1.5px solid {Color.WARNING};
            color: {Color.WARNING};
        }}
        QPushButton:hover {{
            color: {Color.FGWARNING};
            background-color: {Color.WARNING};
        }}
        QPushButton:pressed {{
            color: {Color.FGWARNING};
            background-color: {Color.WARNINGDARK};
        }}
        '''
    BT_DANGER_OUTLINE = f'''QPushButton {{
            background-color: transparent;
            border: 1.5px solid {Color.DANGER};
            color: {Color.DANGER};
        }}
        QPushButton:hover {{
            color: {Color.FGDANGER};
            background-color: {Color.DANGER};
        }}
        QPushButton:pressed {{
            color: {Color.FGDANGER};
            background-color: {Color.DANGER};
        }}
        '''
# /* outline disabled 0-----0-0-0-0-0-*/
# QPushButton#primary-outline:disabled {
    # color: @primarydark;
    # border: 1.5px solid @primarydark;
# }
# 
# QPushButton#secondary-outline:disabled {
    # color: @secondarylight;
    # border: 1.5px solid @secondarydark;
# }
# 
# QPushButton#success-outline:disabled {
    # color: @successdark;
    # border: 1.5px solid @successdark;
# }
# 
# QPushButton#info-outline:disabled {
    # color: @infodark;
    # border: 1.5px solid @infodark;
# }
# 
# QPushButton#warning-outline:disabled {
    # color: @warningdark;
    # border: 1.5px solid @warningdark;
# }
# 
# QPushButton#danger-outline:disabled {
    # color: @dangerdark;
    # border: 1.5px solid @dangerdark;
# }
# /* QpushButton link -------------------------- */
# QPushButton#primary-link {
    # background: transparent;
    # border: none;
    # color: @primary;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#primary-link:hover {
    # text-decoration: underline;
    # color: @primarylight;
# }
# QPushButton#primary-link:pressed {
    # color: @primarydark;
#  
# }
# QPushButton#secondary-link {
    # background: transparent;
    # border: none;
    # color: @secondary;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#secondary-link:hover {
    # text-decoration: underline;
    # color: @secondarylight;
# }
# QPushButton#secondary-link:pressed {
    # color: @secondarydark;
# }
# QPushButton#success-link {
    # background: transparent;
    # border: none;
    # color: @success;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#success-link:hover {
    # text-decoration: underline;
    # color: @successlight;
# }
# QPushButton#success-link:pressed {
    # color: @successdark;
# }
# QPushButton#info-link {
    # background: transparent;
    # border: none;
    # color: @info;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#info-link:hover {
    # text-decoration: underline;
    # color: @infolight;
# }
# QPushButton#info-link:pressed {
    # color: @infodark;
# }
# QPushButton#warning-link {
    # background: transparent;
    # border: none;
    # color: @warning;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#warning-link:hover {
    # text-decoration: underline;
    # color: @warninglight;
# }
# QPushButton#warning-link:pressed {
    # color: @warningdark;
# }
# 
# QPushButton#danger-link {
    # background: transparent;
    # border: none;
    # color: @danger;
    # font-size: 15px;
    # text-align: left;
    # padding: 0;
    # font-weight: 500;
    # text-decoration: none;
# }
# QPushButton#danger-link:hover {
    # text-decoration: underline;
    # color: @dangerlight;
# }
# QPushButton#danger-link:pressed {
    # color: @dangerdark;
# }
# 
# 
# QPushButton#primary-link:disabled {
    # color: @primarydark;
# }
# QPushButton#secondary-link:disabled {
    # color: @secondarydark;
# }
# QPushButton#success-link:disabled {
    # color: @successdark;
# }
# QPushButton#info-link:disabled {
    # color: @infodark;
# }
# QPushButton#warning-link:disabled {
    # color: @warningdark;
# }
# QPushButton#danger-link:disabled {
    # color: @dangerdark;
# } 
    def read_qss(self):
        with open('./style.qss') as file:
            return file.read()

    def get_primary(self):
        padrao = r'QpushButton#primary(?!-outline)(:[\w-]+)?\s*{[^}]*}'
        var_qss = self.read_qss()

        matches = re.finditer(padrao, var_qss, re.DOTALL)
        return [m.group(0) for m in matches]

if __name__ == '__main__':
    resultado = Jstyle().get_primary()

    print(resultado)