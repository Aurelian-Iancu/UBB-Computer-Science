#include "undoRedo.h"
#include <stdlib.h>
#include <assert.h>

UndoRedo* createUndoRedo()
{
    UndoRedo* ur = (UndoRedo*)malloc(sizeof(UndoRedo));
    if (ur == NULL)
        return NULL;

    ur->undoCapacity = 2;
    ur->undoList = (Vector**)malloc(ur->undoCapacity * sizeof(Vector*));
    if (ur->undoList == NULL)
    {
        free(ur);
        return NULL;
    }
    ur->undoSize = 0;

    ur->redoCapacity = 2;
    ur->redoList = (Vector**)malloc(ur->redoCapacity * sizeof(Vector*));
    if (ur->redoList == NULL)
    {
        free(ur->undoList);
        free(ur);
        return NULL;
    }
    ur->redoSize = 0;

    return ur;
}

void destroyUndoRedo(UndoRedo* ur)
{
    if (ur == NULL)
        return;

    int i;
    for (i = 0; i < ur->undoSize; i++)
    {
        destroyVector(ur->undoList[i]);
    }
    free(ur->undoList);

    for (i = 0; i < ur->redoSize; i++)
    {
        destroyVector(ur->redoList[i]);
    }
    free(ur->redoList);

    free(ur);
}

void resizeUndoList(UndoRedo* ur)
{
    if (ur == NULL)
        return;

    ur->undoCapacity *= 2;
    Vector** aux =(Vector**)realloc(ur->undoList, ur->undoCapacity * sizeof(Vector*));
    if (aux == NULL)
        return;

    ur->undoList = aux;
}

void resizeRedoList(UndoRedo* ur)
{
    if (ur == NULL)
        return;

    ur->redoCapacity *= 2;
    Vector** aux = (Vector**)realloc(ur->redoList, ur->redoCapacity * sizeof(Vector*));
    if (aux == NULL)
        return;

    ur->redoList = aux;
}

void addStateToUndo(UndoRedo* ur, Vector* state)
{
    if (ur == NULL || state == NULL)
        return;

    if (ur->undoSize == ur->undoCapacity)
        resizeUndoList(ur);

    ur->undoList[ur->undoSize] = state;
    ur->undoSize++;
}

void addStateToRedo(UndoRedo* ur, Vector* state)
{
    if (ur == NULL || state == NULL)
        return;

    if (ur->redoSize == ur->redoCapacity)
        resizeRedoList(ur);

    ur->redoList[ur->redoSize] = state;
    ur->redoSize++;
}

void clearRedoList(UndoRedo* ur)
{
    if (ur->redoList == NULL)
        return;

    int i;
    for (i = 0; i < ur->redoSize; i++)
    {
        destroyVector(ur->redoList[i]);
        ur->redoList[i] = NULL;
    }

    ur->redoSize = 0;
}

int undo(UndoRedo* ur, Repo* repo)
{
    if (ur == NULL || ur->undoList == NULL)
        return 0;

    if (ur->undoSize == 0)
        return 0;

    Vector* res = ur->undoList[ur->undoSize - 1];
    ur->undoList[ur->undoSize - 1] = NULL;
    ur->undoSize--;
    addStateToRedo(ur, makeCopy(repo->vector));
    destroyVector(repo->vector);
    repo->vector = res;

    return 1;
}

int redo(UndoRedo* ur, Repo* repo)
{
    if (ur == NULL || ur->redoList == NULL)
        return 0;

    if (ur->redoSize == 0)
        return 0;

    Vector* res = ur->redoList[ur->redoSize - 1];
    ur->redoList[ur->redoSize - 1] = NULL;
    ur->redoSize--;
    addStateToUndo(ur, makeCopy(repo->vector));
    destroyVector(repo->vector);
    repo->vector = res;

    return 1;
}