#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
	std::ifstream f(argv[1]);
	std::string line;

	auto total = 0;
	while(std::getline(f, line)) {
		std::vector<int> captcha;
		std::transform(line.begin(), line.end(), std::back_inserter(captcha),
				[](char c) -> int {
					return (c - '0');
				});

		const int jumpLength = captcha.size() / 2;

		auto sum = 0;
		for(auto i = 0; i < captcha.size(); i++) {
			if(captcha[i] == captcha[(i + jumpLength) % captcha.size()]) {
				sum += captcha[i];
			}
		}

		if(captcha[captcha.size() - 1] == captcha[jumpLength]) {
			sum += captcha[jumpLength];
		}

		std::cout << sum;
	}
}

