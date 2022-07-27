#include "repository.h"
#include "userRepository.h"

class UndoRedoAction
{
public:
    virtual void undo() = 0;
    virtual void redo() = 0;
    virtual ~UndoRedoAction() = default;
};

class UndoRedoAdd: public UndoRedoAction
{
private:
    Movie addedMovie;
    Repository& repo;
public:
    UndoRedoAdd(const Movie& movie, Repository& newRepo);
    void undo() override;
    void redo() override;
    ~UndoRedoAdd() = default;
};

class UndoRedoRemove: public UndoRedoAction
{
private:
    Movie removedMovie;
    Repository& repo;
public:
    UndoRedoRemove(const Movie& movie, Repository& newRepo);
    void undo() override;
    void redo() override;
    ~UndoRedoRemove() = default;
};

class UndoRedoUpdate: public UndoRedoAction {
private:
    Movie oldMovie;
    Movie newMovie;
    Repository& repo;
public:
    UndoRedoUpdate(const Movie& oldMovie, const Movie& newMovie, Repository& newRepo);
    void undo () override;
    void redo() override;
    ~UndoRedoUpdate() override = default;
};