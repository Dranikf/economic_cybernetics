function a = ez_calc(m, L, al, bet)
    %subs(L, [sym('db1') , sym('db2') , sym('db3'), sym('t')], [1 2 3 4])
    a = -subs(L, [sym('db1') , sym('db2') , sym('db3'), sym('t')], m(bet,:))*m(al, :) + subs(L, [sym('db1') , sym('db2') , sym('db3'), sym('t')], m(al,:))*m(bet, :);

end