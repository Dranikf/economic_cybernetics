a = [1 1/4 1/2 5/4;
     4 1 2 5;
     2 1/2 1 5/2;
     4/5 1/5 2/5 1];

str_sum = sum(a, 2)
str_col_sum = sum(str_sum);

b = str_sum ./ str_col_sum;