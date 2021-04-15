/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer, and rotates the characters in the string to the right by that given integer amount.
*/

const str1 = "Hello World";
const rotateAmnt1 = 0;
const expected1 = "Hello World";

const str2 = "Hello World";
const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const str3 = "Hello World";
const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const str4 = "Hello World";
const rotateAmnt4 = 4;
const expected4 = "orldHello W";


//create result string
//create variable to store moving letter
//iterate through string
//shift string right
//insert variable at start
//repeat x times
//return



// function rotateStr(str, n) { 
//     let rotatedString = ""
//     for (let i = str.length-1; i > str.length-n ;i--){ 
//         rotatedString += str[i]
//     }
//     for(let j = 0; j < str.length-n; j++){
//         rotatedString += str[j]
//     }
//     return rotatedString
// }
// console.log(rotateStr(str1,rotateAmnt1))
// console.log(rotateStr(str2,rotateAmnt2))
// console.log(rotateStr(str3,rotateAmnt3))
// console.log(rotateStr(str4,rotateAmnt4))


//get a new string that is the last n characters
//reverse that string
//concat that and the old string
//pop the last n
function rotateStr(str, n) {
    let charactersToRotate=""
    if (n != 0){
        for (let i = str.length-n; i < str.length; i++){
            charactersToRotate += str[i]
        }
        charactersToRotate.split("").reverse().join()
        let rotatedString = "" 
        rotatedString += charactersToRotate
        for (let i = 0; i < str.length - n ;i++){
            rotatedString += str[i]
        }
        return rotatedString
        }
    return str
}

console.log(rotateStr(str1,rotateAmnt1))
console.log(rotateStr(str2,rotateAmnt2))
console.log(rotateStr(str3,rotateAmnt3))
console.log(rotateStr(str4,rotateAmnt4))

/*****************************************************************************/

/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

function rotateStr(str, n) {
    let charactersToRotate=""
    if (n != 0){
        for (let i = str.length-n; i < str.length; i++){
            charactersToRotate += str[i]
        }
        charactersToRotate.split("").reverse().join()
        let rotatedString = "" 
        rotatedString += charactersToRotate
        for (let i = 0; i < str.length - n ;i++){
            rotatedString += str[i]
        }
        return rotatedString
        }
    return str
}


function isRotation(s1, s2) { 
    for(let i =0; i < s1.length ;i++){
      if (rotateStr(s1, i) === s2){
        return true
      }
    }
    return false
  }
  
  console.log(isRotation(strA1, strB1))
  console.log(isRotation(strA2, strB2))