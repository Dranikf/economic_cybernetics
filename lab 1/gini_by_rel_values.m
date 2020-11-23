function  gini = gini_by_rel_values(x, y, info)

    % function for compution gini corffficient
    % input data:
    % x - the accumulated share of enterprises in their total amount
    % y - accumulated share of receivables by enterprises in the total amount of debt
    % info - is it neded to show some additional info
    % output data:
    % computed gini koef
    
    n = numel(x);

    t_x = x(1:n-1);
    t_y = y(2: n);

    s1 = sum(t_x.*t_y);

    t_x_ = x(2:n);
    t_y_ = y(1: n-1);

    s2 = sum(t_x_.*t_y_);

    if info
        disp('t_y = x(1: n-1)');
        t_x
        disp('t_y = y(2: n)');
        t_y
        disp('s1 = sum(t_x.*t_y);');
        s1
        disp('t_x_ = x(2:n)');
        t_x_
        disp('t_y_ = y(1:n-1)');
        t_y_
        disp('s2 = sum(t_x_.*t_y_);');
    end

    gini = s1 - s2; 

end