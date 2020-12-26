from hello import norm_multidirectional;
from hello import build_diagramm;
from hello import norm_unidirectional;
from hello import compute_area;
import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv("temp.csv"); # читаем данные из предварительно созданного cvs файла
print('полученные данные');
print(df); # для наглядности представим как загрузились данные

work_data = df.loc[: ,'x1':'x6']; # надо выкинуть первый сторбик - в таком формате
# ждет данные первая функция

# нормируем однонаправленные показатели (формула 2)
work_data = norm_unidirectional(work_data);

# посмотрим, что получилось
print('нормированные данные');
print(work_data);


fig = plt.figure();
ax = fig.add_subplot(111, polar = True);

# строим диаграмму
# так как данные по минской области располагаются в пятой строке то передаем именно эту строку
build_diagramm(work_data.iloc[5, :].tolist(), work_data.keys().tolist(), ax);

plt.show();

# вычисляем прощадь модего неправильного шестиугольника
my_area = compute_area(work_data.iloc[5, :].tolist());
print('площадь моего шестиугольника');
print(my_area);

# вычисляем площадь большого шестиугольника
whole_area = 0.4330127018922193*6;
print('суммарная полщадь');
print(whole_area);

print('ПОЛУЧЕННЫЙ ПОКАЗАТЕЛЬ');
print(my_area/whole_area);