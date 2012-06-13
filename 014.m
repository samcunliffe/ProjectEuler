% MATLAB

% Project Euler - Problem 14
% ==========================
% The following iterative sequence is defined for 
% the set of positive integers:
%           n  n/2 (n is even)
%           n  3n + 1 (n is odd)
% 
% Using the rule above and starting with 13, we
% generate the following sequence:
%       13  40  20  10  5  16  8  4  2  1
% 
% It can be seen that this sequence (starting at 13
% and finishing at 1) contains 10 terms. Although 
% it has not been proved yet (Collatz Problem), it
% is thought that all starting numbers finish at 1.
% 
% Which starting number, under one million, produces
% the longest chain?
% 
% NOTE: Once the chain starts the terms are allowed
% to go above one million.

TermCount = 0;
BiggestSoFar=1;

for StartingInt = 13:1E6
    n=StartingInt;
    while (n > 1)
        TermCount=TermCount+1;
        Remainder=(n/2) - floor(n/2);
        if (Remainder==0) %n is even
            n=n/2;
        else %n is odd
            n=(3*n)+1;
        end       
    end
    
    if (TermCount > BiggestSoFar)
        BiggestSoFar = TermCount;
        disp(StartingInt)
        disp(BiggestSoFar)
        TermCount=0;
    else
        TermCount = 0;
    end
    
end
