//풀이 1
function solution(arr) {
    if(arr.length <= 1) return [-1];
 
    let compare = arr[0];
  
    for(let i = 1; i < arr.length; i++) {
        if(compare >= arr[i]) {
            compare = arr[i];
        }
    }
    return arr.filter((el) => el !== compare);
}

//풀이 2
function solution(arr) {
    if(arr.length <= 1) return [-1];
    return arr.filter((el, idx, arr) => el !== Math.min(...arr));
}
