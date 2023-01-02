package aoc2022

class Solver05(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    /**
     * [G] [D] [R]
     * [W] [V] [C] [T] [M]
     * [L] [P] [Z] [Q] [F] [V]
     * [J] [S] [D] [J] [M] [T] [V]
     * [B] [M] [H] [L] [Z] [J] [B] [S]
     * [R] [C] [T] [C] [T] [R] [D] [R] [D]
     * [T] [W] [Z] [T] [P] [B] [B] [H] [P]
     * [D] [S] [R] [D] [G] [F] [S] [L] [Q]
     *  1   2   3   4   5   6   7   8   9
     */
    private val stacks: List<MutableList<Char>> = listOf(
        mutableListOf(),
        mutableListOf('G', 'W', 'L', 'J', 'B', 'R', 'T', 'D'),
        mutableListOf('C', 'W', 'S'),
        mutableListOf('M', 'T', 'Z', 'R'),
        mutableListOf('V', 'P', 'S', 'H', 'C', 'T', 'D'),
        mutableListOf('Z', 'D', 'L', 'T', 'P', 'G'),
        mutableListOf('D', 'C', 'Q', 'J', 'Z', 'R', 'B', 'F'),
        mutableListOf('R', 'T', 'F', 'M', 'J', 'D', 'B', 'S'),
        mutableListOf('M', 'V', 'T', 'B', 'R', 'H', 'L'),
        mutableListOf('V', 'S', 'D', 'P', 'Q')
    )

    private fun solveCommon(): String {
        inputLines.forEach { line ->
            val splitLine = line.split(" ")
            val moveNumber = splitLine[1].toInt()
            val moveFrom = splitLine[3].toInt()
            val moveTo = splitLine[5].toInt()

            if (isPartTwo) {
                val taken = mutableListOf<Char>()
                for (i in 0 until moveNumber) {
                    taken.add(stacks[moveFrom].removeAt(0))
                }
                taken.reverse()

                taken.forEach { item -> stacks[moveTo].add(0, item) }
            } else {
                for (i in 0 until moveNumber) {
                    val taken = stacks[moveFrom].removeAt(0)
                    stacks[moveTo].add(0, taken)
                }
            }
        }

        var output = ""
        for (i in 1..9) {
            output += stacks[i][0]
        }

        return output
    }

    override fun solve1(): Any = solveCommon()

    override fun solve2(): Any = solveCommon()
}
