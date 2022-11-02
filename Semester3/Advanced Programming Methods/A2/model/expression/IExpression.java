package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.value.Value;

public interface IExpression {
    Value eval(MyIDictionary<String, Value> symTable) throws ADTExceptions, ExpressionEvaluationExceptions;
}
