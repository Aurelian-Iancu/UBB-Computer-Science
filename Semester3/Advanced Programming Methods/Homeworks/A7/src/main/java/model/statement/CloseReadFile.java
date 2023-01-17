package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.StringType;
import model.type.Type;
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
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if(!value.getType().equals(new StringType())){
            throw new InterpreterException("The expression is not a string");
        }
        StringValue fileName = (StringValue) value;
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        if(!fileTable.containsKey(fileName.getValue())){
            throw new InterpreterException("The file is not open");
        }
        BufferedReader bufferedReader = fileTable.lookUp(fileName.getValue());
        try{
            bufferedReader.close();
        }catch (IOException e){
            throw new InterpreterException("The file could not be closed");
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
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("CloseReadFile requires a string expression.");
    }

    @Override
    public String toString(){
        return "close(" + expression.toString() + ")";
    }
}
