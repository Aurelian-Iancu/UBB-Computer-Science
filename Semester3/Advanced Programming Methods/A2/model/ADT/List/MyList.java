package model.ADT.List;

import exceptions.ADTExceptions;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T>{
    private ArrayList<T> list;

    public MyList() {
        list = new ArrayList<>();
    }

    @Override
    public int size() {
        return list.size();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public void add(T e) {
        list.add(e);
    }

    @Override
    public T get(int index) {
        return list.get(index);
    }

    @Override
    public String toString(){
        return this.list.toString();
    }
}
