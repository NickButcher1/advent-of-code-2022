package aoc2022

class Solver03(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    override fun solve1(): Any {
        var score = 0

        inputLines.forEach { line ->
            val fullLineLen = line.length
            val halfLineLen = fullLineLen / 2

            val string1 = line.substring(0, halfLineLen)
            val string2 = line.substring(halfLineLen, fullLineLen)

            ASCII_LETTERS.forEachIndexed { index, char ->
                if (string1.contains(char) and string2.contains(char)) {
                    score += index + 1
                }
            }
        }

        return score
    }

    override fun solve2(): Any {
        var score = 0
        val rucksacks = mutableListOf<String>()

        inputLines.forEach { line -> rucksacks.add(line) }

        for (i in 0 until rucksacks.size step 3) {
            ASCII_LETTERS.forEachIndexed { index, char ->
                if (
                    rucksacks[i].contains(char) &&
                    rucksacks[i + 1].contains(char) &&
                    rucksacks[i + 2].contains(char)
                ) {
                    score += index + 1
                }
            }
        }

        return score
    }
}
