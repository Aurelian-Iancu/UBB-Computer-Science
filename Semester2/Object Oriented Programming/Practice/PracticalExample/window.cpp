#include "window.h"
#include "ui_Window.h"
#include "QMessageBox"
#include <sstream>


Window::Window(Service& service,User* user, QWidget *parent) :
        service(service),user(user), QWidget(parent), ui(new Ui::Window) {

    ui->setupUi(this);
    this->window()->setWindowTitle(QString::fromStdString( user->getName() + " " + user->getType()));
    this->populateList();
    this->service.addObserver(this);
    this->update();
    this->connectSignalsAndSlots();
    this->lockResolveButton();

}

Window::~Window() {
    delete ui;
}

void Window::update() {
    populateList();
}

void Window::populateList() {
    this->ui->issueListWidget->clear();
    for(auto& issue: this->service.getAllIssuesSorted())
    {
        this->ui->issueListWidget->addItem(QString::fromStdString(issue.toString()));
    }
}

void Window::connectSignalsAndSlots() {
    QObject::connect(this->ui->addPushButton, &QPushButton::clicked, this, &Window::addIssue);
    QObject::connect(this->ui->removePushButton, &QPushButton::clicked, this, &Window::removeIssue);
    QObject::connect(this->ui->resolvePushButton,&QPushButton::clicked,this,&Window::resolveIssue);
}

void Window::addIssue() {
    std::string description = this->ui->addLineEdit->text().toStdString();
    try
    {
        if(description.empty())
            throw "The description is empty!";
        else if(this->user->getType() == "programmer")
        {
            throw "Only the testers cand add an issue!";
        }
        else
        {
            this->service.addIssueService(description, "open", user->getName(), "None");
            this->populateList();
        }

    }
    catch(const char *msg) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(msg);
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
}

void Window::removeIssue() {
    std::string description = this->ui->removeLineEdit->text().toStdString();
    try
    {
        if(description.empty())
            throw "The description is empty!";
        else
        {
            for(auto& issue: this->service.getAllIssuesService())
            {
                if(issue.getDescription() == description)
                {
                    if(issue.getStatus() == "closed")
                    {
                        this->service.removeIssueService(description);
                        this->populateList();
                    }
                    else
                    {
                        throw "You can remove only the closed issuse!";
                    }
                }
            }
        }
    }
    catch(const char *msg) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(msg);
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
}

void Window::resolveIssue() {
    std::stringstream x(ui->issueListWidget->currentItem()->text().toStdString());

    std::string desc, status, reporter, solver;

    getline(x, desc, ' ');
    getline(x, status, ' ');
    getline(x, reporter, ' ');
    getline(x, solver, '\n');

    if(user->getType() == "programmer")
    {
        if(status == "open")
        {
            service.updateIssueService(desc, desc, "closed", reporter, this->user->getName());

            populateList();
        }
    }
}

void Window::lockResolveButton() {
    if(user->getType() == "tester")
        this->ui->resolvePushButton->setEnabled(false);
}




