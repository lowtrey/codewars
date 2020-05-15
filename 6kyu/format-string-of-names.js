// Instructions
// Given: an array containing hashes of names

// Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

// Example:

// list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// // returns 'Bart, Lisa & Maggie'

// list([ {name: 'Bart'}, {name: 'Lisa'} ])
// // returns 'Bart & Lisa'

// list([ {name: 'Bart'} ])
// // returns 'Bart'

// list([])
// // returns ''
// Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

// My Solution
function list(names) {
  if (names.length === 0) {
    return "";
  } else if (names.length === 1) {
    return names[0].name;
  } else if (names.length === 2) {
    return `${names[0].name} & ${names[1].name}`;
  } else {
    const namesArray = [];

    for (let index = 0; index < names.length - 1; index++) {
      if (index === names.length - 2) {
        namesArray.push(
          `${names[names.length - 2].name} & ${names[names.length - 1].name}`
        );
      } else {
        namesArray.push(names[index].name);
      }
    }

    return namesArray.join(", ");
  }
}

// Sample Tests
Test.assertEquals(
  list([
    { name: "Bart" },
    { name: "Lisa" },
    { name: "Maggie" },
    { name: "Homer" },
    { name: "Marge" },
  ]),
  "Bart, Lisa, Maggie, Homer & Marge",
  "Must work with many names"
);
Test.assertEquals(
  list([{ name: "Bart" }, { name: "Lisa" }, { name: "Maggie" }]),
  "Bart, Lisa & Maggie",
  "Must work with many names"
);
Test.assertEquals(
  list([{ name: "Bart" }, { name: "Lisa" }]),
  "Bart & Lisa",
  "Must work with two names"
);
Test.assertEquals(
  list([{ name: "Bart" }]),
  "Bart",
  "Wrong output for a single name"
);
Test.assertEquals(list([]), "", "Must work with no names");

// Top Answer
function list(names) {
  return names.reduce(function (prev, current, index, array) {
    if (index === 0) {
      return current.name;
    } else if (index === array.length - 1) {
      return prev + " & " + current.name;
    } else {
      return prev + ", " + current.name;
    }
  }, "");
}
