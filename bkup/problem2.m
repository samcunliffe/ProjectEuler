% Octave

% Project Euler Problem 2
% =======================
% Each new term in the Fibonacci sequence is
% generated by adding the previous two terms. By
% starting with 1 and 2, the first 10 terms will
% be:
%     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
%
% Find the sum of all the even-valued terms in
% the sequence which do not exceed four million.

FirstTerm  = 1;
SecondTerm = 2;
NewTerm    = 3;

Maximum = 4E6;
Total   = 2;

while (NewTerm <= Maximum)
   %generates each term in Fibonacci sequence
	NewTerm = FirstTerm + SecondTerm 

	%finds remainder of division by 2 (=0 if even)
	RemainderOfDivision = NewTerm-(2*(floor(NewTerm/2))) 
	
	if (RemainderOfDivision == 0)
		Total = Total + NewTerm;
	endif

   %readies variables for next iteration
	FirstTerm  = SecondTerm; 
	SecondTerm = NewTerm;
		
endwhile

Total
