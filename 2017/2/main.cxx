#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <boost/tokenizer.hpp>

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto checksum = 0;
	while(std::getline(f, line)) {
		std::vector<int> columns;
		boost::tokenizer<> tok(line);

		std::for_each(tok.begin(), tok.end(), [&columns](const std::string& s) {
				std::size_t pos;
				columns.push_back(std::stoi(s, &pos, 10));
			});

		const auto[min, max] = std::minmax_element(columns.begin(), columns.end());
		checksum += (*max - *min);
	}

	std::cout << checksum << std::endl;
}

