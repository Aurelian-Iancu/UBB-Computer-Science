#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <iostream>
#include <exception>

using namespace std;

ListIterator::ListIterator(const SortedIndexedList& list) : list(list) {
	this->currentNode = list.head;
}
///theta(1)

void ListIterator::first(){
    this->currentNode = this->list.head;
}
///theta(1)

void ListIterator::next(){
	if(this->currentNode != nullptr)
    {
        this->currentNode = this->currentNode->next;
    }
    else
        throw exception();
}
///theta(1)

bool ListIterator::valid() const{
	if(this->currentNode == nullptr)
        return false;
    return true;
}
///theta(1)

TComp ListIterator::getCurrent() const{
    if(this->currentNode == nullptr)
        throw exception();
    return this->currentNode->info;
}
///theta(1)


