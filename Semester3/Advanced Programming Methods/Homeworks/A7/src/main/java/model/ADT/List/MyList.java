package model.ADT.List;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T>{
    private final ArrayList<T> list;

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

    @Override
    public List<T> getList() {
        return this.list;
    }


}
