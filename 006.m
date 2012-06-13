% Octave

% Project Euler - Problem 6
% =========================
% The sum of the squares of the first ten natural 
% numbers is, 
%       1^(2) + 2^(2) + ... + 10^(2) = 385
%
% The square of the sum of the first ten natural 
% numbers is,
%       (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
%
% Hence the difference between the sum of the 
% squares of the first ten natural numbers and the
% square of the sum is 3025 − 385 = 2640.
%
% Find the difference between the sum of the squares
% of the first one hundred natural numbers and the
% square of the sum.

n       =   1;
Maximum = 100;

SumOfSquares = 0;
Sum          = 0;

while (n <= Maximum)
	SumOfSquares = SumOfSquares + (n^(2));
	Sum = Sum + n;

	n = n + 1;
endwhile

SquareOfSum = Sum^(2);
Answer = SquareOfSum - SumOfSquares
