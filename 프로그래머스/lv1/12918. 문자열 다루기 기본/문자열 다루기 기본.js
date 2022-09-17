//10e1과 같은 경우 생각하기
//typeof NaN은 number이다!
function solution(s) {
    if(s.length === 4 || s.length === 6) {
        return s.split('').every(el => !isNaN(el));
    }
    return false;
}