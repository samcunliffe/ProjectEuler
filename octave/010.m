%Project Euler - Problem 10
%==========================
% The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
% 
% Find the sum of all the primes below two million.
Max=2E6;
Total=0;
for i=1:Max
    if (isprime(i)==1)
        Total=Total+i;
    end
end
format long g;
disp(Total);