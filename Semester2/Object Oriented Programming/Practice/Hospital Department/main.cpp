#include <iostream>
#include "Service.h"
#include "UI.h"

int main() {
    Service service;
    UI UI(service);

    UI.run();

    return 0;
}
