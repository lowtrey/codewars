// Instructions
// You have an array of numbers.
// Your task is to sort ascending odd numbers but even numbers must be on their places.

// Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

// Example

// sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


// My Solution
function sortArray(array) {
  // Return a sorted array.
  let result = [];
  if(array.length > 0) {
    result = array;
    let odds = array.filter(num => num % 2 !== 0);
    odds.sort((a, b) => a - b);
    for(let i = 0; i < result.length; i++) {
      if(result[i] % 2 !== 0) {
        result[i] = odds[0];
        odds.shift();
      };
    };
  };
  return result;
}


// Sample Tests
Test.assertSimilar(sortArray([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
Test.assertSimilar(sortArray([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
Test.assertSimilar(sortArray([]),[])

// Top Answer
function sortArray(array) {
  const odd = array.filter((x) => x % 2).sort((a,b) => a - b);
  return array.map((x) => x % 2 ? odd.shift() : x);
}