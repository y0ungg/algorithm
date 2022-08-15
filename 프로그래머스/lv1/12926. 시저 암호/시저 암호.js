function solution(s, n) {
    const alphabet = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'];
    let result = "";
    for(let i = 0; i < s.length; i++) {
        if(s[i] === " ") {
            result += " ";
            continue;
        };
        let idx = alphabet.findIndex(v => v === s[i]);
        idx+(n*2) >= 52
        ? result += alphabet[idx+(n*2) - 52]
        : result += alphabet[idx+(n*2)];
    }
    return result;
}