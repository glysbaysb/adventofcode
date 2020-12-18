#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include "range/v3/view/cartesian_product.hpp"
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

		const auto allPairs = ranges::views::cartesian_product(columns, columns);
		/*const auto it = std::find_if(columns.begin(), columns.end(), [](const std::pair<int, int>& x) {
					const auto[a, b] = x;
					return a % b == 0;
				});
		std::cout << it << ' ' << *it << std::endl;*/
		std::cout << allPairs[0] << std::endl;
		//total += (it.first) / (it.second);

	}

	std::cout << total << std::endl;
}

