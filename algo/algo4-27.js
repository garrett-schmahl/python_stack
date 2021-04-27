//if num = 1
//return 1
//else
//return num*recursiv(num-1)
//floor it somewhere


//call function with default arguments fibnum, fibcount=0, fib1=0, fib2=1
//if fibnum = fibcount
//return fib1+fib2
//else
//return function(fibnum, fib2, fib1+fib2, fibcount++)


/* 
  Recursive Factorial
  Input: integer
  Output: integer, product of ints from 1 up to given integer
  
  If less than zero, treat as zero.
  Bonus: If not integer, truncate (remove decimals).
  
  Experts tell us 0! is 1.
  
  rFact(3) = 6 (1*2*3)
  rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

// 7!
// 7 * 6 * 5 * 4 * 3 * 2 * 1

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

function factorial(n) {
    n = Math.floor(n)
    if (n < 0) n = abs(n)
    if(n < 2) return n
    return n*factorial(n-1)
  }
  
  console.log(factorial(num1))
  console.log(factorial(num2))
  console.log(factorial(num3))

/*****************************************************************************/

/* 
  Return the fibonacci number at the nth position, recursively.
  
  Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  The next number is found by adding up the two numbers before it,
  starting with 0 and 1 as the first two numbers of the sequence.
*/

const num1 = 0;
const expected1 = 0;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;

function fibonacci(fibNum, fibCount = 2, fib1 = 0, fib2 = 1) {
    if (fibNum < 2) return fibNum
    if (fibNum === fibCount) return fib1 + fib2
    return fibonacci(fibNum, fibCount+1, fib2, fib1+fib2)
  }

console.log(fibonacci(num1))
console.log(fibonacci(num2))
console.log(fibonacci(num3))
console.log(fibonacci(num4))
console.log(fibonacci(num5))
console.log(fibonacci(num6))


const num1 = 0;
const expected1 = 0;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;


function grp5fib(num){
    if(num < 2) return num
    return grp5fib(num-1)+grp5fib(num-2)
}
  
console.log(grp5fib(num1))
console.log(grp5fib(num2))
console.log(grp5fib(num3))
console.log(grp5fib(num4))
console.log(grp5fib(num5))
console.log(grp5fib(num6))


const num1 = 0;
const expected1 = 0;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;


function fibMemo(num, memo={0:0, 1:1}){
    if(num < 0) return null
    if (memo[num] !== undefined) return memo[num]
    memo[num] = fibMemo(num-1) + fibMemo(num-2)
    return memo[num]
}

console.log(fibMemo(num1))
console.log(fibMemo(num2))
console.log(fibMemo(num3))
console.log(fibMemo(num4))
console.log(fibMemo(num5))
console.log(fibMemo(num6))