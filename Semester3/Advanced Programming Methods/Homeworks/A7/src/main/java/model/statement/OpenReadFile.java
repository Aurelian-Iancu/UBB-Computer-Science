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
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFile implements IStatement{
    private final IExpression expression;

    public OpenReadFile(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if(value.getType().equals(new StringType())){
            StringValue filename = (StringValue) value;
            MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
            if(!fileTable.containsKey(filename.getValue())){
                BufferedReader br;
                try{
                    br = new BufferedReader(new FileReader(filename.getValue()));
                }catch(FileNotFoundException e){
                    throw new InterpreterException("The file could not be opened");
                }
                fileTable.put(filename.getValue(), br);
                state.setFileTable(fileTable);
            }else{
                throw new InterpreterException("The file is already open");
            }
        }else{
            throw new InterpreterException("The expression is not a string");
        }
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new OpenReadFile(expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws  InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("OpenReadFile requires a string expression.");
    }

    @Override
    public String toString(){
        return "open(" + expression.toString() + ")";
    }
}
