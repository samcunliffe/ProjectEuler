%Project Euler - Problem 4
%=========================
%A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91-99.
%
%Find the largest palindrome made from the product of two 3-digit numbers.

a=99;

while (a > 1)
   b=99;
   while (b > 1)
      %changes product to a string and splits string into two
      AB = a*b;
      StringAB = int2str(AB);
      DigitCount = digitcount(AB);
      
      %splits number into two ranges
       EndFirstRange = floor(DigitCount/2);
       StartSecondRange = ceil((DigitCount/2))+1;
       FirstHalfOfDigits  = StringAB(1:EndFirstRange);
       SecondHalfOfDigits = StringAB(StartSecondRange:DigitCount);
      
      %reverse order of SecondHalfOfDigits
      c = EndFirstRange;
      d = 1;
      while (c > d)       
         SecondHalfOfDigitsFlipped(c) = SecondHalfOfDigits(d);
         c = c-1;
         d = d+1;
      end
      
      if (SecondHalfOfDigitsFlipped == FirstHalfOfDigits)
         %prints result if palindrom is found
         disp(a);
         disp(b);
         disp(AB);
         
         %then exit for loops
         b=1;
         a=1;
      end 

      b = b-1;		
   end 
   a = a-1;   
end
