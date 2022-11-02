package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.type.BoolType;
import model.value.BoolValue;
import model.value.Value;

import java.util.Objects;

public class LogicExpression implements IExpression{
    IExpression expression1;
    IExpression expression2;
    String operation;

    public LogicExpression(IExpression expression1, IExpression expression2, String operation) {
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operation = operation;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable) throws ADTExceptions, ExpressionEvaluationExceptions {
        Value value1, value2;
        value1 = this.expression1.eval(symTable);
        if(value1.getType().equals(new BoolType())){
            value2 = this.expression2.eval(symTable);
            if(value2.getType().equals(new BoolType())){
                BoolValue bool1 = (BoolValue) value1;
                BoolValue bool2 = (BoolValue) value2;
                boolean b1, b2;
                b1 = bool1.getVal();
                b2 = bool2.getVal();
                if(Objects.equals(this.operation, "and")){
                    return new BoolValue(b1 && b2);
                } else if(Objects.equals(this.operation,"or")){
                    return new BoolValue(b1 || b2);
                }
            } else
                throw new ExpressionEvaluationExceptions("Second operand is not of boolean type!");
        } else
            throw new ExpressionEvaluationExceptions("The first operand is not of boolean type!");
        return null;
    }
    @Override
    public String toString(){
        return expression1.toString() + " " + operation + " " + expression2.toString();
    }
}
