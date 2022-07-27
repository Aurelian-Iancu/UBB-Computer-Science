

#include "undoRedo.h"

UndoRedoAdd::UndoRedoAdd(const Movie &movie, Repository &newRepo):addedMovie(movie), repo(newRepo) {

}

void UndoRedoAdd::undo() {
    int index = this->repo.findByTitle(this->addedMovie.getTitle());
    this->repo.removeRepo(index);
}

void UndoRedoAdd::redo() {
    this->repo.addRepo(this->addedMovie);
}

UndoRedoRemove::UndoRedoRemove(const Movie &movie, Repository &newRepo):removedMovie(movie), repo(newRepo) {

}

void UndoRedoRemove::undo() {
    this->repo.addRepo(this->removedMovie);
}

void UndoRedoRemove::redo() {
    int index = this->repo.findByTitle(this->removedMovie.getTitle());
    this->repo.removeRepo(index);
}

UndoRedoUpdate::UndoRedoUpdate(const Movie &oldMovie, const Movie &newMovie, Repository &newRepo)
:oldMovie(oldMovie), newMovie(newMovie), repo(newRepo){

}

void UndoRedoUpdate::undo() {
    int index = this->repo.findByTitle(this->newMovie.getTitle());
    this->repo.updateRepo(index, this->oldMovie);
}

void UndoRedoUpdate::redo() {
    int index = this->repo.findByTitle(this->oldMovie.getTitle());
    this->repo.updateRepo(index, this->newMovie);
}

