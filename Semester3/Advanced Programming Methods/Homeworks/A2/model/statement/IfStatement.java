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

import java.util.Stack;

public class IfStatement implements IStatement{
    IExpression expression;
    IStatement thenStatement;
    IStatement elseStatement;

    public IfStatement(IExpression expression, IStatement thenStatement, IStatement elseStatement) {
        this.expression = expression;
        this.thenStatement = thenStatement;
        this.elseStatement = elseStatement;
    }


    @Override
    public ProgramState execute(ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        Value result = this.expression.eval(state.getSymTable());
        if (result.getType().equals(new BoolType())){
            BoolValue condition = (BoolValue) result;
            IStatement statement;
            if(condition.getVal())
                statement = thenStatement;
            else
                statement = elseStatement;

            MyIStack<IStatement> stack = state.getExeStack();
            stack.push(statement);
            state.setExeStack(stack);
            return state;
        } else{
            throw new StatementExecutionExceptions("The expression cannot be evaluated as true or false!");
        }
    }

    @Override
    public String toString() {
        return String.format("if(%s){%s}else{%s}", expression.toString(), thenStatement.toString(), elseStatement.toString());
    }
}
