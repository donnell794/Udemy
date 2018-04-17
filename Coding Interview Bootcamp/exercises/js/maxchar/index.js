// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
  const chars = {};
  var max = 0;
  var max_chr = '';
  for(let char of str){
    if (chars[char]){
      chars[char]++;
    }else{
      chars[char] = 1;
    }
  }
  for(let char in chars){
    if (chars[char] > max){
      max = chars[char];
      max_chr = char;
    }
  }
  debugger;
  return max_chr;
}
maxChar('this is this thing that');
module.exports = maxChar;
