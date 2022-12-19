package model.ADT.List;

import exceptions.ADTExceptions;

import java.util.List;

public interface MyIList<T> {
    int size();
    boolean isEmpty();
    void add(T e);
    T get(int index);
    String toString();

    List<T> getList();
}
