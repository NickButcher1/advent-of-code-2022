package aoc2022

public class Solver01(
    inputLines: List<String>,
    isPartTwo: Boolean = false
): Solver(inputLines, isPartTwo) {
    override fun solve1(): String {
        var currentSum = 0
        var maxSum = 0

        inputLines.forEach { line ->
            if (line.isEmpty()) {
                if (currentSum > maxSum) {
                    maxSum = currentSum
                }
                currentSum = 0
            } else {
                currentSum += line.toInt()
            }
        }

        return maxSum.toString()
    }

    override fun solve2(): String {
        return "-1"
    }
}
