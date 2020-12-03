
m = 22
for i = [1:5,7,9:12, 14:24]
    for j = [6 8 13]
        %T = [T;ez_calc(Z, L4, i ,j )]
        disp(['T_', num2str(i), '_', num2str(j), '_0 [', num2str(double(ez_calc(Z, L4, i ,j ))), '] = T', num2str(m)])
        m = m+1;
    end
end