clc;
clf;
clear all;
xn = input("Enter x[n] : ");
subplot(3,1,1);
plot2d3(xn);
hn = input("Enter h[n] : ");
subplot(3,1,2);
plot2d3(hn);
x_new =[];
for i = 1 : length(xn)
    x_new = [x_new;xn];
    xn = [xn($) xn(1:$-1)];
end
//x_trans = x_new';
yn=x_new' * hn';
disp(yn);
subplot(3,1,3);
plot2d3(yn);
