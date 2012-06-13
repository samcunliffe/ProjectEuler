% Octave

% Project Euler Problem 1
% =======================
% If we list all the natural numbers below 10 that
% are multiples of 3 or 5, we get 3, 5, 6 and 9. 
% The sum of these multiples is 23.
%
% Find the sum of all the multiples of 3 or 5 below 1000.

n =  3;
m =  5;
l = 15;

Total     = 0;
Overcount = 0;

MaximumLoops = 1000;

while (n < MaximumLoops)
	Total = Total + n;
	n = n + 3;
endwhile

while (m < MaximumLoops)
	Total = Total + m;
	m = m + 5;
endwhile

while (l < MaximumLoops)
	Overcount = Overcount + l;
	l = l + 15;
endwhile

Answer = Total - Overcount
