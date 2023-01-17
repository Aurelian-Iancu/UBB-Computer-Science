package model.utils;


import exceptions.InterpreterException;

import java.util.List;
import java.util.function.Consumer;

public interface MyIList<T> {
    void add(T elem);
    T pop() throws InterpreterException;
    boolean isEmpty();
    List<T> getList();
}