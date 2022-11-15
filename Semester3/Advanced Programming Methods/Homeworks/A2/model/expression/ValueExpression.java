package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.value.Value;

public class ValueExpression implements IExpression{
    Value value;

    public ValueExpression(Value value) {
        this.value = value;
    }


    @Override
    public Value eval(MyIDictionary<String, Value> symTable) throws ADTExceptions, ExpressionEvaluationExceptions {
        return this.value;
    }

    @Override
    public String toString(){
        return this.value.toString();
    }
}
