#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <boost/tokenizer.hpp>

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto total = 0;
	while(std::getline(f, line)) {
		std::vector<int> columns;
		boost::tokenizer<> tok(line);

		std::for_each(tok.begin(), tok.end(), [&columns](const std::string& s) {
				std::size_t pos;
				columns.push_back(std::stoi(s, &pos, 10));
			});

		for(auto i = 0; i < columns.size(); i++) {
			for(auto j = 0; j < columns.size(); j++) {
				if(i == j) { continue; } // don't try a number with itself

				if(columns[i] % columns[j] == 0) {
					total += columns[i] / columns[j];
					break;
				}
			}
		}

	}

	std::cout << total << std::endl;
}

