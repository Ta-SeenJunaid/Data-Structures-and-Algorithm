const countConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill(false);
    table[0] = true;

    for (let i = 0; i <= target.length; i++){
        if (table[i] === true){
            for (let word of wordBank){
                if(target.slice(i, i + word.length) === word){
                    table[i + word.length] = true;
                    if (table[target.length] === true) return true
                }
            }
        }
    }
    return table[target.length]
};


console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']));
console.log(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee"
]));