/* 
	Acronyms
	Create a function that, given a string, returns the string’s acronym 
	(first letter of each word capitalized). 
	Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";
// str1.split(" ") => ["there's", "no", "free", "lunch"]
function acronymize(str) {
  acronymString = ""
  if (str[0] != " "){
    acronymString += str[0]
  }
  for(let i =0; i < str.length;i++){
    if (str[i] === " "){
      if (i+1 < str.length){
        acronymString += str[i+1]
      }
    }
  }
  upperAcroString = acronymString.toUpperCase()
  return upperAcroString
}

console.log(acronymize(str1))
console.log(acronymize(str2))

/*****************************************************************************/

/* 
	String: Reverse
	Given a string,
	return a new string that is the given string reversed
*/
// Strings are immutable
// Strings are 0 indexed
// str1[3]
const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
  reversedString = ""
  for (let i = str.length-1; i >= 0; i--) {
    reversedString += str[i]
  }
  return reversedString
}

console.log(reverseString(str1))
console.log(reverseString(str2))