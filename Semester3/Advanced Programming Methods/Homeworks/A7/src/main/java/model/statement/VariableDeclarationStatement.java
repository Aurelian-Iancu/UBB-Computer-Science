package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.programState.ProgramState;
import model.type.Type;
import model.value.Value;

public class VariableDeclarationStatement implements IStatement{
    String name;
    Type type;

    public VariableDeclarationStatement(String name, Type type) {
        this.name = name;
        this.type = type;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        if(symTable.containsKey(name)){
            throw new InterpreterException("Variable " + name + " is already declared!");
        }
        symTable.put(name, type.defaultValue());
        state.setSymTable(symTable);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new VariableDeclarationStatement(name, type.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public String toString() {
        return String.format("%s %s", type.toString(), name);
    }
}
