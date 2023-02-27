const canSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(false);
    table[0] = true;
    for (let i = 0; i <= targetSum; i++){
        if (table[i] === true) {
            for (let num of numbers){
                table[i + num] = true;
                if (table[targetSum] === true) return true;
            }
        }
    }
    
    return table[targetSum];
};


console.log(canSum(7, [5, 3, 4, 7]));
console.log(canSum(7, [4, 2]));
console.log(canSum(8, [2, 3, 5]));
console.log(canSum(300, [7, 14]));