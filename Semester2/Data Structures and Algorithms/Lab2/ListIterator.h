#pragma once
#include "SortedIndexedList.h"
class SortedIndexedList;

//DO NOT CHANGE THIS PART
class ListIterator{
	friend class SortedIndexedList;
private:

	const SortedIndexedList& list;
	ListIterator(const SortedIndexedList& list);
    SortedIndexedList::Node* currentNode;



public:
	void first();
	void next();
	bool valid() const;
    TComp getCurrent() const;
};


