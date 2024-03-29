const howSum = (targetSum, numbers, memo={}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let num of numbers){
        const remainder = targetSum - num;
        const reminderResult = howSum(remainder, numbers, memo);
        if (reminderResult !== null){
            memo[targetSum] = [...reminderResult, num];
            return memo[targetSum]
        }
    }
    memo[targetSum] = null;
    return null;
};

console.log(howSum(7, [5, 3, 4, 7]));
console.log(howSum(7, [4, 2]));
console.log(howSum(8, [2, 3, 5]));
console.log(howSum(300, [7, 14]));