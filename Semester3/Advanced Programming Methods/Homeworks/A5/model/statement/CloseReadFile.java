package model.statement;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.StringType;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseReadFile implements IStatement{
    private final IExpression expression;

    public CloseReadFile(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if(!value.getType().equals(new StringType())){
            throw new StatementExecutionExceptions("The expression is not a string");
        }
        StringValue fileName = (StringValue) value;
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        if(!fileTable.containsKey(fileName.getValue())){
            throw new StatementExecutionExceptions("The file is not open");
        }
        BufferedReader bufferedReader = fileTable.lookUp(fileName.getValue());
        try{
            bufferedReader.close();
        }catch (IOException e){
            throw new StatementExecutionExceptions("The file could not be closed");
        }
        fileTable.remove(fileName.getValue());
        state.setFileTable(fileTable);
        return null;
    }

    @Override
    public IStatement deepCopy() {
        return new CloseReadFile(expression.deepCopy());
    }

    @Override
    public String toString(){
        return "close(" + expression.toString() + ")";
    }
}
