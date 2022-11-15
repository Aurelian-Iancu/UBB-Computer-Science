package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.value.Value;
import org.jetbrains.annotations.NotNull;

public class VariableExpression implements IExpression{
    String key;

    public VariableExpression(String key) {
        this.key = key;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable) throws ADTExceptions, ExpressionEvaluationExceptions {
        return symTable.lookUp(key);
    }

    @Override
    public String toString(){
        return this.key;
    }
}


