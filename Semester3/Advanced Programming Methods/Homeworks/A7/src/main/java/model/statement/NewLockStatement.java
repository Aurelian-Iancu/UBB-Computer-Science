package model.statement;

import exceptions.InterpreterException;
import model.programState.ProgramState;
import model.type.IntType;
import model.type.Type;
import model.utils.MyIDictionary;
import model.utils.MyILockTable;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class NewLockStatement implements IStatement{
    private final String var;
    private static final Lock lock = new ReentrantLock();

    public NewLockStatement(String var) {
        this.var = var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        lock.lock();
        MyILockTable lockTable = state.getLockTable();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        int freeAddress = lockTable.getFreeValue();
        lockTable.put(freeAddress, -1);
        if (symTable.isDefined(var) && symTable.lookUp(var).getType().equals(new IntType())) {
            symTable.update(var, new IntValue(freeAddress));
        }
        else
            throw new InterpreterException("Variable not declared!");
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (typeEnv.lookUp(var).equals(new IntType()))
            return typeEnv;
        else
            throw new InterpreterException("Var is not of int type!");
    }

    @Override
    public IStatement deepCopy() {
        return new NewLockStatement(var);
    }

    @Override
    public String toString() {
        return String.format("newLock(%s)", var);
    }
}
