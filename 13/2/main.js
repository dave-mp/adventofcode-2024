const fs = require("fs");

function gcd(a, b) {
  a = BigInt(a);
  b = BigInt(b);
  while (b !== 0n) {
    [a, b] = [b, a % b];
  }
  return a;
}

function leastExpensivePath(a, b, p) {
  const costA = 3n;
  const costB = 1n;

  // Convert all inputs to BigInt
  a = a.map(BigInt);
  b = b.map(BigInt);
  p = p.map(BigInt);

  // Add 10^13 to each coordinate of the prize
  const offset = 10000000000000n;
  p = p.map((coord) => coord + offset);

  // Check if the goal is reachable
  const gcdX = gcd(a[0], b[0]);
  const gcdY = gcd(a[1], b[1]);
  const gcdA = gcd(a[0], a[1]);
  const gcdB = gcd(b[0], b[1]);

  if (
    (p[0] % gcdX !== 0n || p[1] % gcdY !== 0n) &&
    (p[0] % gcdA !== 0n || p[1] % gcdA !== 0n) &&
    (p[0] % gcdB !== 0n || p[1] % gcdB !== 0n)
  ) {
    return null; // Goal is not reachable
  }

  // Calculate coefficients for the Diophantine equation
  const det = a[0] * b[1] - a[1] * b[0];

  // Handle the case when det is 0 (parallel vectors)
  if (det === 0n) {
    // Check if the goal is along the direction of either vector
    if (p[0] * a[1] === p[1] * a[0]) {
      const x = p[0] / a[0];
      return x * costA;
    }
    if (p[0] * b[1] === p[1] * b[0]) {
      const y = p[0] / b[0];
      return y * costB;
    }
    return null; // Goal is not reachable with parallel vectors
  }

  const x1 = b[1] * p[0] - b[0] * p[1];
  const y1 = -a[1] * p[0] + a[0] * p[1];

  // Use extended Euclidean algorithm to find the solution
  const [g, x, y] = extendedEuclidean(det, b[0]);
  if (x1 % g !== 0n || y1 % g !== 0n) {
    return null; // No integer solution exists
  }

  let xBase = (x * (x1 / g)) % (det / g);
  let yBase = (y1 - xBase * b[0]) / det;

  // Adjust the solution to be non-negative with minimum cost
  const k = -BigInt(Math.min(Number(xBase / b[1]), Number(yBase / a[1])));
  xBase += k * b[1];
  yBase += k * a[1];

  // Ensure x and y are non-negative
  xBase = xBase < 0n ? 0n : xBase;
  yBase = yBase < 0n ? 0n : yBase;

  // Calculate the cost
  const cost = xBase * costA + yBase * costB;

  return cost;
}

function extendedEuclidean(a, b) {
  if (b === 0n) {
    return [a, 1n, 0n];
  } else {
    const [g, x, y] = extendedEuclidean(b, a % b);
    return [g, y, x - (a / b) * y];
  }
}

function parseInput(input) {
  const lines = input.split("\n").filter((line) => line.trim() !== "");
  const machinesConfig = [];

  for (let i = 0; i < lines.length; i += 3) {
    const [a, b, prize] = lines.slice(i, i + 3);
    const parseCoords = (str) => str.match(/[-\d]+/g).map(Number);

    machinesConfig.push({
      a: parseCoords(a),
      b: parseCoords(b),
      prize: parseCoords(prize),
    });
  }

  return machinesConfig;
}

function calculateFewestTokens(machinesConfig) {
  let fewestTokens = 0n;
  const totalMachines = machinesConfig.length;

  for (let i = 0; i < totalMachines; i++) {
    const mc = machinesConfig[i];
    const result = leastExpensivePath(mc.a, mc.b, mc.prize);

    if (result !== null) {
      fewestTokens += result;
    }

    // Update progress
    const progress = (((i + 1) / totalMachines) * 100).toFixed(2);
    process.stdout.write(
      `\rProgress: ${progress}% (${i + 1}/${totalMachines})`
    );
  }

  process.stdout.write("\n"); // New line after progress bar
  return fewestTokens;
}

// Read and parse input file
const input = fs.readFileSync("input.txt", "utf8");
const machinesConfig = parseInput(input);

console.time("Execution Time");
const fewestTokens = calculateFewestTokens(machinesConfig);
console.timeEnd("Execution Time");

console.log(`Fewest tokens: ${fewestTokens.toString()}`);
