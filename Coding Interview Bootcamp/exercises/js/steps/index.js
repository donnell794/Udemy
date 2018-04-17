// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

function steps(n) {
  for(var i = 0; i < n; i++){
    var str = "";
    for(var k = 0; k < n; k++){
      if (k > i){
        str += ' ';
      }else{
        str += '#'
      }
    }
    console.log(str);
  }
}
/*
recursive solution
function steps(n, row = 0, stair = ''){
  if(row === n){
    return;
  }
  if (stair.length === n){
    console.log(stair);
    return steps(n, row +1);
  }
  if(stair.length <= row){
    stair += '#';
  }
  else{
    stair += ' ';
  }
  steps(n, row, stair)
}
*/
module.exports = steps;
