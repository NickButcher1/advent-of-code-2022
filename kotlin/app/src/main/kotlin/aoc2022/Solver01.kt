package aoc2022

public class Solver01(
    inputLines: List<String>,
    isPartTwo: Boolean = false
): Solver(inputLines, isPartTwo) {
    override fun solve1(): Any {
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

        return maxSum
    }

    override fun solve2(): Any {
        var currentSum = 0
        val maxSums = mutableListOf<Int>()

        inputLines.forEach { line ->
            if (line.isEmpty()) {
                maxSums.add(currentSum)
                currentSum = 0
            } else {
                currentSum += line.toInt()
            }
            maxSums.sortWith(reverseOrder())
        }
        return maxSums[0] + maxSums[1] + maxSums[2]
    }
}
