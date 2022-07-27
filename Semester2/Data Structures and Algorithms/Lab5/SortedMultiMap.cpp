#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <vector>
#include <exception>
using namespace std;

//implemented using a bst with linked list on array representation

SortedMultiMap::SortedMultiMap(Relation r) : rel{r}, capacity{1}, rootPos{-1}, treeLength{0}, firstEmptyPos{0}
{
    lefts = new int[capacity];
    rights = new int[capacity];
    nodes = new Node * [capacity];
    for (int i = 0; i < capacity - 1; i++)
    {
        nodes[i]->key = NULL_KVALUE;
        lefts[i] = i + 1;
        rights[i] = -1;
    }
    lefts[capacity - 1] = -1;
}
//Th(capacity)

void SortedMultiMap::resizeTree()
{
    int* newNextPos = new int[capacity * 2];
    int* newLefts = new int[capacity * 2];
    int* newRights = new int[capacity * 2];
    Node** newNodes = new Node * [capacity * 2];
    for (int i = 0; i < capacity; i++)
    {
        newLefts[i] = lefts[i];
        newRights[i] = rights[i];
        newNodes[i] = nodes[i];
    }
    for (int i = capacity; i < capacity * 2 - 1; i++)
    {

        newLefts[i] = i+1;
        newRights[i] = -1;
    }
    newLefts[capacity * 2 - 1] = -1;

    delete[] nodes;
    delete[] lefts;
    delete[] rights;

    nodes = newNodes;
    lefts = newLefts;
    rights = newRights;

    firstEmptyPos = capacity;
    capacity = capacity * 2;
}
//Th(capacity)


void SortedMultiMap::add(TKey c, TValue v) {

    if (treeLength == 0)
    {
        createNode(firstEmptyPos, c, v);
        rootPos = firstEmptyPos;
        firstEmptyPos = lefts[firstEmptyPos];
        lefts[rootPos] = -1;
        rights[rootPos] = -1;

        treeLength++;
        return;
    }

    int currentPos = rootPos;
    int prevPos = -1;
    while (currentPos != -1)
    {
        if (nodes[currentPos]->key == c)
            break;
        else if (rel(nodes[currentPos]->key, c)) //current node  is "smaller" go right
        {
            prevPos = currentPos;
            currentPos = rights[currentPos];
        }
        else if (!rel(nodes[currentPos]->key, c))//search for an empty pos/existing pos
        {
            prevPos = currentPos;
            currentPos = lefts[currentPos];
        }
    }
    if (currentPos != -1) //if the key already exists
    {
        if (nodes[currentPos]->length == nodes[currentPos]->capacity)
            resizeValues(nodes[currentPos]);
        nodes[currentPos]->values[nodes[currentPos]->length] = v;
        nodes[currentPos]->length++;
        treeLength++;
    }
    if (currentPos == -1) // if the key does not exist we must add it
    {
        if (firstEmptyPos == -1)
            resizeTree();

        currentPos = firstEmptyPos;
        createNode(currentPos, c, v);

        if (rel(nodes[prevPos]->key, c)) // previus node is "smaller" than the one we are adding, so add to the right
            rights[prevPos] = currentPos;
        else
            lefts[prevPos] = currentPos;

        firstEmptyPos = lefts[currentPos];
        lefts[currentPos] = -1;
        rights[currentPos] = -1;
        treeLength++;
    }
}
//BC: Th(1) if it adds a new value for the root
//WC: Th(h) if it adds a new node, for example add a new node with the smallest value to a degenerated tree on the left


vector<TValue> SortedMultiMap::search(TKey c) const {
    if (treeLength == 0)
        return vector<TValue>();

    int currentPos = rootPos;
    while (currentPos != -1)
    {
        if (nodes[currentPos]->key == c)
            break;
        else if (rel(nodes[currentPos]->key, c))
            currentPos = rights[currentPos];
        else if (!rel(nodes[currentPos]->key, c))
            currentPos = lefts[currentPos];
    }
    if (currentPos == -1)
        return vector<TValue>();
    else if (currentPos != -1)
    {
        vector<TValue> values;
        for (int i = 0; i < nodes[currentPos]->length; i++)
        {
            values.push_back(nodes[currentPos]->values[i]);
        }
        return values;
    }
}
//BC : Th(1), to find the first value in the root
//WC: Th(h + values.length), to find the last element for the lowest node

bool SortedMultiMap::remove(TKey c, TValue v) {
    if (treeLength == 0)
        return false;
    if (treeLength == 1 && nodes[rootPos]->values[0] == v)
    {
        nodes[rootPos]->length--;
        delete[] nodes[rootPos]->values;
        lefts[rootPos] = firstEmptyPos;
        firstEmptyPos = rootPos;
        rootPos = -1;
        treeLength--;
        return true;
    }
    if (treeLength == 1 && nodes[rootPos]->values[0] != v)
        return false;

    int currentPos = rootPos;
    int prevPos = -1;
    while (currentPos != -1)
    {
        if (nodes[currentPos]->key == c)
            break;
        else if (rel(nodes[currentPos]->key, c))
        {
            prevPos = currentPos;
            currentPos = rights[currentPos];
        }
        else if (!rel(nodes[currentPos]->key, c))
        {
            prevPos = currentPos;
            currentPos = lefts[currentPos];
        }
    } //find if the key exists
    if (currentPos == -1)
        return false; //key does not exists
    else //key exists
    {
        if (nodes[currentPos]->length > 1) //if there is more than 1 value
            return findAndRemoveFromValues(currentPos, v);
        else
        {
            if (nodes[currentPos]->values[0] != v) //correct key but incorrect value
                return false;
            else                                   //correct key and correct value
            {
                if ((lefts[currentPos] == -1) && (rights[currentPos] == -1)) //leaf
                {
                    removeLeaf(currentPos, prevPos);
                    lefts[currentPos] = firstEmptyPos;
                    firstEmptyPos = currentPos;
                    treeLength--;
                    return true;
                }
                if ((lefts[currentPos] == -1) || (rights[currentPos] == -1)) //only 1 side descendants
                {
                    removeNodeWithOneDescendant(currentPos, prevPos);
                    lefts[currentPos] = firstEmptyPos;
                    firstEmptyPos = currentPos;
                    rights[currentPos] = -1;
                    treeLength--;
                    return true;
                }
                if ((lefts[currentPos] != -1) && (rights[currentPos] != -1))//has 2 descendants
                {
                    int nodeToReplace = currentPos;
                    while (lefts[currentPos] != -1) //find the smallest higher than the node you want to remove
                    {
                        prevPos = currentPos;
                        currentPos = lefts[currentPos];
                    }
                    nodes[nodeToReplace]->key = nodes[currentPos]->key;
                    nodes[nodeToReplace]->length = nodes[currentPos]->length;
                    nodes[nodeToReplace]->capacity = nodes[currentPos]->capacity;
                    delete[] nodes[nodeToReplace]->values;
                    nodes[nodeToReplace]->values = new TValue[nodes[currentPos]->capacity]; //replace values
                    for (int i = 0; i < nodes[nodeToReplace]->length; i++)
                    {
                        nodes[nodeToReplace]->values[i] = nodes[currentPos]->values[i];
                    }
                    //replace all data
                    if ((lefts[currentPos] == -1) && (rights[currentPos] == -1)) //leaf
                    {
                        removeLeaf(currentPos, prevPos);
                        lefts[currentPos] = firstEmptyPos;
                        firstEmptyPos = currentPos;
                        treeLength--;
                        return true;
                    }
                    else
                    {
                        removeNodeWithOneDescendant(currentPos, prevPos);
                        lefts[currentPos] = firstEmptyPos;
                        firstEmptyPos = currentPos;
                        rights[currentPos] = -1;
                        treeLength--;
                        return true;
                    }

                }
            }
        }
    }
    //key does not exist
    return false;
}
//BC: TH(1), one example would be a degenerated tree on the right when removing the root
//WC: Th(h), there are a lot of possible cases for that

int SortedMultiMap::size() const {
    return treeLength;
}
//Th(1)

bool SortedMultiMap::isEmpty() const {
    return (treeLength == 0);
}
//Th(1)

SMMIterator SortedMultiMap::iterator() const {
    return SMMIterator(*this);
}
//see iterator





SortedMultiMap::~SortedMultiMap()
{
    SMMIterator it = iterator();
    while (it.valid())
    {
        if (it.currentValuePos == it.map.nodes[it.currentPos]->length)
        {
            delete[] it.map.nodes[it.currentPos]->values;
        }
        it.next();
    }
    delete[] nodes;
    delete[] lefts;
    delete[] rights;
}
//approx Th(nrOfValues)

void SortedMultiMap::createNode(int Pos, TKey c, TValue v)
{
    nodes[Pos] = new Node;
    nodes[Pos]->capacity = 4;
    nodes[Pos]->length = 1;

    nodes[Pos]->key = c;
    nodes[Pos]->values = new TValue[nodes[Pos]->capacity];
    nodes[Pos]->values[0] = v;
}

bool SortedMultiMap::findAndRemoveFromValues(int Pos, TValue v)
{
    int currentValPos = 0;
    while (currentValPos < nodes[Pos]->length)
    {
        if (nodes[Pos]->values[currentValPos] == v)
            break;
        currentValPos++;
    }
    if (currentValPos == nodes[Pos]->length) //not found
        return false;
    else
    {
        for (int i = currentValPos; i < nodes[Pos]->length - 1; i++)
            nodes[Pos]->values[i] = nodes[Pos]->values[i + 1];
        nodes[Pos]->length--;
        treeLength--;
        return true;
    }

}

void SortedMultiMap::removeLeaf(int leafPos, int parentPos) //lefts and rights of deleted node do not change
{
    if (lefts[parentPos] == leafPos) //leaf is left child
    {
        delete[] nodes[leafPos]->values;
        lefts[parentPos] = -1;
    }
    else
    {
        delete[] nodes[leafPos]->values;
        rights[parentPos] = -1;
    }
}

void SortedMultiMap::removeNodeWithOneDescendant(int nodePos, int parentPos) //lefts and rights of deleted node do not change
{
    if (parentPos != -1)
    {
        if (lefts[parentPos] == nodePos) //node is left child
        {
            if (rights[nodePos] == -1) //node has only left descendants
            {
                delete[] nodes[nodePos]->values;
                nodes[nodePos]->length = 0;
                lefts[parentPos] = lefts[nodePos];
            }
            else if (lefts[nodePos] == -1) //node has only right descendants
            {
                delete[] nodes[nodePos]->values;
                nodes[nodePos]->length = 0;
                lefts[parentPos] = rights[nodePos];
            }
        }
        else  //node is right child
        {
            if (rights[nodePos] == -1) //node has only left descendants
            {
                delete[] nodes[nodePos]->values;
                nodes[nodePos]->length = 0;
                rights[parentPos] = lefts[nodePos];
            }
            else if (lefts[nodePos] == -1) //node has only right descendants
            {
                delete[] nodes[nodePos]->values;
                nodes[nodePos]->length = 0;
                rights[parentPos] = rights[nodePos];
            }
        }
    }
    else //remove root
    {
        if (lefts[nodePos] == -1) //root has only right descendants
        {
            delete[] nodes[nodePos];
            nodes[nodePos]->length = 0;
            rootPos = rights[nodePos];
        }
        else if (rights[nodePos] == -1) //root has only right descendants
        {
            delete[] nodes[nodePos];
            nodes[nodePos]->length = 0;
            rootPos = lefts[nodePos];
        }
    }
}

void SortedMultiMap::replace(TKey k, TValue oldValue, TValue newValue)
{
    int currentPos = rootPos;
    while (currentPos != -1)
    {
        if (nodes[currentPos]->key == k)
            break;
        else if (rel(nodes[currentPos]->key, k))
            currentPos = rights[currentPos];
        else if (!rel(nodes[currentPos]->key, k))
            currentPos = lefts[currentPos];
    }

    if (currentPos != -1)
    {
        if(nodes[currentPos]->length > 0)
            if(nodes[currentPos]->values[0] == oldValue)
            {
                nodes[currentPos]->values[0] = newValue;
            }
    }
}


void resizeValues(Node* node)
{
    node->capacity = node->capacity * 2;
    TValue* temp = new TValue[node->capacity];
    for (int i = 0; i < node->length; i++)
        temp[i] = node->values[i];
    delete[] node->values;
    node->values = temp;
}

