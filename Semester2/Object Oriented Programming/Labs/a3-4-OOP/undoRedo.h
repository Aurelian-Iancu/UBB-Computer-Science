#pragma once
#include "dynamicArray.h"
#include "repository.h"

typedef struct
{
    Vector** undoList;
    int undoSize, undoCapacity;
    Vector** redoList;
    int redoSize, redoCapacity;
} UndoRedo;

/// This is for creating an UndoRedo instance
/// \return The UndoRedo instance
UndoRedo* createUndoRedo();

/// This is for destroying an UndoRedo instance
/// \param ur The UndoRedo
void destroyUndoRedo(UndoRedo* ur);

/// In this function we basically create the list of lists(we add to ur which is a stack the last operation state)
/// \param ur The UndoRedo
/// \param state The last performed operation
void addStateToUndo(UndoRedo* ur, Vector* state);

/// This function is the undo implementation which returns the last performed operation to the repo
/// \param ur The UndoRedo
/// \param repo The repo
/// \return 1 if the undo was performed, 0 if not
int undo(UndoRedo* ur, Repo* repo);

/// This function is the redo implementation which returns the last undone operation to the repo
/// \param ur The UndoRedo
/// \param repo The repo
/// \return 1 if the redo was performed, 0 if not
int redo(UndoRedo* ur, Repo* repo);

/// This function is used to clear the redo list. After we make a new operation we shouldn't be able to redo, only to undo
/// \param ur The UndoRedo
void clearRedoList(UndoRedo* ur);