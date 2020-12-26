import matplotlib.pyplot as plt
import numpy as np
from math import sin;
import pandas as pd;
import copy;


def norm_unidirectional(data):
    '''функция для нормирования однонаправленных показателей
    на вход ждет pandas data frame'''
    keys = data.keys();
    result = copy.copy(data);
    
    # перебираем показатели
    for k in keys:
        colunm = data[k];
        m = max(colunm);
        # перебираем показатели по областям и нормируем
        for i in range(0 , len(data[k])):
            result[k][i] = colunm[i]/m;

    # возвращаем результат
    return result;



def norm_multidirectional(x):
    '''функция для снормирования  разнонаправленных переменных'''

    width = len(x[1]);
    height = len(x);

    a = [];
    for i in range(0, height):
        a.append([]);
        for j in range(0, width):
            a[i].append(0);


    for j in range(0, width):
        temp = [];
        for i in range(0, height):
            temp.append(x[i][j]);
        
        print(temp);
        max_j = max(temp);
        min_j = min(temp);

        for i in range(0, height):
            temp2 = (temp[i] - min_j)/(max_j - min_j);
            a[i][j] = temp2;

    
    return a;


def build_diagramm(data, labels, axes):
    '''функция для построения лепестковых диаграмм '''
    #data - данные по которым будут строиться диогранммы
    #labels - подписи к осям
    #axes - оси для отрисовки polar = true

    labels=np.array(labels);
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False);
    angles=np.concatenate((angles,[angles[0]]));
    stats=np.concatenate((data,[data[0]]));

    axes.plot(angles, stats, 'o-', linewidth=2);
    axes.fill(angles, stats, alpha=0.25);

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False);
    axes.set_thetagrids(angles * 180/np.pi, labels);


def compute_area(data):
    '''функция для расчета площади моей лепестковой диаграммы'''
    # data - строка с нормированными показателями по которым строилась лепестковая диаграмма
    area = 0;

    data_len = len(data);

    for i in range(0, data_len - 1 ):
        area += data[i]*data[i+1];

    area += data[data_len - 1]*data[0];
    area *= 0.4330127018922193; #sin(pi/3)/2 = 0.4330127018922193
    return area;