package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Heap.MyIHeap;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public class WriteHeapStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public WriteHeapStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();
        if (!symTable.containsKey(varName))
            throw new InterpreterException(String.format("%s not present in the symTable", varName));
        Value value = symTable.lookUp(varName);
        if (!(value instanceof RefValue))
            throw new InterpreterException(String.format("%s not of RefType", value));
        RefValue refValue = (RefValue) value;
        Value evaluated = expression.eval(symTable, heap);
        if (!evaluated.getType().equals(refValue.getLocationType()))
            throw new InterpreterException(String.format("%s not of %s", evaluated, refValue.getLocationType()));
        heap.update(refValue.getAddress(), evaluated);
        state.setHeap(heap);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new WriteHeapStatement(varName, expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (typeEnv.lookUp(varName).equals(new RefType(expression.typeCheck(typeEnv))))
            return typeEnv;
        else
            throw new InterpreterException("WriteHeap: right hand side and left hand side have different types.");
    }

    @Override
    public String toString() {
        return String.format("WriteHeap(%s, %s)", varName, expression);
    }
}
