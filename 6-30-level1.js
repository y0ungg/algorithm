function solution(num) {
    const collatz = (num, count) => {
        //base case
        if(num === 1) return count;
        if(count >= 500) return -1;

        //recursive case
        if(num % 2 === 0) return collatz(num / 2, count+1)
        else {
            return collatz((num * 3) + 1, count + 1)
        }
    };

    return collatz(num, 0);
};
