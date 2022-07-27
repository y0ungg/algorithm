function solution(n) {
    let arr = n.toString().split('').sort((a,b) => b-a)
    return Number(arr.join(''))
}