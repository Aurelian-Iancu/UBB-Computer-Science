package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Heap.MyIHeap;
import model.type.Type;
import model.value.Value;

public class ValueExpression implements IExpression{
    Value value;

    public ValueExpression(Value value) {
        this.value = value;
    }


    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws ADTExceptions, ExpressionEvaluationExceptions {
        return this.value;
    }

    @Override
    public IExpression deepCopy() {
        return new ValueExpression(value.deepCopy());
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws ExpressionEvaluationExceptions, ADTExceptions {
        return value.getType();
    }

    @Override
    public String toString(){
        return this.value.toString();
    }
}
