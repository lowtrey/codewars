// Instructions
// Complete the solution so that the function will break up camel casing, using a space between words.

// Example
// solution('camelCasing') // => should return 'camel Casing'


// My Solution
function solution(string) {
  let solution = string;
  for(let i = 0; i < string.length; i++) {
    let currentChar = string.charAt(i);
    if(currentChar === currentChar.toUpperCase()) {
      solution = solution.split(currentChar).join(` ${currentChar}`);
    };
  };
  return solution;
}


// Sample Tests
Test.assertEquals(solution('camelCasing'), 'camel Casing')

// Top Answer
function solution(string) {
  return(string.replace(/([A-Z])/g, ' $1'));
}