from kivy.uix.boxlayout         import BoxLayout;
from kivy.uix.button            import Button;
from labels                     import BackLabel, LineLabel;
import numpy                    as np;

class BrunchClass(BoxLayout):

    def __init__(self, brunch, **kwargs):
        self.orientation = 'vertical';
        self.padding = 3;
        super(BrunchClass, self).__init__(**kwargs);

        bl = BackLabel(size_hint_y = 0.3, text =  brunch['name']);
        self.add_widget(bl);
        
        lines = BoxLayout(size_hint_y = 0.1);

        n = len(brunch['brunches']);
        if n <= 1:
            return;

        next_level = BoxLayout(orientation = 'horizontal');
        p = self.compute_prioritets(brunch['matrix']);
        l_m = self.compute_lambd(brunch['matrix'], p);
        IS = (l_m - n)  / (n - 1);


        bl.text = bl.text + '\n lambda ' + str(l_m)[0:5] + ', index ' + str(IS)[0:5];
        

        for i in range(len(brunch['brunches'])):

            lines.add_widget(LineLabel(text = str(p[i]*100)[0:6] ));
            next_level.add_widget(BrunchClass(brunch['brunches'][i]));

        self.add_widget(lines);
        self.add_widget(next_level);


    def compute_prioritets(self, matrix):

        result = [];

        for line in matrix:
            result.append(sum(line));

        summ = sum(result);

        for i in range(len(result)):
            result[i] = result[i]/summ;

        return result;

    
    def compute_lambd(self, matr, p):
        temp = np.matrix(matr);
        temp = temp.dot(np.matrix(p).transpose());

        temp = temp.tolist();

        for i in range(len(temp)):
            temp[i] = temp[i][0]/p[i];

        return sum(temp) / float(len(temp));