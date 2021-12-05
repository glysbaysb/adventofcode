import java.io.File
import java.io.BufferedReader

val lineList = mutableListOf<String>()

File("input").useLines { lines -> lines.forEach { lineList.add(it) }}
println("heyyyy")

var x = 0;
var y = 0;
lineList.forEach {
	val tmp = it.split(' ')
	val byHowMuch = tmp[1].toInt()
	if(it.startsWith("forward")) {
		x += byHowMuch
	} else if(it.startsWith("down")) {
		y += byHowMuch
	} else {
		y -= byHowMuch
	}
}
println("${x}, ${y}, ${x*y}")
