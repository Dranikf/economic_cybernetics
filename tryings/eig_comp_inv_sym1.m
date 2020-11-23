function [max_lambda, vector] = eig_comp_inv_sym1(matrix, info)
    % compution of eig by gigla algorimt 1
    % input:
    % matrix - matrix for compution
    % output:
    % max_lambda - maximum eigenvalue
    % vector - corresponding vector
    % info - is it needed to show some more info

    str_sum = sum(matrix, 2);
    str_col_sum = sum(str_sum);
    vector = str_sum ./ str_col_sum;

    max_lambda = matrix*vector ./ vector;

    if info
        disp('strings sum');
        str_sum
        disp('final sum');
        str_col_sum
        disp('matrix*vector');
        matrix*vector
    end

end