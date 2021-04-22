//create remainder var
//create empty dict
// take given cents, modulo 25, store that result as remainder
// subtract remainder from cents. divide result by 25 and  if the result is greater than 0, store as quarter in dict.
//repeat for dime and nickel
//final remainder is penny.
//return dict



//create counter var, start at 0
//iterate through array, when value = 0, +1 counter and loop.
//when it does not find a match, check if counter - arr.length-1.
//if yes, return null, if no, return counter




/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

function coinChangeHelper(coinVal, coinType, cents, changeObj){
    let remainder = 0
    remainder = cents % coinVal
    if (cents-remainder> 0){
      changeObj[coinType] = (cents-remainder)/coinVal
      cents = cents - changeObj[coinType]*coinVal
    }
    return cents
  }
  
  function fewestCoinChange(cents) {
    let changeObj = {}
    cents = coinChangeHelper(25, "quarter", cents, changeObj)
    cents = coinChangeHelper(10, "dime", cents, changeObj)
    cents = coinChangeHelper(5, "nickel", cents, changeObj)
    cents = coinChangeHelper(1, "penny", cents, changeObj)
    return changeObj
  }
  
  
  console.log(fewestCoinChange(cents1))
  console.log(fewestCoinChange(cents2))
  console.log(fewestCoinChange(cents3))
  console.log(fewestCoinChange(cents4))
  


function fewestCoinChange(cents) {
    let remainder = 0
    let changeObj = {}
    remainder = cents % 25
    if (cents-remainder> 0){
      changeObj['quarter'] = (cents-remainder)/25
      cents = cents - changeObj['quarter']*25
    }

    remainder = cents % 10
    if (cents-remainder> 0){
      changeObj['dime'] = (cents-remainder)/10
      cents = cents - changeObj['dime']*10
    }

    remainder = cents % 5
    if (cents-remainder> 0){
      changeObj['nickel'] = (cents-remainder)/5
      cents = cents - changeObj['nickel']*5
    }

    if (cents > 0){
      changeObj['pennt'] = cents
    }
    return changeObj
  }
  
    console.log(fewestCoinChange(cents1))
    console.log(fewestCoinChange(cents2))
    console.log(fewestCoinChange(cents3))
    console.log(fewestCoinChange(cents4))

//create remainder var
//create empty dict
// take given cents, modulo 25, store that result as remainder
// subtract remainder from cents. divide result by 25 and  if the result is greater than 0, store as quarter in dict.
//repeat for dime and nickel
//final remainder is penny.
//return dict

/*****************************************************************************/

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const nums1 = [3, 0, 1];
const expected1 = 2;




const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

function missingValue(unorderedNums) {}
