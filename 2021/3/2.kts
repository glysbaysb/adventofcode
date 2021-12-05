import java.io.File
import java.io.BufferedReader

val lineList = mutableListOf<String>()

File("input").useLines { lines -> lines.forEach { lineList.add(it) }}

//var count = arrayOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
fun mostCommonInPosition(lines: List<String>, pos: Int): Int {
	var cnt1 = 0
	var cnt0 = 0
	lines.forEach {
		if(it[pos] == '1') {
			cnt1++;
		} else {
			cnt0++
		}
	}

	if(cnt0 == cnt1) {
		return 1
	}
	else return if(cnt1 > cnt0) { 1 } else { 0 }
}
fun leastCommonInPosition(lines: List<String>, pos: Int): Int {
	var cnt1 = 0
	var cnt0 = 0
	lines.forEach {
		if(it[pos] == '1') {
			cnt1++;
		} else {
			cnt0++
		}
	}

	if(cnt0 == cnt1) {
		return 0
	}
	else return if(cnt1 > cnt0) { 0 } else { 1 }
}

// oxygen
var oxyCpy = lineList.toMutableList()
var pos = 0
while (oxyCpy.size > 1) {
	val mc = mostCommonInPosition(oxyCpy, pos)
	oxyCpy.retainAll { (it[pos] - '0').toInt() == mc }
	pos++
}
println(oxyCpy[0])

// co2
var co2Cpy = lineList.toMutableList()
var posCo2 = 0
while (co2Cpy.size > 1) {
	val lc = leastCommonInPosition(co2Cpy, posCo2)
	co2Cpy.retainAll { (it[posCo2] - '0').toInt() == lc }
	posCo2++
}
println(co2Cpy[0])

println(co2Cpy[0].toInt(2) * oxyCpy[0].toInt(2))
