#include "validators.h"

ValidationException::ValidationException(std::string &_message): message(_message){}

const char* ValidationException::what() const noexcept {
    return message.c_str();
}

MovieValidator::MovieValidator() = default;


bool MovieValidator::validateString(const std::string &string) {
    for(auto i: string)
        if(std::isdigit(i) != false)
            return false;
    return true;
}

void MovieValidator::validateTitle(const std::string &title) {
    std::string errors;
    if(title.length() == 0)
        errors += std::string("The title is empty!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateGenre(const std::string &genre) {
    std::string errors;
    if(!validateString(genre))
        errors += std::string("The genre should not contain digits!");
    if(genre.length() == 0)
        errors += std::string("The genre is empty!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateYearString(const std::string &year) {
    std::string errors;
    if(year.empty())
        errors += std::string("The year should not be empty!");
    if(year.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The year has characters that are not digits!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateYear(int year) {
    std::string errors;
    if(year < 0)
        errors += std::string("The year should be a positive number!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateLikesString(const std::string &likes) {
    std::string errors;
    if(likes.empty())
        errors += std::string("The number of likes should not be empty!");
    if(likes.find_first_not_of("0123456789") != std::string::npos)
        errors += std::string("The year has characters that are not digits!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateYearLikes(int likes) {
    std::string errors;
    if(likes < 0)
        errors += std::string("The number of likes should be a positive number!");
    if(!errors.empty())
        throw ValidationException(errors);
}

void MovieValidator::validateTrailer(const std::string &trailer) {
    std::string errors;
    if(trailer.length() == 0)
        errors += std::string("The trailer should not be empty!");
    if(trailer.find("www") == std::string::npos)
        errors += std::string("The link is not valid");
    if(!errors.empty())
        throw ValidationException(errors);
}

MovieValidator::~MovieValidator() = default;


