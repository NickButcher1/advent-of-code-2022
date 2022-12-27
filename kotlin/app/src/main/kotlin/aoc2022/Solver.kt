package aoc2022

/**
 * Subclass Solver for each day.
 */
abstract class Solver(
    protected val inputLines: List<String>,
    protected val isPartTwo: Boolean = false
) {
    abstract fun solve1(): Any

    abstract fun solve2(): Any

    companion object {
        @JvmStatic
        protected val ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

        @JvmStatic
        protected val ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        @JvmStatic
        protected val ASCII_LETTERS = ASCII_LOWERCASE + ASCII_UPPERCASE
    }
}
