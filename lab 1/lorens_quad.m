function koefs = lorens_quad(x, y, info)
    % function for square approximation of lorens function
    % input data:
    % x - the accumulated share of enterprises in their total amount
    % y - accumulated share of receivables by enterprises in the total amount of debt
    % info - is it neded to show some additional info
    % 
    % output data:
    % koefs - vector of coefficients of the approximating function y = koef(1)*x^2 + koef(2)*x + koef(3) 

    x_four = x.^(4);
    x_three = x.^(3);
    x_two = x.^(2);
    yx_two = y.*(x_two);
    yx = x.*y;

    x_four_sum = sum(x_four);
    x_three_sum = sum(x_three);
    x_two_sum = sum(x_two);
    yx_two_sum = sum(yx_two);
    yx_sum = sum(yx);
    y_sum = sum(y);
    x_sum = sum(x);


    a = [x_four_sum x_three_sum x_two_sum;
         x_three_sum x_two_sum x_sum;
         x_two_sum x_sum 1];

    b = [yx_two_sum; yx_sum; y_sum];

    if info
        disp('system of coofs');
        a
        b 
    end

    koefs = inv(a) * b;

end