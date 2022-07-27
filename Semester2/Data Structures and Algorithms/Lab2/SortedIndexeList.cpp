#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <iostream>
using namespace std;
#include <exception>

SortedIndexedList::SortedIndexedList(Relation r) {
	this->relation = r;
    this->length = 0;
    this->head = nullptr;
    this->tail = nullptr;
}
///theta(1)

int SortedIndexedList::size() const {
	return this->length;
}
///theta(1)

bool SortedIndexedList::isEmpty() const {
	if (this->length == 0)
        return true;
    return false;
}
///theta(1)

TComp SortedIndexedList::getElement(int i) const{
	Node* currentNode = this->head;
    int index = 0;
    while(currentNode != nullptr)
    {
        if(index == i)
            return currentNode->info;
        currentNode = currentNode->next;
        index++;
    }

    throw exception();

}
///BC: Theta(1), WC:Theta(nrNodes), Total: O(nrNodes)

TComp SortedIndexedList::remove(int i) {
    Node* currentNode = this->head;
    TComp nodeValue;
    int index;
    if(this->length == 0 || i < 0 || i >= this->length)
        throw exception();
    else {
        for (index = 0; index < i; index++)
            currentNode = currentNode->next;
        nodeValue = currentNode->info;
        this->length--;
        if(currentNode == this->head)
            this->head = currentNode->next;

        if(currentNode->next != nullptr)
            currentNode->next->prev = currentNode->prev;

        if(currentNode->prev != nullptr)
            currentNode->prev->next = currentNode->next;

        delete currentNode;

    }
    return nodeValue;
}
///BC: Theta(1) WC: Theta(nrNodes), Total:O(nrNodes)

int SortedIndexedList::search(TComp e) const {
	Node* currentNode = this->head;
    int index = 0;
    int foundIndex = -1;
    while(currentNode != nullptr && this->relation(currentNode->info, e) && foundIndex == -1)
    {
        if(currentNode->info == e)
            foundIndex = index;
        else {
            currentNode = currentNode->next;
            index++;
        }
    }
    return foundIndex;
}
///BC: Theta(1) WC: Theta(nrNodes), Total:O(nrNodes)

void SortedIndexedList::add(TComp e) {
	if(this->length == 0)
    {
        Node* newNode = new Node();
        newNode->info = e;
        newNode->next = nullptr;
        newNode->prev = nullptr;
        this->head = newNode;
        this->tail = newNode;
        this->length++;
    }
    else
    {
        Node *currentNode = this->head;
        while(currentNode != nullptr && this->relation(currentNode->info, e))
            currentNode = currentNode->next;

        if(currentNode == this->head && currentNode != nullptr)
        {
            Node *newNode = new Node();
            newNode->info = e;
            newNode->prev = nullptr;
            newNode->next = currentNode;
            currentNode->prev = newNode;
            this->head = newNode;
            this->length++;
        }
        else if(currentNode == nullptr)
        {
            Node* newNode = new Node();
            newNode->info = e;
            newNode->next = currentNode;
            newNode->prev = this->tail;
            this->tail->next = newNode;
            this->tail = newNode;
            this->length++;
        }
        else
        {
            Node *newNode = new Node();
            newNode->info = e;
            newNode->prev = currentNode->prev;
            newNode->next = currentNode;
            currentNode->prev->next = newNode;
            currentNode->prev = newNode;
            this->length++;
        }

    }
}
///BC: Theta(1) WC: Theta(nrNodes), Total:O(nrNodes)

ListIterator SortedIndexedList::iterator(){
	return ListIterator(*this);
}
///theta(1)

//destructor
SortedIndexedList::~SortedIndexedList() {
    Node* prevNode = nullptr;
    Node* currentNode = this->head;
    while (currentNode != nullptr) {
        prevNode = currentNode;
        currentNode = currentNode->next;
        delete prevNode;
    }
}
///theta(nrNodes)

///EXTRA OPERATION
int SortedIndexedList::lastIndexOf(TComp e) const {
    Node* currentNode = this->head;
    int index = 0;
    int foundIndex = -1;
    int indexLast = -1;
    while(currentNode != nullptr && this->relation(currentNode->info, e) && foundIndex == -1)
    {
        if(currentNode->info == e) {
            foundIndex = index;
            indexLast = index;
        }
        else {
            currentNode = currentNode->next;
            index++;
        }
    }

    if(indexLast != -1)
    {
        while(currentNode != nullptr && currentNode->info == e )
        {
            indexLast++;
            currentNode = currentNode->next;
        }
        indexLast --;
    }
    return indexLast;

}
//////BC: Theta(1) WC: Theta(nrNodes), Total:O(nrNodes)

