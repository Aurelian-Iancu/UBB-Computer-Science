package model.ADT.Stack;

import exceptions.ADTExceptions;

import java.util.List;

public interface MyIStack<T> {
    T pop();
    void push(T elem);
    boolean isEmpty();
    int size();
    List<T> getReversed();
}