function [max_lambda, vector] = eig_comp_inv_sym2(matrix, info)
    % compution of eig by gigla algorimt 2
    % input:
    % matrix - matrix for compution
    % info - is it needed to show some more info
    % output:
    % max_lambda - maximum eigenvalue
    % vector - corresponding vector

    col_sum = sum(matrix, 1)';
    inv_col = 1./col_sum;
    inv_sum = sum(inv_col);
    vector = inv_col ./ inv_sum;
    max_lambda = matrix*vector ./ vector;

    if info
        disp('columns sum');
        col_sum
        disp('inverse colums sums');
        inv_col
        disp('sum of inv_col');
        inv_sum
        disp('matrix*vector');
        matrix*vector
    end

    

    

end