#include <iostream>
#include <fstream>
#include <cassert>
#include <array>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

bool countDuplicates(std::string str, int expectedForAny) {
	std::array<int, 26> count = {0};

	for(const auto c : str) {
		assert(islower(c));
		count[c - 'a']++;
	}

	return std::find(std::begin(count), std::end(count), expectedForAny) != std::end(count);
}

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::vector<std::string> allLines;
	std::string line;

	while(std::getline(f, line)) {
		allLines.push_back(line);
	}

	for(auto& id: allLines) {
		auto res = std::find_if(allLines.begin(), allLines.end(), [=](const std::string elem) {
				std::array<char, 26> difference = {0};
				assert(id.length() == elem.length() && id.length() == 26);

				for(auto i = 0; i < id.length(); i++) {
					difference[i] = (id[i] - elem[i]) != 0;
				}

				return std::accumulate(difference.begin(), difference.end(), 0) == 1;
			});
		if(res == std::end(allLines)) {
			continue;
		}

		std::cout << id << " ~ " << *res << std::endl;


		/*
		std::set<char> a(id.begin(), id.end());
		std::set<char> b((*res).begin(), (*res).end());
		std::string sharedCharacters;
		std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(sharedCharacters));

		std::cout << " --> "  << sharedCharacters << std::endl;
		*/
		const auto[ firstDiffIt, _ ] = std::mismatch(id.begin(), id.end(), (*res).begin(), (*res).end());
		id.erase(firstDiffIt);
		std::cout << id << std::endl;

		break;
	}
}

