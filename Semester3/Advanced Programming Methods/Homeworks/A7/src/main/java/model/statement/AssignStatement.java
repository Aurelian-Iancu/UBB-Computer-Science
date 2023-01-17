package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.Type;
import model.value.Value;

public class AssignStatement implements IStatement{
    private String key;
    private IExpression expression;

    public AssignStatement(String key, IExpression expression) {
        this.key = key;
        this.expression = expression;
    }


    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symbolTable = state.getSymTable();

        if(symbolTable.containsKey(key)){
            Value value = expression.eval(symbolTable, state.getHeap());
            Type type = (symbolTable.lookUp(key)).getType();
            if(value.getType().equals(type)){
                symbolTable.update(key, value);
            } else{
                throw new InterpreterException("Declared type of variable " + key + " and the type of the assigned expression do not match!");
            }
        } else {
            throw new InterpreterException("The used variable " + key + " was not declared before!");
        }
        state.setSymTable(symbolTable);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new AssignStatement(key, expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        Type typeVar = typeEnv.lookUp(key);
        Type typeExp = expression.typeCheck(typeEnv);
        if(typeVar.equals(typeExp))
            return typeEnv;
        else
            throw new InterpreterException("Assignment: right hand side and left hand side have different types ");
    }

    @Override
    public String toString(){
        return String.format("%s = %s", key, expression.toString());
    }
}
