package aoc2022

class Solver04(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    private fun solveCommon(): Int {
        var score = 0
        inputLines.forEach { line ->
            val splitLine = line.split(",")
            val oneStart = splitLine[0].split("-")[0].toInt()
            val oneEnd = splitLine[0].split("-")[1].toInt()
            val twoStart = splitLine[1].split("-")[0].toInt()
            val twoEnd = splitLine[1].split("-")[1].toInt()

            if (isPartTwo) {
                if (oneStart < twoStart) {
                    if (oneEnd >= twoStart) {
                        score += 1
                    }
                } else if (oneStart > twoStart) {
                    if (twoEnd >= oneStart) {
                        score += 1
                    }
                } else {
                    score += 1
                }
            } else {
                if (oneStart >= twoStart && oneEnd <= twoEnd) {
                    score += 1
                } else if (twoStart >= oneStart && twoEnd <= oneEnd) {
                    score += 1
                }
            }
        }
        return score
    }

    override fun solve1(): Any = solveCommon()

    override fun solve2(): Any = solveCommon()
}
