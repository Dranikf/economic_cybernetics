from hello import norm_multidirectional;
from hello import build_diagramm;

x = [[3, 2.6, 2.4, 113, 47, 0.3],
    [ 2.3, 2.6,2.7,98,49,0.6],
    [2.6,2.5,2.5,117,48,1.2],
    [4.3,2.5,2.4,91,55,2.3],
    [2.9,2.8,2.1,99,49,2.6],
    [2.4,3.1,3.1,89,52,5.5],
    [5.1,1.6,2.1,79,58,2.4],
    [3.4,2,1.7,72,57,1.6],
    [2,2.9,2.7,123,50,3.2],
    [4.5,2.9,2.8,80,53,4.2]];
a = norm_multidirectional(x);

for i in range(0, 10):
    print(a[i]);


build_diagramm(a[0]);
build_diagramm(a[1]);
build_diagramm(a[2]);