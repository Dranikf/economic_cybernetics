import kivy
import json
kivy.require('1.11.1')

from kivy.app           import App
from BrunchClass        import BrunchClass;


data = [];
with open('tree.json') as json_file:
    data = json.load(json_file)


print(data);

main_brunch = BrunchClass(data);


class MyApp(App):

    def build(self):
        return main_brunch;


if __name__ == '__main__':
    MyApp().run()