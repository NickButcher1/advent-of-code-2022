package aoc2022

import java.io.File

class App {
    fun runOneSolver(day: Int, useRealInput: Boolean): Long {
        val startTimeMs = System.currentTimeMillis()

        val inputFileName = "../../input/input%02d${if (!useRealInput) {"-sample"} else { "" }}".format(day)
        val inputLines = File(inputFileName).useLines { it.toList()  }

        val cls = Class.forName("aoc2022.Solver%02d".format(day))
        val output1 = (cls.constructors[0].newInstance(inputLines, false) as Solver).solve1()
        val output2 = (cls.constructors[0].newInstance(inputLines,  true) as Solver).solve2()

        // TODO compare outputs with expected outputs

        val timeTakenMs = System.currentTimeMillis() - startTimeMs
        print("Day $day ${timeTakenMs}ms\n$output1\n$output2\n")
        return timeTakenMs
    }
}

/**
 * Command line parameters:
 * 1  Day number.
 * 2  Optional. Any value to use sample input instead of real input.
 */
fun main(args: Array<String>) {
    val useRealInput = args.size == 1

    if (args[0] == "all") {
        var totalTimeTakenMs = 0L

        for (day in 1..26) {
            totalTimeTakenMs += App().runOneSolver(day, useRealInput)
        }

        print("Total time: ${totalTimeTakenMs}ms\n")

    } else {
        App().runOneSolver(args[0].toInt(), useRealInput)
    }
}
