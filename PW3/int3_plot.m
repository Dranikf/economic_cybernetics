
figure
hold on
xlabel('x');
ylabel('y');
zlabel('z');


[Z,Y] = meshgrid(1.2:0.2:6,1.15:0.2:4.2);

X = Z*0;

surf(X+1.05, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Red');
surf(X +1.3, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Red');

[X,Z] = meshgrid(1.05:0.01:1.3,1.2:0.2:6);

Y = Z * 0 + 1.15;
surf(X, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Blue');
Y = 1.5+2.*X;
surf(X, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Blue');

[X,Y] = meshgrid(1.05:0.01:1.3,1.15:0.2:4.2);
Z = Y * 0 + 1.2;
surf(X, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Green');
Z = 0.5 + 1.5*X + 0.9*Y;
surf(X, Y, Z, 'FaceAlpha', 0.5, 'FaceColor', 'Green');