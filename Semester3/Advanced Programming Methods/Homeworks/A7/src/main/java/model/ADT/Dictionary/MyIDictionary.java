package model.ADT.Dictionary;

import exceptions.InterpreterException;

import java.util.HashMap;
import java.util.Set;

public interface MyIDictionary<T1, T2> {
    void put(T1 key, T2 value);
    boolean containsKey(T1 key);
    T2 get(T1 key);
    Set<T1> keySet();
    void remove(T1 key);
    HashMap<T1, T2> getContent();

    T2 lookUp(T1 key) throws InterpreterException;
    void update(T1 key, T2 value) throws InterpreterException;

    MyIDictionary<T1, T2> deepCopy() throws InterpreterException;


}
