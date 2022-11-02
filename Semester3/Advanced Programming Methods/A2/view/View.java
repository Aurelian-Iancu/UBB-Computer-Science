package view;

import controller.Controller;
import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;
import model.ADT.Dictionary.MyDictionary;
import model.ADT.Dictionary.MyIDictionary;
import model.ADT.List.MyIList;
import model.ADT.List.MyList;
import model.ADT.Stack.MyIStack;
import model.ADT.Stack.MyStack;
import model.expression.ArithmeticExpression;
import model.expression.ValueExpression;
import model.expression.VariableExpression;
import model.programState.ProgramState;
import model.statement.*;
import model.type.BoolType;
import model.type.IntType;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;
import repository.IRepository;
import repository.Repository;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;
import java.util.Stack;

public class View {
    public void start() {
        boolean done = false;
        while (!done) {
            try {
                printMenu();
                Scanner readOption = new Scanner(System.in);
                int option = readOption.nextInt();
                if (option == 0) {
                    done = true;
                } else if (option == 1) {
                    runProgram1();
                } else if (option == 2) {
                    runProgram2();
                } else if (option == 3) {
                    runProgram3();
                } else {
                    System.out.println("Invalid input!");
                }
            } catch (Exception exception) {
                System.out.println(exception.getMessage());
            }
        }
    }

    private static void printMenu(){
        System.out.println("MENU: ");
        System.out.println("0. Exit.");
        System.out.println("1. Run the first program: \n\tint v;v=2;Print(v)");
        System.out.println("2. Run the second program: \n\tint a;int b;a=2+3*5;b=a+1;Print(b)");
        System.out.println("3. Run the third program: \n\tbool a;int v;a=true;(If a Then v=2 Else v=3);Print(v)");
        System.out.println("Choose an option: ");
    }

    private void runProgram1() throws ExpressionEvaluationExceptions, ADTExceptions, StatementExecutionExceptions, IOException {
        IStatement ex1 = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        runStatement(ex1);
    }

    private void runProgram2() throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions, IOException{
        IStatement ex2 = new CompoundStatement(new VariableDeclarationStatement("a",new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b",new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ArithmeticExpression('+',new ValueExpression(new IntValue(2)),new
                                ArithmeticExpression('*',new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(new AssignStatement("b",new ArithmeticExpression('+',new VariableExpression("a"), new ValueExpression(new
                                        IntValue(1)))), new PrintStatement(new VariableExpression("b"))))));
        runStatement(ex2);
    }

    private void runProgram3() throws ADTExceptions, ExpressionEvaluationExceptions, StatementExecutionExceptions, IOException{
        IStatement ex3 = new CompoundStatement(new VariableDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ValueExpression(new BoolValue(false))),
                                new CompoundStatement(new IfStatement(new VariableExpression("a"),
                                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                        new AssignStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));
        runStatement(ex3);
    }

    private void runStatement(IStatement statement) throws ExpressionEvaluationExceptions, ADTExceptions, StatementExecutionExceptions, IOException {
        MyIStack<IStatement> executionStack = new MyStack<>();
        MyIDictionary<String, Value> symbolTable = new MyDictionary<>();
        MyIList<Value> output = new MyList<>();

        ProgramState state = new ProgramState(executionStack, symbolTable, output,statement);

        IRepository repository = new Repository(state);
        Controller controller = new Controller(repository);

        System.out.println("Do you want to display the steps?[Y/n]");
        Scanner readOption = new Scanner(System.in);
        String option = readOption.next();
        controller.setDisplayFlag(Objects.equals(option, "Y"));

        controller.allSteps();
        System.out.println("Result is" + state.getOut().toString().replace('[', ' ').replace(']', ' '));
    }

}
