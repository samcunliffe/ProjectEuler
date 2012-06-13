function s=getithDigit(n,i)
    %this function gets the ith digit in number
    s=floor(n/(10^(i)))-junk;
end