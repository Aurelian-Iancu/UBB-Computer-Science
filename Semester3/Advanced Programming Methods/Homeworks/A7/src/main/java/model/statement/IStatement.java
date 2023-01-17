package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.programState.ProgramState;
import model.type.Type;

public interface IStatement {
    ProgramState execute(ProgramState state) throws InterpreterException;
    IStatement deepCopy();

    MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException;
}
