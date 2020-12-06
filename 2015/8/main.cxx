#include <iostream>
#include <fstream>
#include <cassert>

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto total = 0;
	while(std::getline(f, line)) {
		auto totalLength = line.length();
		auto encodedLength = 2; // start and end "
		for(auto i = 0; i < line.length(); i++) {
			switch(line[i]) {
			case '"':
			case '\\':
				encodedLength += 2;
				break;
			default:
				encodedLength += 1;
			}
		}

		total += (encodedLength - totalLength);
	}

	std::cout << total << std::endl;
	return 0;
}

