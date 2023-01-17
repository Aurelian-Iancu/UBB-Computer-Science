package model.expression;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Heap.MyIHeap;
import model.type.Type;
import model.value.Value;

public class VariableExpression implements IExpression{
    String key;

    public VariableExpression(String key) {
        this.key = key;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws InterpreterException {
        return symTable.lookUp(key);
    }

    @Override
    public IExpression deepCopy() {
        return new VariableExpression(key);
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        return typeEnv.lookUp(key);
    }

    @Override
    public String toString(){
        return this.key;
    }
}


