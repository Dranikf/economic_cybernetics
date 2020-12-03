function tabl = compute_table(matr, L)
    s = size(matr);
    new_vec = [];

    for i = 1:s(1)
        new_vec = [new_vec; subs(L, [sym('db1') , sym('db2') , sym('db3'), sym('t')], matr(i,:))];
    end
    tabl = [matr, new_vec];
end