package controller;

import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Stack.MyIStack;
import model.programState.ProgramState;
import model.statement.IStatement;
import model.statement.IfStatement;
import model.value.RefValue;
import model.value.Value;
import repository.IRepository;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

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

    public List<Integer> getAddrFromSymTable(Collection<Value> symTableValues) {
        return symTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddrFromHeap(Collection<Value> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }


    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, List<Integer> heapAddr, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symTableAddr.contains(e.getKey()) || heapAddr.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void allSteps() throws ExpressionEvaluationExceptions, ADTExceptions, StatementExecutionExceptions, IOException{
        ProgramState program = this.repository.getCurrentState();
        this.repository.logPrgStateExec();
        display();
        while(!program.getExeStack().isEmpty()) {
            oneStep(program);

            program.getHeap().setHeap((HashMap<Integer, Value>) safeGarbageCollector(
                    getAddrFromSymTable(program.getSymTable().getContent().values()),
                    getAddrFromHeap(program.getHeap().getHeap().values()),
                    program.getHeap().getHeap()
            ));
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
