#pragma once

#include "service.h"
#include "undoRedo.h"

typedef struct{
    Service* s;
}UI;

/// This function creates the ui dynamically
/// \param s The service
/// \return The UI
UI *createUI(Service* s);

/// Being dynamically alocated we must free it. This is the reason for which this function exists
/// \param ui The ui
void destroyUI(UI *ui);

/// This function is for printing the menu
void print_menu();

/// This function is for adding a product in the ui
/// \param ui The UI
int addUI(UI* ui, UndoRedo* ur);

/// This function is for removing a product in the ui
/// \param ui The UI
int removeUI(UI* ui, UndoRedo* ur);

/// This function is for updating a product from the ui
/// \param ui The UI
int updateUI(UI* ui, UndoRedo* ur);

/// This function prints all Products
void listAllProducts(UI* ui);

/// This function checks if a command is valid
/// \param command The command
/// \return 1 if it's valid 0 if not
int validCommand(int command);

/// This function transforms a string into a command(integer)
/// \param message The message "Input command: " which is constant
/// \return The integer command
int readIntegerNumber(const char* message);

/// This function is for the start of the program. We call it in main
void start(UI *ui);

/// This function solves the c functionality
/// \param ui The ui
/// \return 1 if we found something to print, 0 otherwise
int listSearchProductByCategory(UI* ui);

/// This function solves the b functionality
/// \param ui The ui
/// \return 1 if we found something to print, 0 otherwise
int listGivenString(UI* ui);

/// This function prints a dynamic vector
/// \param result The vector
/// \return 1 if we printed it, 0 otherwise
int printVector(Vector* result);
