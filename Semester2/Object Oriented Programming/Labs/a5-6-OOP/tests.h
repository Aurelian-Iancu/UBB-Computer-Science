#pragma once

typedef Movie TElem;

class Tests
{
public:
    ///Tests for the domain
    void testsDomain();

    ///Tests for the admin service
    void testsAdminService();

    ///Tests for the vector
    void testsVector();

    ///Tests for the admin repository
    void testsAdminRepository();

    ///Tests for the user repository
    void testsUserRepository();

    ///Tests for the user service
    void testsUserService();

    void testsSort();
};
