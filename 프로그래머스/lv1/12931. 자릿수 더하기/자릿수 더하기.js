function solution(n){
    const nums = n.toString().split('').map(v => Number(v));
    const result = nums.reduce((acc, cur) => {return acc + cur});
    return result;
}