#include <iostream>
#include "Service.h"
#include "UI.h"

int main() {
    Service service;
    UI ui(service);

    ui.run();

    return 0;
}
