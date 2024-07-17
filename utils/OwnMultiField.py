from django import forms


class CustomMultiWidget(forms.MultiWidget):
    def __init__(self, widgets, *args, **kwargs):
        super().__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return value.split(',')
        return [None] * len(self.widgets)


class OwnMultiField(forms.MultiValueField):
    def __init__(self, widget_classes, *args, **kwargs):
        props_own = kwargs.pop('propsOwn', {})
        fields = [forms.CharField() for _ in range(len(widget_classes))]
        self.widgets = [widget_cls(**props_own) for widget_cls in widget_classes]
        super().__init__(fields, *args, **kwargs)
        self.widget = CustomMultiWidget(widgets=self.widgets)

    def compress(self, data_list):
        return ','.join(data_list) if data_list else ''
