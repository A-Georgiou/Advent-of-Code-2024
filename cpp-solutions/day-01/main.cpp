#include <iostream>
#include <fstream>
#include <vector>

void solve(const std::vector<std::string>& input) {
    for (const auto& line : input) {
        std::cout << line << std::endl;
    }
}

int main() {
    std::ifstream inputFile("input.txt");
    if (!inputFile) {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    // Read the input lines into a vector
    std::vector<std::string> input;
    std::string line;
    while (std::getline(inputFile, line)) {
        input.push_back(line);
    }

    // Call the solve function
    solve(input);

    return 0;
}