a = [1 1/4 1/2 5/4;
     4 1 2 5;
     2 1/2 1 5/2;
     4/5 1/5 2/5 1];

col_sum = sum(a, 1)'
obr_col_sum = ones(4 , 1) ./ col_sum