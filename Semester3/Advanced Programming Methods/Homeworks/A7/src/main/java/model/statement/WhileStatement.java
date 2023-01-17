package model.statement;

import exceptions.InterpreterException;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Stack.MyIStack;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.BoolType;
import model.type.Type;
import model.value.BoolValue;
import model.value.Value;

public class WhileStatement implements IStatement{
    private IExpression expression;
    private IStatement statement;

    public WhileStatement(IExpression expression, IStatement statement) {
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        MyIStack<IStatement> stack = state.getExeStack();
        if(!value.getType().equals(new BoolType()))
            throw new InterpreterException(String.format("%s is not of BoolType", value));
        BoolValue boolValue = (BoolValue) value;
        if(boolValue.getVal()) {
            stack.push(this);
            stack.push(statement);
        }
        return state;

    }

    @Override
    public IStatement deepCopy() {
        return new WhileStatement(expression.deepCopy(), statement.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        Type typeExpr = expression.typeCheck(typeEnv);
        if (typeExpr.equals(new BoolType())) {
            statement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        } else
            throw new InterpreterException("The condition of WHILE does not have the type Bool.");
    }

    @Override
    public String toString() {
        return String.format("while(%s){%s}", expression, statement);
    }
}
