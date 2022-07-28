#include <vector>
#include <string>
#include <sstream>

std::vector<std::string> tokenize(std::string string, char delimiter)
{
    std::vector<std::string> result{};
    std::stringstream ss{string};
    std::string token{};
    while(std::getline(ss, token, delimiter))
        result.push_back(token);

    return result;
}