#include "ui.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "undoRedo.h"

UI* createUI(Service *s)
{
    UI* ui = malloc(sizeof(UI));
    if(ui == NULL)
        return NULL;
    ui->s = s;

    return ui;

}

void destroyUI(UI *ui)
{
    if(ui == NULL)
        return;
    destroyService(ui->s);
    free(ui);

}

void print_menu()
{
    printf("\t\tThe menu of commands is:\n");
    printf("\tIf you want to add a product: 1\n");
    printf("\tIf you want to remove a product: 2\n");
    printf("\tIf you want to update a product: 3\n");
    printf("\tIf you want to print the products that contain a certain string: 4\n");
    printf("\tIf you want third functionality: 5\n");
    printf("\tIf you want to undo: 6\n");
    printf("\tIf you want to redo: 7\n");
    printf("\tIf you want to use the bonus filter: 8\n");
    printf("\tIf you want to exit the program: 0\n");

}

int validCommand(int command)
{
    if (command >= 0 && command <= 9)
        return 1;
    return 0;
}

int readIntegerNumber(const char* message)
{
    char s[16] = { 0 };
    int res = 0;
    int flag = 0;
    int r = 0;

    while (flag == 0)
    {
        printf(message);
        int scanf_result = scanf("%15s", s);

        r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
        flag = (r == 1);
        if (flag == 0)
            printf("Error reading number!\n");
    }
    return res;
}

int addUI(UI* ui, UndoRedo* ur)
{
    char name[50], category[10];
    int quantity = 0, date = 0 , scanfResult, res;

    fgetc(stdin); //clear the buffer

    printf("Name: ");
    fgets(name, 49, stdin);
    name[strlen(name) - 1]  = '\0';

    printf("Category: ");
    fgets(category, 9, stdin);
    category[strlen(category) - 1]  = '\0';

    printf("Quantity: ");
    scanfResult = scanf("%d", &quantity);

    printf("Date: ");
    scanfResult = scanf("%d", &date);

    Vector * copy = makeCopy(ui->s->repo->vector);
    res = addService(ui->s, name, category, quantity, date);

    if(res == 1)
    {
        addStateToUndo(ur, copy);
        clearRedoList(ur);
    }
    else
    {
        destroyVector(copy);
    }
    return res;
}

int removeUI(UI* ui, UndoRedo* ur)
{
    char name[50], category[10];
    int res;

    fgetc(stdin);

    printf("Name: ");
    fgets(name, 49, stdin);
    name[strlen(name) - 1]  = '\0';

    printf("Category: ");
    fgets(category, 9, stdin);
    category[strlen(category) - 1]  = '\0';

    Vector * copy = makeCopy(ui->s->repo->vector);
    res = removeService(ui->s, name, category);
    if(res == 1)
    {
        addStateToUndo(ur, copy);
        clearRedoList(ur);
    }
    else
    {
        destroyVector(copy);
    }
    return res;
}

int updateUI(UI* ui, UndoRedo* ur)
{
    char name[50], category[10];
    int newQuantity, newDate,scanfResult, res;

    fgetc(stdin); //clear the buffer

    printf("Name: ");
    fgets(name, 49, stdin);
    name[strlen(name) - 1]  = '\0';

    printf("Category: ");
    fgets(category, 9, stdin);
    category[strlen(category) - 1]  = '\0';

    printf("Quantity: ");
    scanfResult = scanf("%d", &newQuantity);

    printf("Date: ");
    scanfResult = scanf("%d", &newDate);

    Vector* copy = makeCopy(ui->s->repo->vector);
    res = updateService(ui->s, name, category, newQuantity, newDate);
    if(res == 1)
    {
        addStateToUndo(ur, copy);
        clearRedoList(ur);
    }
    else
    {
        destroyVector(copy);
    }
    return res;

}

int printVector(Vector* result)
{
    int i;
    for (i = 0; i < result->size; i++)
    {
        char representation[200];
        Product* p = (Product*)malloc(sizeof(Product));
        if (p == NULL)
            return 0;

        p = result->data[i];
        toString(p, representation);
        if (p != NULL)
            printf("%s\n", representation);
        else
            printf("no estate found...\n");
    }

    return 1;
}

int listGivenString(UI* ui)
{
    char filter[50];
    int filtered, printed;
    printf("filter: ");
    fgetc(stdin); // clear the buffer
    fgets(filter, 49, stdin);
    filter[strlen(filter) - 1] = '\0';

    Vector* result = createVector(getLengthRepo(ui->s->repo));
    if(result == NULL)
        return 0;

    filtered = filterForPrinting(ui->s, filter, result);
    if(result->size == 0 || filtered == 0)
        return 0;

    printed = printVector(result);
    if(printed == 0)
        return 0;

    destroyVector(result);

    return 1;
}


int listSearchProductByCategory(UI* ui)
{
    if(ui == NULL)
        return 0;

    char category[50];
    int expirationDate, x, scanfResult, searched, printed, sorted;


    fgetc(stdin);

    printf("Category: ");
    fgets(category, 9, stdin);
    category[strlen(category) - 1]  = '\0';

    printf("Expiration date: ");
    scanfResult = scanf("%d", &expirationDate);

    printf("X days close to the expiration date: ");
    scanfResult = scanf("%d", &x);

    printf("Ascending: 1, Descending: 2");
    scanfResult = scanf("%d", &sorted);

    Vector* result = createVector(getLengthRepo(ui->s->repo));
    if(result == NULL)
        return 0;

    if(sorted == 1)
    {
        searched = searchProductByCategoryAscending(ui->s, category, expirationDate, x, result);
        if(result->size == 0 || searched == 0)
            return 0;

        printed = printVector(result);
        if(printed == 0)
            return 0;
    }
    else if(sorted == 2)
    {
        searched = searchProductByCategoryDescending(ui->s, category, expirationDate, x, result);
        if(result->size == 0 || searched == 0)
            return 0;

        printed = printVector(result);
        if(printed == 0)
            return 0;
    }
    else
        return 0;

    destroyVector(result);

    return 1;
}

///Here is for bonus point
int listOtherFilter(UI* ui)
{
    int filter;
    int filtered, printed, scanfResult;
    printf("Filter: ");
    scanfResult = scanf("%d", &filter);

    Vector* result = createVector(getLengthRepo(ui->s->repo));
    if(result == NULL)
        return 0;

    filtered = getFilterBonus(ui->s, filter, result);
    if(result->size == 0 || filtered == 0)
        return 0;

    printed = printVector(result);
    if(printed == 0)
        return 0;

    destroyVector(result);

    return 1;
}


void start(UI* ui) {
    int command, res;
    UndoRedo* ur = createUndoRedo();

    while (1)
    {
        print_menu();
        command = readIntegerNumber("Input command: ");
        while (validCommand(command) == 0) {
            printf("Please input a valid command!\n");
            command = readIntegerNumber("Input command: ");
        }
        switch (command)

        {
            case 0:
            {
                destroyUndoRedo(ur);
                return;
            }
            case 1:
            {
                res = addUI(ui, ur);
                if (res == 1)
                    printf("Product successfully added!!\n");
                else
                    printf("The product already existed in the fridge! The quantity was updated.\n");
                break;
            }
            case 2:
            {
                res = removeUI(ui, ur);
                if(res == 1)
                    printf("Product successfully remove!\n");
                else
                    printf("The product you want does not exist in out list!\n");
                break;
            }
            case 3:
            {
                res = updateUI(ui, ur);
                if(res == 1)
                    printf("Product successfully updated!\n");
                else
                    printf("The product you want does not exist in our list!\n");
                break;
            }
            case 4:
            {
                res = listGivenString(ui);
                if(res == 0)
                    printf("There has been an error, possible no matches!\n");
                break;
            }
            case 5:
            {
                res = listSearchProductByCategory(ui);
                if(res == 0)
                    printf("There has been an error, possible no matches!\n");
                break;
            }
            case 6:
            {
                res = undo(ur, ui->s->repo);
                if(res == 0)
                    printf("You cant undo anymore!\n");
                else
                    printf("Undo successful!!\n");
                break;
            }
            case 7:
            {
                res = redo(ur, ui->s->repo);
                if (res == 0)
                    printf("You cant redo anymore!\n");
                else
                    printf("Redo successful\n");
                break;
            }
            case 8:
            {
                res = listOtherFilter(ui);
                if(res == 0)
                    printf("There has been an error, possible no matches!\n");
                break;
            }
        }
    }
}