const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

function dedupeSorted(nums) {
    dedupedArray = []
    dedupedArray.push(nums[0])
    for (let i = 1; i < nums.length; i++){
      if (nums[i] != nums[i-1]){
        dedupedArray.push(nums[i])
      }
    }
    return dedupedArray
  }

  console.log(dedupeSorted(nums1))
  console.log(dedupeSorted(nums2))
  console.log(dedupeSorted(nums3))



const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

function mode(nums) {
    if (nums.length===1){
        return nums
    }
  let frequencyDict = {}
  if (nums.length > 0) {
    for (let i = 0; i < nums.length; i++) {
      if(!frequencyDict[nums[i]]) {
        frequencyDict[nums[i]] = 0
      }
      ++frequencyDict[nums[i]]
    }
  }
  let frequentest = 0
  for (index in frequencyDict){
    if (frequencyDict[index] > frequentest){
        frequentest = frequencyDict[index]
    }
  }
  let returnArray = []
  let notSame = false
  for (index in frequencyDict){
    if (frequencyDict[index] === frequentest){
      returnArray.push(index)
    } else{
        notSame = true
    }
  }
  if (notSame === true){
    return returnArray
  }
    return []
}


console.log(mode(nums1))
console.log(mode(nums2))
console.log(mode(nums3))
console.log(mode(nums4))
console.log(mode(nums5))