package aoc2022

class Solver25(
    inputLines: List<String>,
    isPartTwo: Boolean = false
) : Solver(inputLines, isPartTwo) {
    private fun decimalToSnafu(decimal: Long): String {
        var reverseOutput = ""
        var remainingDecimal = decimal

        while (remainingDecimal != 0L) {
            var remainder = remainingDecimal % 5
            remainingDecimal = (remainingDecimal / 5)

            if (remainder == 3L) {
                remainder = -2L
                remainingDecimal += 1
            } else if (remainder == 4L) {
                remainder = -1L
                remainingDecimal += 1
            }
            reverseOutput += LONG_TO_SNAFU[remainder]
        }

        return reverseOutput.reversed()
    }

    private fun snafuToDecimal(snafu: String): Long {
        var mult = 1L
        var sum = 0L

        snafu.reversed().forEach { snafuChar ->
            sum += SNAFU_TO_LONG[snafuChar]!! * mult
            mult *= 5
        }
        return sum
    }

    override fun solve1(): Any {
        var sum = 0L
        inputLines.forEach { line ->
            sum += snafuToDecimal(line.split(" ")[0])
        }

        return decimalToSnafu(sum)
    }

    /** There is no part two. */
    override fun solve2(): Any {
        return "-1"
    }

    companion object {
        private val LONG_TO_SNAFU = mapOf(
            -2L to "=",
            -1L to "-",
            0L to "0",
            1L to "1",
            2L to "2"
        )

        private val SNAFU_TO_LONG = mapOf(
            '=' to -2L,
            '-' to -1L,
            '0' to 0L,
            '1' to 1L,
            '2' to 2L
        )
    }
}
