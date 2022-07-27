#include "comparator.h"


bool ComparatorAscendingByLikes::compare(Movie first, Movie second) {
    if (first.getNumberOfLikes()>second.getNumberOfLikes())
        return false;
    return true;
}



bool ComparatorAscendingByGenre::compare(Movie first, Movie second) {
    if (first.getGenre()>second.getGenre())
        return false;
    return true;
}


