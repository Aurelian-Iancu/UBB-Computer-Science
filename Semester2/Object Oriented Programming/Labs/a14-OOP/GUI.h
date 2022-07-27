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
#include "QShortcut"
#include "QTableView"


class MovieTableModel: public QAbstractTableModel
{
private:
    std::vector<Movie> movies;

public:
    explicit MovieTableModel(std::vector<Movie> v);

    int rowCount(const QModelIndex& parent = QModelIndex()) const;

    int columnCount(const QModelIndex& parent = QModelIndex()) const;

    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;

    void update();
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
    QPushButton* undoButton;
    QPushButton* redoButton;

    QShortcut* shortcutUndo;
    QShortcut* shortcutRedo;

    void initAdminGUI();
    void populateList();
    void connectSignalsAndSlots();
    void addMovie();
    void removeMovie();
    void updateMovie();
    int getSelectedIndex();
    void undoGUI();
    void redoGUI();

    QWidget* chartWindow;

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
    QPushButton* tableViewButton;

    QRadioButton* csvButton;
    QRadioButton* htmlButton;

    QTableView* playlistTable;
    MovieTableModel* playlistTableModel;
    QWidget* playlistWindow;

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
    void createTable();


public:
    explicit UserGUI(QWidget* parent, Service& serv, UserService& userserv, MovieValidator& validator1);

    ~UserGUI() override;
};
