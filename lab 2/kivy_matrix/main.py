import kivy
kivy.require('1.11.1')

from kivy.app               import App
from KivyMatrix             import KivyEnterMatrix, InverselyAgreedMatrix;
from kivy.uix.label         import Label;
from kivy.uix.gridlayout    import GridLayout;
from kivy.uix.button        import Button;

my_matrix = InverselyAgreedMatrix();

def plus(hello = 0):
    m_s = my_matrix.get_mat_size()[0];
    my_matrix.set_mat_size([m_s + 1 , m_s + 1]);

def minus(hello = 0):
    m_s = my_matrix.get_mat_size()[0];
    my_matrix.set_mat_size([m_s - 1 , m_s - 1]);

def get_matrix(hello = 0):
   print(my_matrix.get_matrix());

def set_matrix(hello = 0):
    my_matrix.set_matrix([[1, 2, 3], [3, 4, 5], [1, 2, 3]]);



gl = GridLayout(cols = 1);
gl2 = GridLayout(cols = 2);

but1 = Button(text = '+', on_press = plus);
but2 = Button(text = '-', on_press = minus)
but3 = Button(text = 'get matrix' , on_press = get_matrix);
but4 = Button(text = 'set matrix', on_press = set_matrix);

gl.add_widget(my_matrix);
gl.add_widget(gl2);
gl.add_widget(but3);
gl.add_widget(but4);

gl2.add_widget(but1);
gl2.add_widget(but2);



class MyApp(App):

    def build(self):
        return gl;


if __name__ == '__main__':
    MyApp().run()