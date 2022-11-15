package repository;

import model.programState.ProgramState;

import java.util.List;

public interface IRepository {
    List<ProgramState> getProgramStates();
    void addProgram(ProgramState programState);
    ProgramState getCurrentState();
    void setProgramStates(List<ProgramState> programStates);
}
