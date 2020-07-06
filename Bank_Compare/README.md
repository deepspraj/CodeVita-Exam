# Bank Comparison

The question was asked in Codevita Examination 2019

## Problem Statement

There are two banks; Bank A and Bank B. Their interest rates vary. You have received offers from both bank in terms of annual rate of interest, tenure and variations of rate of interest over the entire tenure.

You have to choose the offer which costs you least interest and reject the other.

Do the computation and make a wise choice.

The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :

EMI = (loanAmount * monthlyInterestRate )/( 1 - 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))

## Explaination

Find EMI for every slot of bank A and bank B. 

Sum all the EMI's for bank A and bank B respectively. 

Compare both the EMI and get the result.

<br/>
<br/>

```\Bank_Compare>python bankCompare.py```

```500000```

```20```

```3```

```10 9.5```

```5 9.0```

```5 6.8```

```2```

```10 9.2```

```10 5.6```

Output :

```Bank B```
