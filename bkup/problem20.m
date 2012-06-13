%% (Unolved) This code works in MATLAB 
%
%
% Project Euler - Problem 20
% ==========================
% n! means n × (n ? 1) × ... × 3 × 2 × 1
% 
% Find the sum of the digits in the number 100!
%
%
%%
format long
n=factorial(100);
total =0;
for i=1:digitcount(n)
    total = total + getithDigit(n,i);
end