import matplotlib.pyplot as plt
import numpy as np
from math import sin;

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

def build_diagramm(a):

    labels=np.array(['a1', 'a2', 'a3', 'a4', 'a5', 'a6']);
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False);
    angles=np.concatenate((angles,[angles[0]]));
    stats=np.concatenate((a,[a[0]]));

    fig = plt.figure();
    ax = fig.add_subplot(111, polar=True);
    ax.plot(angles, stats, 'o-', linewidth=2);
    ax.fill(angles, stats, alpha=0.25);

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False);
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.show();