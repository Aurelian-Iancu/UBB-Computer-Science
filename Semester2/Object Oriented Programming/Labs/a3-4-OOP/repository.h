#pragma once
#include "domain.h"
#include "dynamicArray.h"

typedef struct
{
    Vector* vector;
}Repo;

/// This function creates the repository
/// \param size The size of the repository
/// \param data The elements of the repository
/// \return The repository
Repo* createRepo();

/// Because our repo is dynamically allocated we must free the memory and here's the function that does the thing
/// \param r The repository
void destroyRepo(Repo* r);

/// This function checks if 2 Products have the same name and category(ID)
/// \param p1 The first product
/// \param p2 The second product
/// \return 1 if they have the same name and category, 0 otherwise
int sameId(Product* p1, Product* p2);

/// This function swaps 2 Products
/// \param a The first product
/// \param b The second product
void swapProducts(Product *a, Product *b);

/// This function gets the length of the repository
/// \param r The repository
/// \return The length of the repository
int getLengthRepo(Repo* r);

/// This function is created in order to get the product from a certain position in repo
/// \param r The repository
/// \param pos The position from the repository
/// \return The product from the position pos
Product* getProductOnPos(Repo * r, int pos);

/// This function finds a Product in the repo by his name and category
/// \param r The repository
/// \param name The name of the product
/// \param category The category of the products
/// \return 1 if it finds the Product, 0 otherwise
Product* findById(Repo* r, char* name, char* category);

/// This function adds a product to the repository
/// \param r The repository
/// \param p The product
/// \return 1 if the product was added, 0 if it already existed and the quantity was updated
int addRepo(Repo* r, Product* p);

/// This function removes a product from the repository if it exists
/// \param r The repository
/// \param name The name of the product
/// \param category The category of the product
/// \return 1 if the product is successfully removed, 0 otherwise
int removeRepo(Repo* r, char* name, char* category);

/// This function updates a product from the repository
/// \param r The repository
/// \param name The name of the product
/// \param category The category of the product
/// \param newQuantity The new quantity
/// \param newDate The new date
/// \return 1 if the product is successfully updated, 0 otherwise
int updateRepo(Repo* r, char* name, char* category, int newQuantity, int newDate);

/// This function gets the position of a product in the repository
/// \param r The repository
/// \param p The product
/// \return The position on which we can find the product p in the repository r
int getPosOfProduct(Repo* r, Product* p);


/// This function is for initializing the repo
void initProductRepoTest(Repo* r);

/// This function is used for testing the add function
void testAdd();

/// This function is for tests
void testRepo();
