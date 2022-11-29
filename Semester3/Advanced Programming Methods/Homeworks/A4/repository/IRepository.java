package repository;

import exceptions.ADTExceptions;
import model.programState.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {
    List<ProgramState> getProgramStates();
    void addProgram(ProgramState programState);
    ProgramState getCurrentState();
    void setProgramStates(List<ProgramState> programStates);
    void logPrgStateExec() throws IOException, ADTExceptions;
}
