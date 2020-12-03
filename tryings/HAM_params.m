function [cons_ind, prioties, t] = HAM_params(matrix)
    % hierarchy analysis method
    % input data
    % matrix - matrix of priorities
    % output data
    % cons_ind - consistency index
    % priorities - vector of priorities

    [max_lambda, prioties] = eig_comp_inv_sym1(matrix, false);

    max_lambda = mean(max_lambda);
    s = size(matrix); s = s(1);

    cons_ind = (max_lambda - s)/(s - 1);

end