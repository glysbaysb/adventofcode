#include <iostream>
#include <fstream>
#include <cassert>
#include <array>

bool countDuplicates(std::string str, int expectedForAny) {
	std::array<int, 26> count = {0};

	for(const auto c : str) {
		assert(islower(c));
		count[c - 'a']++;
	}

	for(const auto c: count) {
		if(c == expectedForAny) {
			return true;
		}
	}

	return false;
}

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto totalDouble = 0;
	auto totalTriple = 0;
	while(std::getline(f, line)) {
		totalDouble += countDuplicates(line, 2);
		totalTriple += countDuplicates(line, 3);
	}

	std::cout << totalDouble * totalTriple << std::endl;
}

