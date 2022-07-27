#pragma once
#include "SortedBag.h"

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	const SortedBag& bag;
	SortedBagIterator(const SortedBag& b);

	int length, index, key;
    TElem *array;

public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();

    ///Extra operation
    ///changes the current element from the iterator to the previous element, or, if the current element was the first,
    ///makes the iterator invalid
    ///throws an exception if the iterator is invalid
    void previous();
};

