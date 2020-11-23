from kivy.uix.gridlayout    import GridLayout;
from kivy.uix.textinput     import TextInput;
from kivy.properties        import BooleanProperty;

class KivyEnterMatrix(GridLayout):
    '''class for ui object for editing matrixex'''
    def __init__(self, **kwargs):

        mat_size = kwargs.pop('mat_size' , None);
        if mat_size == None:
            mat_size = [3 , 3];


        super(KivyEnterMatrix, self).__init__(**kwargs);

        self._edits_settings = {'text' : str(0), 'multiline' : False}

        self.set_mat_size(mat_size);


    def _init_matrix(self):
        '''build matrix with new parameters, all old data will deleted'''
        self.clear_widgets();
        self._inputs = [];

        for i in range(self._mat_size[0]):
            temp = [];
            for j in range(self._mat_size[1]):
                inp = TextInput(**self._edits_settings);
                temp.append(inp);
                self.add_widget(inp);

            self._inputs.append(temp);

    
    def set_mat_size(self, mat_size):

        if mat_size[0] < 1 or mat_size[1] < 1:
            print('mar size shold be more then 0');
            return;

        self._mat_size = mat_size;
        self.cols = self._mat_size[1];
        self._init_matrix();

    
    def get_mat_size(self):
        return self._mat_size;
    
    
    def get_matrix(self):

        print(self.ids.keys());
        result = [];

        for i in range(self._mat_size[0]):
            temp = [];
            for j in range(self._mat_size[1]):
                temp.append(int(self._inputs[i][j].text));
            result.append(temp);

        return result;
        

class InverselyAgreedMatrix(KivyEnterMatrix):


    class fInput(TextInput):
        def on_focus(self, instance, value):
            id_ = instance.id;
            ind = id_.find('_');

            i = int(id_[0:ind]);
            j = int(id_[ind+1:len(id_)]);
            
            mat = instance.parent;

            if i == j:
                mat._inputs[i][j].text = str(1.0);
            else:
                mat._inputs[j][i].text = str(1/float(instance.text));


    def __init__(self, **kwargs):
        super(InverselyAgreedMatrix, self).__init__(**kwargs);
        self._edits_settings = {'text' : str(1.0) , 'multiline' : False}
        self._init_matrix();


    def _init_matrix(self):
        '''build matrix with new parameters, all old data will deleted'''
        self.clear_widgets();
        self._inputs = [];

        for i in range(self._mat_size[0]):
            temp = [];

            for j in range(self._mat_size[1]):
                self._edits_settings['id'] = str(i) + '_' + str(j);
                inp = self.fInput(**self._edits_settings);
                temp.append(inp);
                self.add_widget(inp);

            self._inputs.append(temp);


    def set_matrix(self, matrix):
        self._mat_size[0] = len(matrix);
        self._mat_size[1] = len(matrix[0]);

        self.clear_widgets();
        self._inputs = [];

        my_settings = self._edits_settings;

        for i in range(self._mat_size[0]):
            temp = [];

            for j in range(self._mat_size[1]):
                
                my_settings['id'] = str(i) + '_' + str(j);
                my_settings['text'] = str(matrix[i][j])
                inp = self.fInput(**my_settings);
                temp.append(inp);
                self.add_widget(inp);

            self._inputs.append(temp);