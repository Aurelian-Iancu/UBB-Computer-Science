#include "SMMIterator.h"
#include "SortedMultiMap.h"

//Th(h) = Th(log n) for a balanced tree with n nodes


SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d), currentPos(map.rootPos), currentValuePos(0)
{

    if (map.treeLength == 0)
    {
        currentPos = -1;
        return;
    }

    //current pos is the root pos
    while (currentPos != -1) //while current pos is valid
    {
        s.push(currentPos);
        currentPos = map.lefts[currentPos];
    } //current pos is the left until no more lefts
    if (s.size() != 0)
    {
        currentPos = s.top();
        currentValuePos = 0;
    }
    //now current pos is the position of the leftmost element
    //if stack is empty then current pos is -1;
}
//BC = Th(1) in case of degenerated tree in the right
//WC = Th(h) in case of degenerated tree on the left for example (only need the leftmost to be lowest)

void SMMIterator::first(){

    if (map.treeLength == 0)
    {
        currentPos = -1;
        return;
    }

    //current pos is the root pos
    stack<int> empty_s; //clear the stack
    s = empty_s;
    currentPos = map.rootPos;
    while (currentPos != -1) //while current pos is valid
    {
        s.push(currentPos);
        currentPos = map.lefts[currentPos];
    } //current pos is the left until no more lefts
    if (s.size() != 0)
    {
        currentPos = s.top();
        currentValuePos = 0;
    }
    //now current pos is the position of the leftmost element
    //if stack is empty then current pos is -1;
}
//BC = Th(1) in case of degenerated tree in the right
//WC = Th(h) in case of degenerated tree on the left for example (only need the leftmost to be lowest)

void SMMIterator::next()
{
    if (!valid())
        throw exception();

    int number_of_values = map.nodes[currentPos]->length;
    if (currentValuePos < number_of_values - 1)
        currentValuePos++;
    else if (currentValuePos == number_of_values - 1)
    {
        s.pop();
        if (map.rights[currentPos] != -1) //if there is a right subtree
        {
            currentPos = map.rights[currentPos];
            while (currentPos != -1)
            {
                s.push(currentPos);
                currentPos = map.lefts[currentPos];
            }
        }
        if (s.size() != 0)
        {
            currentPos = s.top(); //current pos is the top of the stack
        }
        else if (s.size() == 0)
        {
            currentPos = -1;
        }
        currentValuePos = 0;
    }
}
//BC = O(1),
//WC = Th(h), if for example reaches the root then goes right, and after left all the way down h steps

bool SMMIterator::valid() const{
    if (currentPos == -1)
        return false;
    else return true;
}
//Th(1)

TElem SMMIterator::getCurrent() const{

    if (!valid())
        throw exception();

    TElem elem;
    elem.first = map.nodes[currentPos]->key;
    elem.second = map.nodes[currentPos]->values[currentValuePos];
    return elem;
}
//Th(1)

