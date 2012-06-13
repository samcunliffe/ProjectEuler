% MATLAB

% Project Euler - Problem 7
% =========================
% By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
% we can see that the 6th prime is 13.
%
% What is the 10001st prime number?

i = 1;
Max = 1E7;
IntegerToBeDivided = 1;
n=1;
while (i < Max)
    if (isprime(i)==1)
        if (n==10001)
            disp(n);
            disp(i);
            i=Max+1;
        end
    n=n+1;
    end 
    i=i+1;
end
disp('Finished');
