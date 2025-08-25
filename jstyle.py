from style import Color
import re

class Jstyle:
    
 
        
    def __init__(self) -> None:...
    
    def read_qss(self):
        with open('./style.qss', 'r', encoding='utf-8') as file:
            return file.read()
    
    def get_styleByType(self, widget_name, styleType):
        
        padrao = str(widget_name)+'#'+styleType+r'(:[\w-]+)?\s*{[^}]*}'

        var_qss = self.read_qss()
        matches = re.finditer(padrao, var_qss, re.DOTALL)
        blocos = [m.group(0) for m in matches]

        blocos = "\n\n".join(blocos)
        blocos.replace(f'{widget_name}#{styleType}', widget_name)
        blocos = re.sub('#'+styleType, "", blocos)
        return blocos
        

    def get_primary(self, widget):
        widget_name = widget
        to_return = self.get_styleByType(widget_name, 'primary')
        return to_return
    
    def get_secondary(self, widget):
        widget_name = widget
        to_return = self.get_styleByType(widget_name, 'secondary')
        return to_return
    def get_success(self, widget):
        widget_name = widget
        
        to_return = self.get_styleByType(widget_name, 'success')
        return to_return
    def get_info(self, widget):
        widget_name = widget
        
        to_return = self.get_styleByType(widget_name, 'info')
        return to_return
    def get_warning(self, widget):
        widget_name = widget
        
        to_return = self.get_styleByType(widget_name, 'warning')
        return to_return
    
    def get_danger(self, widget):
        widget_name = widget
        
        to_return = self.get_styleByType(widget_name, 'danger')
        return to_return



class JButton(Jstyle):
    def __init__(self,) -> None:
        self.widget_name = 'QPushButton'
        
        self.primary = self.get_styleByType(self.widget_name, 'primary')
        self.secondary = self.get_styleByType(self.widget_name, 'secondary')
        self.success = self.get_styleByType(self.widget_name, 'success')
        self.info = self.get_styleByType(self.widget_name, 'info')
        self.warning = self.get_styleByType(self.widget_name, 'warning')
        self.danger = self.get_styleByType(self.widget_name, 'danger')
        self.link = self.get_styleByType(self.widget_name, 'link')
        
        # bt outline
        
        self.primaryOutline = self.get_styleByType(self.widget_name, 'primary-outline')
        self.secondaryOutline = self.get_styleByType(self.widget_name, 'secondary-outline')
        self.successOutline = self.get_styleByType(self.widget_name, 'success-outline')
        self.infoOutline = self.get_styleByType(self.widget_name, 'info-outline')
        self.warningOutline = self.get_styleByType(self.widget_name, 'warning-outline')
        self.dangerOutline = self.get_styleByType(self.widget_name, 'danger-outline')
        

class JLabel(Jstyle):
    def __init__(self) -> None:
        super().__init__()
        widget_name = 'QLabel'

        self.primary = self.get_styleByType(widget_name, 'primary') 
        self.secondary = self.get_styleByType(widget_name, 'secondary') 
        self.success = self.get_styleByType(widget_name, 'success') 
        self.info = self.get_styleByType(widget_name, 'info') 
        self.warning = self.get_styleByType(widget_name, 'warning') 
        self.danger = self.get_styleByType(widget_name, 'danger') 
        
        
        
if __name__ == '__main__':
    
    j = Jstyle()
    bt = JButton()


    widget = 'QPushButton'
    print('bottoes', bt.successOutline)