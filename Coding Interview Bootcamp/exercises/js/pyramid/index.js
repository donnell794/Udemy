// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'

function pyramid(n, row = 0, level = '') {
  if(row === n){
    return;
  }
  const max_width = n + n - 1;
  if(level.length === max_width){
    console.log(level);
    return pyramid(n, row + 1);
  }
  //width = n + n - 1
  const midpoint = Math.floor(max_width / 2);
  if(level.length >= midpoint - row && level.length <= midpoint + row){
    level += '#';
  }
  else{
    level += ' ';
  }
  pyramid(n, row, level);
}

module.exports = pyramid;
