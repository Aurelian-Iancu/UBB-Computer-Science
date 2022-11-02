package model.ADT.Stack;

import java.util.Stack;

public class MyStack<T> implements MyIStack<T>{
    Stack<T> stack;

    public MyStack(){
        this.stack = new Stack<>();
    }

    @Override
    public T pop() {
        return this.stack.pop();
    }

    @Override
    public void push(T elem) {
        this.stack.push(elem);
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    @Override
    public int size(){return stack.size();}

    @Override
    public String toString(){
        return this.stack.toString();
    }
}
