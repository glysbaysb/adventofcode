#include <iostream>
#include <fstream>
#include <cassert>

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto total = 0;
	while(std::getline(f, line)) {
		auto totalLength = line.length();
		auto inMemLength = 0;
		for(auto i = 1; i < line.length() - 1; i++) {
			if(line[i] == '\\') {
				inMemLength++;

				switch(line[i + 1]) {
				case 'x':
					i += 3;
					break;
				case '"':
				case '\\':
					i += 1;
					break;
				default:
					std::cerr << line << "\t" << line[i] << line[i+1] << std::endl;
					assert(false);
				}
				continue;
			}

			inMemLength++;
		}

		total += (totalLength - inMemLength);
	}

	std::cout << total << std::endl;
	return 0;
}

