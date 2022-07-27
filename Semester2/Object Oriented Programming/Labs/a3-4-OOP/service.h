#pragma once
#include "repository.h"

typedef struct
{
    Repo* repo;
}Service;

/// This function is used to create a service for a repository
/// \param r The repository
/// \return The service
Service* createService(Repo* r);

/// This function is used to destroy a service
/// \param s The service
void destroyService(Service* s);

/// This function is used to add a Product in service
/// \param s The service
/// \param name The name of the product
/// \param category The category of the product
/// \param quantity The quantity of the product
/// \param date The date of the product
/// \return 1 if we managed to add it, 0 if the quantity is updated
int addService(Service* s, char* name, char* category, int quantity, int date);

/// Returns the repo of a service
/// \param s The service
/// \return The repository
Repo* getRepo(Service* s);

/// This function is used to remove a Product in service
/// \param s The service
/// \param name The name of the product
/// \param category The category of the product
/// \return 1 if it was remove, 0 if not
int removeService(Service* s, char* name, char* category);

/// This function is used to update a Product in service
/// \param s The service
/// \param name The name of the product
/// \param category The category of the product
/// \param newQuantity The new quantity of the product
/// \param newDate The new date of the product
/// \return 1 if it was updated, 0 if not
int updateService(Service* s, char* name, char* category, int newQuantity, int newDate);

/// This function is used to sort a vector using pointer function sort
/// \param result The vector which will be sorted
/// \param sort The sorting function
void sortVector(Vector* result, int(*sort)(Product* p1, Product* p2));

/// This function is used to filter all the products that have a quantity bigger than the filter
/// \param s The service
/// \param quantity The quantity filter
/// \param result The result vector
/// \param filter The filter pointer function
/// \return 1 if it was filtered, 0 if not
int filterVectorBonus(Service* s, int quantity, Vector* result,int (*filter)(Product* p, int quantity));

/// This function gets the filter and returns it to the UI
/// \param s The service
/// \param quantity The quantity
/// \param result The result vector
/// \return 1 if it was filtered, 0 if not
int getFilterBonus(Service* s, int quantity, Vector* result);

/// This function is used to filter the products which have a certain string in their name
/// \param s The service
/// \param filter The filter
/// \param result The result vector
/// \return 1 if it was filtered, 0 if not
int filterForPrinting(Service* s, char* filter, Vector* result);

/// This function is used for functionality c ordered ascending
/// \param s The service
/// \param category The category
/// \param expirationDate The expiration date
/// \param x The number of days until it expires
/// \param result The result vector
/// \return 1 if it filtered, 0 if not
int searchProductByCategoryAscending(Service* s, char* category, int expirationDate, int x, Vector* result);

/// This function is used for functionality c ordered descending
/// \param s The service
/// \param category The category
/// \param expirationDate The expiration date
/// \param x The number of days until it expires
/// \param result The result vector
/// \return 1 if it filtered, 0 if not
int searchProductByCategoryDescending(Service* s, char* category, int expirationDate, int x, Vector* result);


/// Here are some tests for the service
void testAddService();

void testDeleteService();

void testUpdateService();

void testService();