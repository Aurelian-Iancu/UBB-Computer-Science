#pragma once
#include <qwidget.h>
#include "movie.h"
#include <QListWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QPushButton>
#include <QRadioButton>
#include <QLabel>
#include "service.h"
#include "repository.h"
#include "userService.h"
#include "validators.h"


class DogListModel: public QAbstractListModel
{
private:
    Repository &repository;

public:
    explicit DogListModel(Repository& repo): repository{repo} {};

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;

    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};

class GUI: public QWidget
{
    Q_OBJECT
private:
    Service& service;
    UserService& userService;
    MovieValidator& movieValidator;
    Repository& repository;
    std::vector<Movie> movies;

    QLabel* titleWidget;
    QPushButton* adminButton;
    QPushButton* userButton;

    void initGUI();
    void showAdmin();
    void showUser();
    void connectSignalsAndSlots();
public:
    GUI(Service& serv, UserService& userService, MovieValidator& movieValidator, Repository& repo);

    ~GUI();
};

class AdminGUI: public QWidget
{
private:
    Service& service;
    MovieValidator& validator;
    Repository& repository;

    QLabel* titleWidget;

    QListWidget* movieListWidget;

    QLineEdit* titleLineEdit;
    QLineEdit* genreLineEdit;
    QLineEdit* yearLineEdit;
    QLineEdit* likesLineEdit;
    QLineEdit* trailerLineEdit;

    QPushButton* addButton;
    QPushButton* removeButton;
    QPushButton* updateButton;

    void initAdminGUI();
    void populateList();
    void connectSignalsAndSlots();
    void addMovie();
    void removeMovie();
    void updateMovie();
    int getSelectedIndex();

public:
    explicit AdminGUI(QWidget* parent, Service& serv, MovieValidator& validator1, Repository& repo);

    ~AdminGUI() override;
};


class UserGUI:public QWidget
{
private:
    Service& service;
    MovieValidator& validator;
    UserService& userService;

    QLabel* titleWidget;

    QListWidget* movieListWidget;
    QListWidget* playListWidget;
    QLineEdit* titleLineEdit;
    QLineEdit* genreLineEdit;
    QLineEdit* yearLineEdit;
    QLineEdit* likeLineEdit;
    QLineEdit* trailerLineEdit;
    QLineEdit* filterLineEdit;
    QLineEdit* removeLineEdit;

    QPushButton* addButton;
    QPushButton* nextButton;
    QPushButton* removeButton;
    QPushButton* filterButton;
    QPushButton* openListButton;

    QRadioButton* csvButton;
    QRadioButton* htmlButton;

    bool repoTypeSelected;
    bool filtered;
    void initUserGUI();
    void populateMovieList();
    void populatePlayList();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void addMovie();
    void filterMovie();
    void next();
    void removeMovie();


public:
    explicit UserGUI(QWidget* parent, Service& serv, UserService& userserv, MovieValidator& validator1);

    ~UserGUI() override;
};
