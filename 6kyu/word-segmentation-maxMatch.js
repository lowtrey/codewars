// Instructions
// MaxMatch starts at the first character of a sentence and tries to find the longest valid word starting from that character. 
// If no word is found, the first character is deemed the longest "word", regardless of its validity. 
// In order to find the rest of the words, MaxMatch is then recursively invoked on all of the remaining 
// characters until no characters remain. A list of all of the words that were found is returned.

// So for the string "happyday", "happy" is found because "happyday" is not a valid word, nor is "happyda", 
// nor "happyd". Then, MaxMatch is called on "day", and "day" is found. The output is the list ["happy", "day"] in that order.

// The Challenge
// Write maxMatch, which takes an alphanumeric, spaceless, lowercased String as input and returns an 
// Array of all the words found, in the order they were found. All valid words are in the Set VALID_WORDS, 
// which only contains around 500 English words.


// My Solution
function maxMatch(sentence) {
  const longestWords = [];
  let currentSentence = sentence;
  
  // Start At First Character
  while(currentSentence.length) {
    // Find Valid Words
    const validWords = [];
    for(let charIndex = 1; charIndex <= currentSentence.length; charIndex++) {
      if(VALID_WORDS.has(currentSentence.slice(0, charIndex))) {
        validWords.push(currentSentence.slice(0, charIndex));
      };
    };
    // Find Lomgest Valid Word
    const longestValidWord = 
      validWords.length > 0 ?
      validWords.sort((a, b) => b.length - a.length)[0] :
      currentSentence.charAt(0);
      
    longestWords.push(longestValidWord);
    currentSentence = currentSentence.replace(longestValidWord, "");
  };
return longestWords;
}


// Sample Tests
Test.assertDeepEquals(maxMatch('goodluck'), ['good','luck']);
Test.assertDeepEquals(maxMatch('ewingsa'),['e','w','in','g','s','a']);//'ewingsa' is not a valid word
Test.assertDeepEquals(maxMatch('gobbledygook'), ['go', 'b', 'b', 'l', 'e', 'd', 'y', 'go', 'o', 'k']);

// Top Answer
function maxMatch(text) {

  for (let i = text.length; i > 0; i--)

    if (i === 1 || VALID_WORDS.has(text.slice(0, i)))

      return [ text.slice(0, i) ].concat(maxMatch(text.slice(i)));

  return [];

}