package model.expression;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Heap.MyIHeap;
import model.type.Type;
import model.value.Value;

public interface IExpression {
    Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws InterpreterException;
    IExpression deepCopy();
    Type typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException;
}
