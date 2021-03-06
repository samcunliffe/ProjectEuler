%Project Euler - Problem 8
%=========================
%Find the greatest product of five consecutive digits in the 1000-digit
%number.
%=========================

%Loads and sorts digits into elements of a row vector
disp('Loading data...');
cd 'H:/Project Euler'
load problem8data.txt;    %a 50x20 matrix
TheNumber = zeros(1,1000); %a row vector containing 1000(=50*20) entries

%takes each row of data matrix and adds it onto the end of row vector
for RowCount=1:20
    TheNumber(((RowCount*50)-49):(RowCount*50))=problem8data(RowCount,1:50);
end
disp('Data is loaded');

%product variables
ProductLength=5;
ProductOne=1;
ProductTwo=0;
GreatestProduct = ProductTwo;
disp('Beginning sum loop for product length =');
disp(ProductLength);
for i=1:(1000-ProductLength)
    
    for j=i:(i+ProductLength)
        ProductOne = ProductOne*TheNumber(1,j);       %somthing wrong with this loop
    end
    
    if (ProductOne > ProductTwo)
        GreatestProduct = ProductOne;
    end
    
    ProductTwo = ProductOne;
    ProductOne = 1;
    
end
disp('Finished, Greatest product =');
disp(GreatestProduct);