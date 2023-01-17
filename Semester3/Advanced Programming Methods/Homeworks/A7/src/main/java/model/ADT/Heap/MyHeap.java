package model.ADT.Heap;

import exceptions.InterpreterException;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public class MyHeap implements MyIHeap{
    HashMap<Integer, Value> heap;
    Integer freeLocationValue;

    public MyHeap() {
        this.heap = new HashMap<>();
        this.freeLocationValue = 1;
    }

    public int newValue(){
        freeLocationValue += 1;
        while(freeLocationValue == 0 || heap.containsKey(freeLocationValue))
            freeLocationValue += 1;
        return freeLocationValue;
    }

    @Override
    public int getFreeValue() {
        return freeLocationValue;
    }

    @Override
    public HashMap<Integer, Value> getHeap() {
        return heap;
    }

    @Override
    public void setHeap(HashMap<Integer, Value> newHeap) {
        this.heap = newHeap;
    }

    @Override
    public int add(Value value) {
        heap.put(freeLocationValue, value);
        Integer toReturn = freeLocationValue;
        freeLocationValue = newValue();
        return toReturn;
    }

    @Override
    public void update(Integer position, Value value) throws InterpreterException {
        if(!heap.containsKey(position))
            throw new InterpreterException(String.format("%d is not present in the heap", position));
        heap.put(position, value);
    }

    @Override
    public Value get(Integer position) throws InterpreterException {
        if(!heap.containsKey(position))
            throw new InterpreterException(String.format("%d is not present in the heap", position));
        return heap.get(position);
    }

    @Override
    public boolean containsKey(Integer position) {
        return this.heap.containsKey(position);
    }

    @Override
    public void remove(Integer key) throws InterpreterException {
        if (!containsKey(key))
            throw new InterpreterException(key + " is not defined.");
        freeLocationValue = key;
        this.heap.remove(key);
    }

    @Override
    public Set<Integer> keySet() {
        return heap.keySet();
    }

    @Override
    public String toString(){
        return this.heap.toString();
    }
}
