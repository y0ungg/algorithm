//arr1[0][0] + arr2[0][0] = result[0][0]
function solution(arr1, arr2) {
    let answer = [];
    for(let i=0; i < arr1.length; i++) {
        let ele =[];
        for(let j=0; j < arr1[i].length; j++) {
            ele.push(arr1[i][j] + arr2[i][j])
        }
        answer.push(ele)
    }
    return answer;
}
