function fsr_chcker(Z,L)
    s = size(Z);
    n = numel(L);

    for i = 1:100000
        k =  unidrnd(100000, 1,s(1));
        res = [0 0 0 0];
        for j= 1:s(1)
            res = res+Z(j,:)*k(j);
        end
        disp(['+++++++++++++++++++++++++', num2str(i)]);
        for j = 1:n
            a = subs(L(j), [sym('db1') , sym('db2') , sym('db3'), sym('t')], res)
            if a<0     
                disp('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                k
                a
                res
                return
            end
        end
        disp(['+++++++++++++++++++++++++', num2str(i)]);
    end

end