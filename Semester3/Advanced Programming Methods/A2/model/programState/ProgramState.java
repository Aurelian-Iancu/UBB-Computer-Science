package model.programState;

import model.ADT.Dictionary.MyIDictionary;
import model.ADT.List.MyIList;
import model.ADT.Stack.MyIStack;
import model.ADT.Stack.MyStack;
import model.statement.IStatement;
import model.value.Value;
import org.jetbrains.annotations.NotNull;

import java.util.List;
import java.util.Stack;

public class ProgramState {
    private MyIStack<IStatement> exeStack;
    private MyIDictionary<String, Value> symTable;
    private MyIList<Value> out;
    private IStatement originalProgram;

    public ProgramState(@NotNull MyIStack<IStatement> exeStack, MyIDictionary<String, Value> symTable, MyIList<Value> out, IStatement originalProgram) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.originalProgram = originalProgram;
        this.exeStack.push(originalProgram);
    }
    public MyIStack<IStatement> getExeStack() {
        return exeStack;
    }

    public void setExeStack(MyIStack<IStatement> exeStack) {
        this.exeStack = exeStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
    }

    public void setSymTable(MyIDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public IStatement getOriginalProgram() {
        return originalProgram;
    }

    public void setOriginalProgram(IStatement originalProgram) {
        this.originalProgram = originalProgram;
    }

    public String exeStackToString(){
        return exeStack.toString();
    }

    public String symTableToString(){
        return symTable.toString();
    }

    public String outListToString(){
        return out.toString();
    }

    public String toString() {
        return "Execution stack: \n" + exeStack + "\nSymbol table: \n" + symTable.toString() + "\nOutput list: \n" + out.toString();
    }


}
