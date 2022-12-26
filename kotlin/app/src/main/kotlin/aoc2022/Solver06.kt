package aoc2022

class Solver06(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {

    private fun isUnique(input: String): Boolean {
        val map = mutableMapOf<Char, Int>()

        for (i in input.indices) {
            if (map[input[i]] == 1) {
                return false
            } else {
                map[input[i]] = 1
            }
        }

        return true
    }

    private fun solveCommon(idx: Int): Any {
        inputLines.forEach { line ->
            for (i in line.indices) {
                val subst = line.substring(i, i + idx)
                if (isUnique(subst)) {
                    return i + idx
                }
            }
        }
        return -1 // Never reached.
    }

    override fun solve1(): Any = solveCommon(4)

    override fun solve2(): Any = solveCommon(14)
}
