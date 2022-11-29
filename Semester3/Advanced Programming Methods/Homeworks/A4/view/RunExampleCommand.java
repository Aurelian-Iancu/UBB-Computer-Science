package view;

import controller.Controller;
import exceptions.ADTExceptions;
import exceptions.ExpressionEvaluationExceptions;
import exceptions.StatementExecutionExceptions;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

public class RunExampleCommand extends Command{
    private final Controller controller;

    public RunExampleCommand(String key, String description, Controller controller){
        super(key, description);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try{
            System.out.println("Display the steps?(yes/no)");
            Scanner option = new Scanner(System.in);
            String optionString = option.next();
            controller.setDisplayFlag(Objects.equals(optionString, "yes"));
            controller.allSteps();
        }catch(ExpressionEvaluationExceptions | ADTExceptions | StatementExecutionExceptions | IOException exception){
            System.out.println(exception.getMessage());
        }
    }
}
