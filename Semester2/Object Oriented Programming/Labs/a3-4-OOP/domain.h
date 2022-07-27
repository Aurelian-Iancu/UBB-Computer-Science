#pragma once

typedef struct{
    char* name;
    char* category;
    int quantity;
    int date;
}Product;

/// This is a function for creating a product
/// \param name The name of the product
/// \param category The category of the product
/// \param quantity The quantity of the product
/// \param date The date of the product
/// \return The product
Product* createProduct(char* name, char* category, int quantity, int date);

/// Because our product is dynamically allocated we must free the memory and here's the function that does the thing
/// \param p The product that we want to free
void destroyProduct(Product* p);

/// This function gets the name of a product
/// \param p The product
/// \return The name of the product
const char* getName(Product* p);

/// This function gets the category of a product
/// \param p The product
/// \return The category of the product
const char* getCategory(Product* p);

/// This function gets the quantity of a product
/// \param p The product
/// \return The quantity of the product
int getQuantity(Product* p);

/// This function gets the date of a product
/// \param p The product
/// \return The date of the product
int getDate(Product* p);

/// /// This function sets the name of the product with another one
/// \param p The product
/// \param name The name of the product
void setName(Product* p, char* name);

/// /// This function sets the category of the product with another one
/// \param p The product
/// \param name The category of the product
void setCategory(Product* p, char* category);

/// This function sets the quantity of the product with another one
/// \param p The product
/// \param otherQuantity The other quantity
void setQuantity(Product* p, int otherQuantity);

/// This function sets the date of the product with another one
/// \param p The product
/// \param otherDate THe other date
void setDate(Product* p, int otherDate);

/// This function works like an str for the struct Product
/// \param p The product
/// \param str The format in which we want to print a product
void toString(Product* p, char str[]);

/// This function is for tests
void testProduct();

