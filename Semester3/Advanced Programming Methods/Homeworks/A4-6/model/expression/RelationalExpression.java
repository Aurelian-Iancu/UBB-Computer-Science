package model.expression;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Heap.MyIHeap;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;

import java.util.Objects;

public class RelationalExpression implements IExpression{
    IExpression expression1;
    IExpression expression2;
    String operator;

    public RelationalExpression(String operator,IExpression expression1, IExpression expression2) {
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operator = operator;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> symTable, MyIHeap heap) throws ADTExceptions, ExpressionEvaluationExceptions {
        Value value1, value2;
        value1 = this.expression1.eval(symTable, heap);
        if (value1.getType().equals(new IntType())){
            value2 = this.expression2.eval(symTable, heap);
            if (value2.getType().equals(new IntType())){
                IntValue val1 = (IntValue) value1;
                IntValue val2 = (IntValue) value2;
                int v1, v2;
                v1 = val1.getVal();
                v2 = val2.getVal();
                if (Objects.equals(this.operator, "<"))
                    return new BoolValue(v1 < v2);
                else if (Objects.equals(this.operator, "<="))
                    return new BoolValue(v1 <= v2);
                else if (Objects.equals(this.operator, "=="))
                    return new BoolValue(v1 == v2);
                else if (Objects.equals(this.operator, "!="))
                    return new BoolValue(v1 != v2);
                else if (Objects.equals(this.operator, ">"))
                    return new BoolValue(v1 > v2);
                else if (Objects.equals(this.operator, ">="))
                    return new BoolValue(v1 >= v2);
            }else
                throw new ExpressionEvaluationExceptions("Second operand is not an integer.");
        } else
            throw new ExpressionEvaluationExceptions("First operand in not an integer.");
        return null;
    }

    @Override
    public IExpression deepCopy() {
        return new RelationalExpression(operator, expression1.deepCopy(), expression2.deepCopy());
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws ExpressionEvaluationExceptions, ADTExceptions {
        Type type1, type2;
        type1 = expression1.typeCheck(typeEnv);
        type2 = expression2.typeCheck(typeEnv);
        if(type1.equals(new IntType())){
            if(type2.equals(new IntType())){
                return new BoolType();
            } else
                throw new ExpressionEvaluationExceptions("Second operand is not an integer!");
        } else
            throw new ExpressionEvaluationExceptions("First operand is not an integer!");

    }

    @Override
    public String toString() {
        return this.expression1.toString() + " " + this.operator + " " + this.expression2.toString();
    }
}