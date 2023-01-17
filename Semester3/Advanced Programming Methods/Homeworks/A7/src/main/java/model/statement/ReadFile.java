package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFile implements IStatement{
    private final IExpression expression;
    private final String variableName;

    public ReadFile(IExpression expression, String variableName) {
        this.expression = expression;
        this.variableName = variableName;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symbolTable = state.getSymTable();
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        if(symbolTable.containsKey(variableName)){
            Value value = symbolTable.lookUp(variableName);
            if(value.getType().equals(new IntType())){
                value = expression.eval(symbolTable, state.getHeap());
                if(value.getType().equals(new StringType())){
                    StringValue castValue = (StringValue) value;
                    if(fileTable.containsKey(castValue.getValue())){
                        BufferedReader br = fileTable.lookUp(castValue.getValue());
                        try{
                            String line = br.readLine();
                            if(line == null)
                                line = "0";
                            symbolTable.put(variableName, new IntValue(Integer.parseInt(line)));
                        }catch(IOException e){
                            throw new InterpreterException("The file could not be read");
                        }
                    }else{
                        throw new InterpreterException(String.format("The file table does not contain %s", castValue));
                    }
                }else{
                    throw new InterpreterException("The expression is not a string");
                }
            }else{
                throw new InterpreterException("The variable is not an integer");
            }
        }else{
            throw new InterpreterException("The variable is not defined in the symTable");
        }
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new ReadFile(expression.deepCopy(), variableName);
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            if (typeEnv.lookUp(variableName).equals(new IntType()))
                return typeEnv;
            else
                throw new InterpreterException("ReadFile requires an int as its variable parameter.");
        else
            throw new InterpreterException("ReadFile requires a string as es expression parameter.");
    }
}
