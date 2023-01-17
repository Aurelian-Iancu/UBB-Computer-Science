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

public class NewStatement implements IStatement{
    private final String varName;
    private final IExpression expression;

    public NewStatement(String varName, IExpression expression) {
        this.varName = varName;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();
        if (!symTable.containsKey(varName))
            throw new InterpreterException(String.format("%s not in symTable", varName));
        Value varValue = symTable.lookUp(varName);
        if (!(varValue.getType() instanceof RefType))
            throw new InterpreterException(String.format("%s in not of RefType", varName));
        Value evaluated = expression.eval(symTable, heap);
        Type locationType = ((RefValue)varValue).getLocationType();
        if (!locationType.equals(evaluated.getType()))
            throw new InterpreterException(String.format("%s not of %s", varName, evaluated.getType()));
        int newPosition = heap.add(evaluated);
        symTable.put(varName, new RefValue(newPosition, locationType));
        state.setSymTable(symTable);
        state.setHeap(heap);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new NewStatement(varName, expression.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException{
        Type typeVar = typeEnv.lookUp(varName);
        Type typeExp = expression.typeCheck(typeEnv);
        if (typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new InterpreterException("NEW stmt: right hand side and left hand side have different types");
    }

    @Override
    public String toString() {
        return String.format("New(%s, %s)", varName, expression);
    }
}
