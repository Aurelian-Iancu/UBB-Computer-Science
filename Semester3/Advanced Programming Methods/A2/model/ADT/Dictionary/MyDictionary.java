package model.ADT.Dictionary;

import exceptions.ADTExceptions;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<T1, T2> implements MyIDictionary<T1, T2> {
    private final HashMap<T1, T2> dictionary;

    public MyDictionary() {
        dictionary = new HashMap<>();
    }

    @Override
    public void put(T1 key, T2 value) {
        dictionary.put(key, value);
    }

    @Override
    public boolean containsKey(T1 key) {
        return dictionary.containsKey(key);
    }

    @Override
    public T2 get(T1 key) {
        return dictionary.get(key);
    }

    @Override
    public Set<T1> keySet() {
        return dictionary.keySet();
    }

    @Override
    public void remove(T1 key) {
        dictionary.remove(key);
    }

    @Override
    public HashMap<T1, T2> getContent() {
        return dictionary;
    }

    @Override
    public T2 lookUp(T1 key) throws ADTExceptions {
        if (!containsKey(key))
            throw new ADTExceptions(key + " is not defined.");
        return this.dictionary.get(key);
    }

    @Override
    public void update(T1 key, T2 value) throws ADTExceptions {
        if (!containsKey(key))
            throw new ADTExceptions(key + " is not defined.");
        this.dictionary.put(key, value);
    }

    @Override
    public String toString(){
        return this.dictionary.toString();
    }

}
