#pragma once
#include "movie.h"


template <typename Type> class Comparator{
public:
    virtual bool compare(Type first, Type second) = 0;
};

class ComparatorAscendingByLikes : public Comparator<Movie>{
    bool compare(Movie first, Movie second) override;
};


class ComparatorAscendingByGenre : public Comparator<Movie>{
public:
    bool compare(Movie first, Movie second) override;


};
