const assesDay = (steps, goal = 10000) => {
    if (steps >= goal) return "HIT";
    return "MISS";
};
console.log("\nGoal assesment:");
const stepLog = [9800, 11400, 6300, 10050];
for(const steps of stepLog){
    console.log(`${steps.toLocaleString()}---> ${assesDay(steps)}`);
}
const weekSummary = (stepsArray) =>{
    const total = stepsArray.reduce((sum, steps) => sum + steps, 0);
    const average = total / stepsArray.length;
    const hitCount = stepsArray.filter(steps => steps >= 10000).length;
    return {total, average, hitCount };
};

console.log("\n Week summary:", weekSummary(stepLog));
console.log("Hello world, come tommorrow okay, good.");

