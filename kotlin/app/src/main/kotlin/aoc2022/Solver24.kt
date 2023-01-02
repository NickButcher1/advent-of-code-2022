package aoc2022

class Solver24(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    private val numRows = inputLines.size
    private val numCols = inputLines[0].length

    private val startPos = Pair(0, inputLines[0].split(".")[0].length)
    private val targetPos = Pair(
        inputLines.size - 1,
        inputLines[inputLines.size - 1].split(".")[0].length
    )

    private var solvedPartA = false
    private var solvedPartB = false
    private var solvedPartC = false

    private var matrix: MutableList<MutableList<MutableList<Char>>> = initMatrix()

    private fun initMatrix(): MutableList<MutableList<MutableList<Char>>> {
        val matrix: MutableList<MutableList<MutableList<Char>>> = mutableListOf()

        for (rowIdx in 0 until numRows) {
            val row = mutableListOf<MutableList<Char>>()
            matrix.add(row)
            for (colIdx in 0 until numCols) {
                val content = inputLines[rowIdx][colIdx]
                val cellList = if (content == '.') {
                    mutableListOf()
                } else {
                    mutableListOf(content)
                }
                row.add(cellList)
            }
        }

        matrix[startPos.first][startPos.second] = mutableListOf('S')
        matrix[targetPos.first][targetPos.second] = mutableListOf('E')

        return matrix
    }
    private fun flowOneStep(): MutableList<MutableList<MutableList<Char>>> {
        val newMatrix: MutableList<MutableList<MutableList<Char>>> = mutableListOf()

        for (i in 0 until numRows) {
            val newRow: MutableList<MutableList<Char>> = mutableListOf()
            newMatrix.add(newRow)

            for (j in 0 until numCols) {
                newRow.add(mutableListOf())
            }
        }

        for (i in 0 until numRows) {
            for (j in 0 until numCols) {
                matrix[i][j].forEach { cellContent ->
                    when (cellContent) {
                        '<' -> {
                            val newJ = if (j == 1) {
                                numCols - 2
                            } else {
                                j - 1
                            }
                            newMatrix[i][newJ].add('<')
                        }

                        '>' -> {
                            val newJ = if (j == (numCols - 2)) {
                                1
                            } else {
                                j + 1
                            }
                            newMatrix[i][newJ].add('>')
                        }

                        '^' -> {
                            val newI = if (i == 1) {
                                numRows - 2
                            } else {
                                i - 1
                            }
                            newMatrix[newI][j].add('^')
                        }

                        'v' -> {
                            val newI = if (i == (numRows - 2)) {
                                1
                            } else {
                                i + 1
                            }
                            newMatrix[newI][j].add('v')
                        }

                        else -> newMatrix[i][j].add(cellContent)
                    }
                }
            }
        }

        matrix = newMatrix
        return matrix
    }

    private fun isValidMove(matrix: MutableList<MutableList<MutableList<Char>>>, i: Int, j: Int): Boolean =
        when {
            i == -1 -> false

            i == numRows -> false

            matrix[i][j] == mutableListOf('E') && (!solvedPartB || !solvedPartC) -> true

            matrix[i][j] == mutableListOf('S') && solvedPartA && !solvedPartB -> true

            i == 0 || j == 0 -> false

            i == (numRows - 1) || j == (numCols - 1) -> false

            matrix[i][j] == mutableListOf<Char>() -> true

            else -> false
        }

    private fun getValidMoves(matrix: MutableList<MutableList<MutableList<Char>>>, humanPos: Pair<Int, Int>): List<Pair<Int, Int>> {
        val validMoves = mutableListOf<Pair<Int, Int>>()

        if (isValidMove(matrix, humanPos.first - 1, humanPos.second)) {
            validMoves.add(Pair(humanPos.first - 1, humanPos.second))
        }

        if (isValidMove(matrix, humanPos.first + 1, humanPos.second)) {
            validMoves.add(Pair(humanPos.first + 1, humanPos.second))
        }

        if (isValidMove(matrix, humanPos.first, humanPos.second - 1)) {
            validMoves.add(Pair(humanPos.first, humanPos.second - 1))
        }

        if (isValidMove(matrix, humanPos.first, humanPos.second + 1)) {
            validMoves.add(Pair(humanPos.first, humanPos.second + 1))
        }

        // Wait in place.
        if (isValidMove(matrix, humanPos.first, humanPos.second)) {
            validMoves.add(Pair(humanPos.first, humanPos.second))
        } else if (humanPos.first == 0 && humanPos.second == 1) {
            validMoves.add(Pair(humanPos.first, humanPos.second))
        }

        return validMoves
    }

    private fun solveCommon(): Int {
        var currentTargetPos = targetPos
        var depth = 1
        var matrix = flowOneStep()
        var validMoves = getValidMoves(matrix, startPos)
        var newValidMoves: List<Pair<Int, Int>>

        while (true) {
            depth++
            matrix = flowOneStep()

            newValidMoves = mutableListOf()
            validMoves.forEach { move ->
                newValidMoves.addAll(getValidMoves(matrix, move))
            }

            // Remove duplicates.
            validMoves = newValidMoves.distinct()

            if (currentTargetPos in validMoves) {
                if (!isPartTwo) {
                    return depth
                } else if (!solvedPartA) {
                    solvedPartA = true
                    validMoves = mutableListOf(currentTargetPos)
                    currentTargetPos = startPos
                } else if (!solvedPartB) {
                    solvedPartB = true
                    validMoves = mutableListOf(currentTargetPos)
                    currentTargetPos = targetPos
                } else if (!solvedPartC) {
                    solvedPartC = true
                    return depth
                }
            }
        }
    }

    override fun solve1(): Any = solveCommon()

    override fun solve2(): Any = solveCommon()
}
