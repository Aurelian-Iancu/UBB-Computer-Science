package controller;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Stack.MyIStack;
import model.programState.ProgramState;
import model.statement.IStatement;
import model.statement.IfStatement;
import repository.IRepository;

import java.io.IOException;
import java.util.Stack;

public class Controller {
    IRepository repository;
    boolean displayFlag = false;

    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public ProgramState oneStep(ProgramState state) throws StatementExecutionExceptions, ADTExceptions, ExpressionEvaluationExceptions{
        MyIStack<IStatement> stack = state.getExeStack();
        if(stack.isEmpty())
            throw new StatementExecutionExceptions("Execution stack is empty!");
        IStatement currentStatement = stack.pop();
        state.setExeStack(stack);
        return currentStatement.execute(state);
    }

    public void allSteps() throws ExpressionEvaluationExceptions, ADTExceptions, StatementExecutionExceptions, IOException{
        ProgramState program = this.repository.getCurrentState();
        this.repository.logPrgStateExec();
        display();
        while(!program.getExeStack().isEmpty()) {
            oneStep(program);
            this.repository.logPrgStateExec();
            display();
        }

    }

    private void display() throws ADTExceptions {
        if(displayFlag){
            System.out.println(this.repository.getCurrentState().programStateToString());
        }
    }
}
