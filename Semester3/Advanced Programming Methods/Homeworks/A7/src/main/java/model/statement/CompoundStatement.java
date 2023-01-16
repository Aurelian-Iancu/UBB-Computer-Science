package model.statement;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.Stack.MyIStack;
import model.programState.ProgramState;
import model.type.Type;

import java.util.Stack;

public class CompoundStatement implements IStatement{
    IStatement firstStatement;
    IStatement secondStatement;

    public CompoundStatement(IStatement firstStatement, IStatement secondStatement) {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }


    @Override
    public ProgramState execute(ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        MyIStack<IStatement> stack = state.getExeStack();
        stack.push(secondStatement);
        stack.push(firstStatement);
        state.setExeStack(stack);
        return state;
    }

    @Override
    public IStatement deepCopy() {
        return new CompoundStatement(firstStatement.deepCopy(), secondStatement.deepCopy());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws StatementExecutionExceptions, ExpressionEvaluationExceptions, ADTExceptions {
        return secondStatement.typeCheck(firstStatement.typeCheck(typeEnv));
    }

    @Override
    public String toString() {
        return String.format("(%s|%s)", firstStatement.toString(), secondStatement.toString());
    }
}
