function  fsr_chker2(eqes, solutions, n)

    eq_count = numel(eqes);
    sol_count = numel(solutions);

    k_sym = [];
    for i = 1:n
        k_sym = [k_sym, sym(['k', num2str(i)])];
    end
    k_sym

    for i = 1:100000
        disp(['iteration +++++++++++++++++', num2str(i)]);
        k =  unidrnd(100000, 1, n);
        x = [];
        
        for j = 1:sol_count
            x = [x ; subs(solutions(j), k_sym , k)];
        end
        
        res = [];
        for j = 1:eq_count
            temp =  subs(eqes(j), symvar(eqes(j)) ,x');
            if temp < 0
                disp('aaaaaaaaaaa')
                k
                x
                res
                temp
                return;
            end
            res = [res,temp];
        end
        res
        x
        disp(['iteration +++++++++++++++++', num2str(i)]);
    end
end