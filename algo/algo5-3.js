
/* 
  https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/
  Stable sort
  
  Time Complexity
    - Best: O(n) linear when array is already sorted.
    - Average: O(n^2) quadratic.
    - Worst: O(n^2) quadratic when the array is reverse sorted.
  Space: O(1) constant.
  For review, create a function that uses BubbleSort to sort an unsorted array in-place.
  For every pair of adjacent indices, swap them if the item on the left is larger than the item on the right until array is fully sorted
*/

const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

/*
 * Sorts the given nums in-place by mutating the array.
 * Best: O(n) linear when array is already sorted.
 * Average: O(n^2) quadratic.
 * Worst: O(n^2) quadratic when the array is reverse sorted.
 * @param {Array<number>} nums
 * @returns {Array<number>} The given nums after being sorted.
 */

function bubbleSort(nums) {
    let stopTrigger=false
    while(stopTrigger===false){
        stopTrigger=true
        for(let i=0;i<nums.length-1;i++){
            if(nums[i]>nums[i+1]){
                let saveVal = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = saveVal
                stopTrigger=false
            }
        }
    }
    return nums
}

console.log(bubbleSort(numsRandomOrder))
console.log(bubbleSort(numsReversed))


//first loop to repeat entire process until a trigger tells it to stop
//loop inside is working loop, compares each value with the next and swaps if next is lower




/* 
  https://visualgo.net/en/sorting
    
  Selection sort works by iterating through the list, finding the minimum
  value, and moving it to the beginning of the list. Then, ignoring the first
  position, which is now sorted, iterate through the list again to find the
  next minimum value and move it to index 1. This continues until all values
  are sorted.
  Unstable sort.
  
  Time Complexity
    - Best: O(n^2) quadratic.
    - Average: O(n^2) quadratic.
    - Worst: O(n^2) quadratic.
  Space: O(1) constant.
  Selection sort is one of the slower sorts.
  - ideal for: pagination, where page 1 displays 10 records for example,
      you run selection sort for 10 iterations only to display the first 10
      sorted items.
*/

const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

/*
 * Sorts given array in-place.
 * Best: O(n^2) quadratic.
 * Average: O(n^2) quadratic.
 * Worst: O(n^2) quadratic.
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array after being sorted.
 */

function selectionSort(nums) {
    let saveIndex = 0;
    for(let i=0;i<nums.length;i++){
        saveIndex = i;
        for(let j=i+1;j<nums.length;j++){
            if (nums[saveIndex] > nums[j]){
                saveIndex = j;
            }
        }
        [nums[i], nums[saveIndex]] =
        [nums[saveIndex], nums[i]];
    }
    return nums
}

console.log(selectionSort(numsRandomOrder))
console.log(selectionSort(numsReversed))

//nested loops
//for loop that determines what index is being swapped to
//for loop that iterates through list and finds lowest value
//close for loop
//swap values
//close for loop
//return sorted array