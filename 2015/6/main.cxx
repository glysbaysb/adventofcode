#include <iostream>
#include <fstream>
#include <cassert>

int main(int argc, char** argv) {
	int arr[1000][1000] = {0};

	std::ifstream f(argv[1]);
	std::string line;

	while(std::getline(f, line)) {
		if(line.find("toggle ") == 0) {
			auto bx = std::stoi(line.substr(std::string("toggle ").length(), line.find(",")));
			auto by = std::stoi(line.substr(line.find(",") + 1, line.find(" ", line.find(","))));

			auto ux = std::stoi(line.substr(line.find("through ") + std::string("through ").length(), line.rfind(",")));
			auto uy = std::stoi(line.substr(line.rfind(",") + 1));

			assert(bx < ux);
			assert(by < uy);

			for(auto x = bx; x <= ux; x++) {
				for(auto y = by; y <= uy; y++) {
					arr[x][y] += 2;
				}
			}
		} else if (line.find("turn on ") == 0) {
			auto bx = std::stoi(line.substr(std::string("turn on ").length(), line.find(",")));
			auto by = std::stoi(line.substr(line.find(",") + 1, line.find(" ", line.find(","))));

			auto ux = std::stoi(line.substr(line.find("through ") + std::string("through ").length(), line.rfind(",")));
			auto uy = std::stoi(line.substr(line.rfind(",") + 1));

			assert(bx < ux);
			assert(by < uy);
			for(auto x = bx; x <= ux; x++) {
				for(auto y = by; y <= uy; y++) {
					arr[x][y] += 1;
				}
			}
		} else if (line.find("turn off ") == 0) {
			auto bx = std::stoi(line.substr(std::string("turn off").length(), line.find(",")));
			auto by = std::stoi(line.substr(line.find(",") + 1, line.find(" ", line.find(","))));

			auto ux = std::stoi(line.substr(line.find("through ") + std::string("through ").length(), line.rfind(",")));
			auto uy = std::stoi(line.substr(line.rfind(",") + 1));

			assert(bx < ux);
			assert(by < uy);
			for(auto x = bx; x <= ux; x++) {
				for(auto y = by; y <= uy; y++) {
					arr[x][y] = std::max(0, arr[x][y] - 1);
				}
			}
		}
	}

	auto sum = 0;
	for(auto x = 0; x < 1000; x++) {
		for(auto y = 0; y < 1000; y++) {
			sum += arr[x][y];
		}
	}

	std::cout << sum << std::endl;
	return 0;
}
