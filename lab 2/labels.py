from kivy.uix.label     import Label;
from kivy.lang          import Builder

Builder.load_file('BackLabel.kv')

class BackLabel(Label):
    def __init__(self, **kwargs):
        super(BackLabel, self).__init__(**kwargs);


class LineLabel(Label):
    def __init__(self, **kwargs):
        super(LineLabel, self).__init__(**kwargs);