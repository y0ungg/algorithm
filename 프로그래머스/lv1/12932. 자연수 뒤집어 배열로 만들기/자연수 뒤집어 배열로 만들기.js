function solution(n) {
    const result = [];
    let str = n.toString();
    
    for(let i=str.length-1; i>=0; i--) {
        result.push(Number(str[i]));
    }
    
    return result;
}