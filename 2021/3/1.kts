import java.io.File
import java.io.BufferedReader

val lineList = mutableListOf<String>()

File("input").useLines { lines -> lines.forEach { lineList.add(it) }}

var count = arrayOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
//var count = arrayOf(0, 0, 0, 0, 0)
lineList.forEach {
	for(i in 0..it.length-1) {
		if(it[i] == '1') {
			count[i]++;
		}
	}
}

var gamma = 0
var epsilon = 0
for(i in 11 downTo 0) {
//for(i in 4 downTo 0) {
	if(count[11-i] > lineList.size / 2) {
		gamma = gamma + (1 shl i)
	} else {
		epsilon += 1 shl i
	}
}
println(gamma * epsilon)
