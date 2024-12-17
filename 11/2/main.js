function processStone(stone, count) {
  const strStone = stone.toString();
  if (strStone === "0") {
    return [[1n, count]];
  }
  if (strStone.length % 2 === 0) {
    const mid = Math.floor(strStone.length / 2);
    return [
      [BigInt(strStone.slice(0, mid)), count],
      [BigInt(strStone.slice(mid)), count],
    ];
  }
  return [[stone * 2024n, count]];
}

function blink(stoneMap) {
  const newStoneMap = new Map();
  for (const [stone, count] of stoneMap) {
    const processed = processStone(stone, count);
    for (const [newStone, newCount] of processed) {
      newStoneMap.set(newStone, (newStoneMap.get(newStone) || 0n) + newCount);
    }
  }
  return newStoneMap;
}

function countStones(initialStones, iterations) {
  let stoneMap = new Map(initialStones.map((stone) => [BigInt(stone), 1n]));
  for (let i = 0; i < iterations; i++) {
    stoneMap = blink(stoneMap);
  }
  return Array.from(stoneMap.values()).reduce((a, b) => a + b, 0n);
}

const initialStones = [4610211n, 4n, 0n, 59n, 3907n, 201586n, 929n, 33750n];
const iterations = 75;

console.time("Optimized version with BigInt");
const result = countStones(initialStones, iterations);
console.timeEnd("Optimized version with BigInt");

console.log(
  `Number of stones after ${iterations} iterations: ${result.toString()}`
);
