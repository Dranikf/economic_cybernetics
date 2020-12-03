function sym_sol = solution_disp(matr)

    s = size(matr);
    sym_sol = [];

    for i = 1:s(2);
        line = ' ';
        for j = 1:s(1)
            elem = double(matr(j, i));
            if elem >= 0
                sig = '+';
            else
                sig = '';
            end
            line = [line, sig, num2str(double(elem)), '*k', num2str(j)];

        end
        disp(line);
        sym_sol = [sym_sol, sym(line)];
    end

end