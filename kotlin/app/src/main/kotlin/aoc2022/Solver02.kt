package aoc2022

public class Solver02(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    private val inputs = mutableListOf<String>()
    private fun readInput() {
        inputLines.forEach { line ->
            inputs.add(line[0].toString() + line[2].toString())
        }
    }
    private fun solveCommon(lookupTable: Map<String, Int>): Any {
        readInput()
        var score = 0
        inputs.forEach { input ->
            score += lookupTable[input]!!
        }
        return score
    }

    override fun solve1(): Any {
        val lookupTable = mapOf(
            // Rock
            "AX" to 1 + 3,
            "AY" to 2 + 6,
            "AZ" to 3 + 0,
            // Paper
            "BX" to 1 + 0,
            "BY" to 2 + 3,
            "BZ" to 3 + 6,
            // Scissors
            "CX" to 1 + 6,
            "CY" to 2 + 0,
            "CZ" to 3 + 3
        )

        return solveCommon(lookupTable)
    }

    override fun solve2(): Any {
        // X=lose, Y=draw, Z=win
        val lookupTable = mapOf(
            // Rock
            "AX" to 3 + 0,
            "AY" to 1 + 3,
            "AZ" to 2 + 6,
            // Paper
            "BX" to 1 + 0,
            "BY" to 2 + 3,
            "BZ" to 3 + 6,
            // Scissors
            "CX" to 2 + 0,
            "CY" to 3 + 3,
            "CZ" to 1 + 6
        )
        return solveCommon(lookupTable)
    }
}
