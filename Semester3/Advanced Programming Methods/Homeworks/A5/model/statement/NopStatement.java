package model.statement;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.programState.ProgramState;

public class NopStatement implements IStatement{
    @Override
    public ProgramState execute(ProgramState state) throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions {
        return null;
    }
    @Override
    public String toString() {
        return "NopStatement";
    }
}
