#pragma once

#include "SortedMultiMap.h"
#include <stack>

class SMMIterator{
    friend class SortedMultiMap;
private:
    //DO NOT CHANGE THIS PART
    const SortedMultiMap& map;
    SMMIterator(const SortedMultiMap& map);
    std::stack<int> s;
    int currentPos;
    int currentValuePos;

public:
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};
