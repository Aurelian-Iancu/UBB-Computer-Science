#pragma once
//DO NOT INCLUDE SMMITERATOR

//DO NOT CHANGE THIS PART
#include <vector>
#include <utility>
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111);
#define NULL_KVALUE -111111
using namespace std;
class SMMIterator;
typedef bool(*Relation)(TKey, TKey);

struct Node
{
    TKey key;
    TValue* values;
    int capacity;
    int length;
};

class SortedMultiMap {
    friend class SMMIterator;
private:
    int rootPos;
    int firstEmptyPos;
    int* lefts;
    int* rights;
    Node** nodes;
    Relation rel;
    int treeLength;
    int capacity;

    void resizeTree();

    void createNode(int Pos, TKey c, TValue v); //does not complete the lefts and rights vector!!!!!

    bool findAndRemoveFromValues(int Pos, TValue v);

    void removeLeaf(int leafPos, int parentPos);

    void removeNodeWithOneDescendant(int nodePos, int parentPos);

public:

    // constructor
    SortedMultiMap(Relation r);

    //adds a new key value pair to the sorted multimap
    void add(TKey c, TValue v);

    //returns the values belonging to a given key
    vector<TValue> search(TKey c) const;

    //removes a key value pair from the sorted multimap
    //returns true if the pair was removed (it was part of the multimap), false if nothing is removed
    bool remove(TKey c, TValue v);

    //returns the number of key-value pairs from the sorted multimap
    int size() const;

    //verifies if the sorted multi map is empty
    bool isEmpty() const;

    // returns an iterator for the sorted multimap. The iterator will return the pairs as required by the relation (given to the constructor)
    SMMIterator iterator() const;

    // destructor
    ~SortedMultiMap();

    void replace(TKey k, TValue oldValue, TValue newValue);




};

void resizeValues(Node* node);