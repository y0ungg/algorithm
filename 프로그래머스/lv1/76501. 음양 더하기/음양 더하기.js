function solution(absolutes, signs) {
    const nums = [];
    for(let i = 0; i < absolutes.length; i++) {
        if(signs[i]) nums.push(absolutes[i]);
        else {
            nums.push(-absolutes[i]);
        }
    }
    return nums.reduce((pre, cur) => pre + cur);
}