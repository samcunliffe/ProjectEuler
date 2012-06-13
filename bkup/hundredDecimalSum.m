function s=hundredDecimalSum(decimalNumber)
    runningDecimal = decimalNumber;
    s=0;

    for p=1:10
        dth = 10^(-p);
        runningDecimal = decimalNumber - runningDecimal;
        s = s + floor(runningDecimal/dth);
        runningDecimal = floor(runningDecimal/dth)*dth;
    end

end