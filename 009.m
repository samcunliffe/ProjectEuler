% Project Euler - Problem 9
% =========================
% A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
% 
% a^2 + b^2 = c^2
%
% For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
% 
% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.

for a=1:1000
    for b=1:1000
        c = sqrt( (a^2) + (b^2) );
        if ((c-floor(c)) == 0)
            %triangle number is found!
            %add 'em up and see if 1000
            Total = a+b+c;
            if (Total==1000)
                disp('Total value found');
                DispArray1 = ['a = ' num2str(a) ';  ' 'b = ' num2str(b) ';  ' 'c = ' num2str(c) ';  '];
                disp(DispArray1);
                Product=a*b*c;
                DispArray2 = ['abc = ' num2str(Product)];
                disp(DispArray2);
                disp('=======');
            end
        end
    end
end
