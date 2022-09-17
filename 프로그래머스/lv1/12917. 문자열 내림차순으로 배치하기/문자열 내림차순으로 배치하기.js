function solution(s) {
    return s.split('').sort((a, b) => {
        if(a < b) return 1;
        else return -1;
    }).join('')
}