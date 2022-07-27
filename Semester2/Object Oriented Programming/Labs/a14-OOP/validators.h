#pragma once

#include "movie.h"

class ValidationException: public std::exception{
private:
    std::string message;
public:
    explicit ValidationException(std::string& _message);

    const char *what() const noexcept override;
};

class MovieValidator{
public:
    MovieValidator();

    bool validateString(const std::string& string);

    void validateTitle(const std::string& title);

    void validateGenre(const std::string& genre);

    void validateYearString(const std::string& year);

    void validateYear(int year);

    void validateLikesString(const std::string& likes);

    void validateYearLikes(int likes);

    void validateTrailer(const std::string& trailer);

    ~MovieValidator();



};
