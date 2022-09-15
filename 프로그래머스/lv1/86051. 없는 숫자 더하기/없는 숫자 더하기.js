function solution(numbers) {
    const nums = "0123456789";
    let result = 0;
    
    for(let i of nums) {
        if (numbers.findIndex(el => el === +i) < 0) { 
            result += +i;
        }
    }

    return result;
}