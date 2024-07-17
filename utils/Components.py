from django import forms
from django.utils.safestring import mark_safe


class MultiInputForm(forms.MultiWidget):
    def __init__(self, **kwargs):
        self.cant = kwargs.get('cant', 2)
        self.configGlobal = kwargs.get('optionGlobal', {})
        if 'style' in self.configGlobal:
            self.styleGlobal = self.configGlobal.pop('style') + '; margin-bottom: 20px;'
        else:
            self.styleGlobal = 'margin-bottom: 15px;'

        self.elementConfig = kwargs.get('elementConfig', [{}])
        widgets = [
            forms.TextInput(attrs=self.get_options(i, self.elementConfig))
            for i in range(1, self.cant + 1)
        ]
        super().__init__(widgets, self.configGlobal)

    def get_options(self, index, option):
        option_return = {'style': self.styleGlobal}
        for element in option:
            if element.get('element') == index:
                if 'style' in element.get('options'):
                    element.get("options")["style"] += "; " + self.styleGlobal
                option_return.update(element.get('options'))
        return option_return

    def decompress(self, value):
        if value:
            decompressed_values = value.split(',')
            return decompressed_values
        return [None] * self.cant
