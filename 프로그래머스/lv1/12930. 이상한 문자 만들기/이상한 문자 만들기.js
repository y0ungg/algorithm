function solution(s) {
    let result = [];
    let now = 0;
    for(let i=0; i< s.length; i++) {
        if(s[i] === ' ') {
            result.push(' ');
            now = 0;
            continue;
        }
        else{
            now % 2 === 0
                ? result.push(s[i].toUpperCase())
            : result.push(s[i].toLowerCase())
            now += 1
        }
    }
    return result.join('')
}