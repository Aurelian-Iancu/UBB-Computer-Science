package model.statement;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.Type;
import model.value.Value;
import org.jetbrains.annotations.NotNull;

public class AssignStatement implements IStatement{
    private String key;
    private IExpression expression;

    public AssignStatement(String key, IExpression expression) {
        this.key = key;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(@NotNull ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        MyIDictionary<String, Value> symbolTable = state.getSymTable();

        if(symbolTable.containsKey(key)){
            Value value = expression.eval(symbolTable);
            Type type = (symbolTable.lookUp(key)).getType();
            if(value.getType().equals(type)){
                symbolTable.update(key, value);
            } else{
                throw new StatementExecutionExceptions("Declared type of variable " + key + " and the type of the assigned expression do not match!");
            }
        } else {
            throw new StatementExecutionExceptions("The used variable " + key + " was not declared before!");
        }
        state.setSymTable(symbolTable);
        return state;
    }

    @Override
    public String toString(){
        return String.format("%s = %s", key, expression.toString());
    }
}
