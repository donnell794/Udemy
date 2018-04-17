// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
  var r_str = "";
  for(var i = str.length; i >= 0; i--){
    r_str +=  str.charAt(i);
  }
  return r_str;
}

module.exports = reverse;
