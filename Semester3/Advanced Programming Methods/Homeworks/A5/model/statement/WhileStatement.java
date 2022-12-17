package model.statement;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Stack.MyIStack;
import model.expression.IExpression;
import model.programState.ProgramState;
import model.type.BoolType;
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
    public ProgramState execute(ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        MyIStack<IStatement> stack = state.getExeStack();
        if(!value.getType().equals(new BoolType()))
            throw new StatementExecutionExceptions(String.format("%s is not of BoolType", value));
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
    public String toString() {
        return String.format("while(%s){%s}", expression, statement);
    }
}
