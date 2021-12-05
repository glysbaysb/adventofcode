import java.io.File
import java.io.BufferedReader

val lineList = mutableListOf<String>()

File("input_test").useLines { lines -> lines.forEach { lineList.add(it) }}
println("heyyyy")

var x = 0;
var y = 0;
var aim = 0;
lineList.forEach {
	val tmp = it.split(' ')
	val byHowMuch = tmp[1].toInt()
	if(it.startsWith("forward")) {
		x += byHowMuch
		y += aim * byHowMuch
	} else if(it.startsWith("down")) {
		aim += byHowMuch
	} else {
		aim -= byHowMuch
	}
}
println("${x}, ${y}, ${x*y}")

