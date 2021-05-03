const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

const nums4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
const searchNum4 = 19;

function binarySearch(sortedNums, searchNum){
    if (sortedNums.length === 0) return false
    let searchIndex = Math.floor(sortedNums.length/2)
    if (sortedNums[searchIndex] === searchNum){
        return true
    } else if (sortedNums[searchIndex] > searchNum){
        sortedNums = sortedNums.slice(0, searchIndex)
    } else if (sortedNums[searchIndex] < searchNum){
        sortedNums = sortedNums.slice(searchIndex+1, sortedNums.length)
    }
    return binarySearch(sortedNums, searchNum)
}



console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))
console.log(binarySearch(nums4, searchNum4))


// base case, if array empty, return false
// if Math.floor(sortedNums.length/2) is searchnum, return true
// if sortedNums > Math.floor(sortedNums.length/2)
// slice 0 to Math.floor(sortedNums.length/2)
// else
// slice Math.floor(sortedNums.length/2) to sortedNums.length
// return recursion 