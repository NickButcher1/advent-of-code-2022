package aoc2022

/**
 * Subclass Solver for each day.
 */
abstract class Solver(
    protected val inputLines: List<String>,
    protected val isPartTwo: Boolean = false
) {
    abstract fun solve1(): String

    abstract fun solve2(): String
}
