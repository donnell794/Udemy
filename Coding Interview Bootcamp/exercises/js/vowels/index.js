// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
  /*regex answer
  const matches = str.match(/[aeiou]/gi);
  return matches ? matches.length : 0;
  */
  vowel_str = "aeiou";
  count = 0;
  for(let chr of str.toLowerCase()){
    if(vowel_str.includes(chr)){
      count++;
    }
  }
  return count;
}

module.exports = vowels;
