package model.ADT.Heap;

import exceptions.ADTExceptions;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public interface MyIHeap {
    int getFreeValue();
    HashMap<Integer, Value> getHeap();
    void setHeap(HashMap<Integer, Value> newHeap);
    int add(Value value);
    void update(Integer position, Value value) throws ADTExceptions;
    Value get(Integer position) throws ADTExceptions;
    boolean containsKey(Integer position);
    void remove(Integer key) throws ADTExceptions;
    Set<Integer> keySet();
}
