#include <QVBoxLayout>
#include <QFormLayout>
#include <QErrorMessage>
#include <QMessageBox>
#include <windows.h>
#include <shellapi.h>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
#include "GUI.h"

MovieTableModel::MovieTableModel(std::vector<Movie> v) {
    this->movies = v;
}

int MovieTableModel::rowCount(const QModelIndex &parent) const {
    return this->movies.size();
}

int MovieTableModel::columnCount(const QModelIndex &parent) const {
    return 5;
}

QVariant MovieTableModel::data(const QModelIndex &index, int role) const {
    int row = index.row();
    int column = index.column();
    Movie movie = this->movies[row];
    if (role == Qt::DisplayRole || role == Qt::EditRole){
        switch (column) {
            case 0:
                return QString::fromStdString(movie.getTitle());
            case 1:
                return QString::fromStdString(movie.getGenre());
            case 2:
                return QString::fromStdString(std::to_string(movie.getYear()));
            case 3:
                return QString::fromStdString(std::to_string(movie.getNumberOfLikes()));
            case 4:
                return QString::fromStdString(movie.getTrailer());
            default:
                break;
        }
    }
    return QVariant();
}

QVariant MovieTableModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole) {
        if (orientation == Qt::Horizontal) {
            switch (section) {
                case 0:
                    return QString("Title");
                case 1:
                    return QString("Genre");
                case 2:
                    return QString("Year of release");
                case 3:
                    return QString("Number of likes");
                case 4:
                    return QString("Trailer");
                default:
                    break;
            }
        }
    }
    return QVariant();
}

GUI::GUI(Service &serv, UserService &userService, MovieValidator &movieValidator, Repository &repo) :
        service{serv}, userService{userService}, movieValidator{movieValidator}, repository{repo}
{
    this->titleWidget = new QLabel(this);
    this->adminButton = new QPushButton(this);
    this->userButton = new QPushButton(this);
    this->initGUI();
    this->connectSignalsAndSlots();
}

void GUI::initGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#0b303f>Tinder movies!Hello Gabi! <br> Select your mode!</font></p>");
    titleFont.setBold(true);
    titleFont.setPointSize(10);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);
    this->adminButton->setText("Admin mode");
    layout->addWidget(this->adminButton);
    this->userButton->setText("User mode");
    layout->addWidget(this->userButton);
    this->setLayout(layout);
    this->setStyleSheet("background-color:#fce7cb");
}

void GUI::connectSignalsAndSlots() {
    QObject::connect(this->adminButton, &QPushButton::clicked, this, &GUI::showAdmin);
    QObject::connect(this->userButton, &QPushButton::clicked, this, &GUI::showUser);
}

GUI::~GUI() = default;

void GUI::showAdmin() {
    this->service.clearUndoRedo();
    auto* admin = new AdminGUI(this, this->service, this->movieValidator, this->repository);
    admin->show();
}

AdminGUI::AdminGUI(QWidget *parent, Service &serv, MovieValidator &validator1, Repository &repo):
        service{serv}, validator{validator1}, repository{repo}{
    this->titleWidget = new QLabel(this);
    this->movieListWidget = new QListWidget{};
    this->titleLineEdit = new QLineEdit{};
    this->genreLineEdit = new QLineEdit{};
    this->yearLineEdit = new QLineEdit{};
    this->likesLineEdit = new QLineEdit{};
    this->trailerLineEdit = new QLineEdit{};

    this->addButton = new QPushButton("Add");
    this->removeButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");
    this->undoButton = new QPushButton("Undo");
    this->redoButton = new QPushButton("Redo");

    this->shortcutUndo = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Z), this);
    this->shortcutRedo = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Y), this);

    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initAdminGUI();
    this->populateList();
    this->connectSignalsAndSlots();
}

void AdminGUI::initAdminGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#0b303f>ADMIN MODE</font></p>");
    titleFont.setBold(true);
    titleFont.setPointSize(10);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    layout->addWidget(this->movieListWidget);

    auto * movieDetailsLayout = new QFormLayout{};
    movieDetailsLayout->addRow("Title", this->titleLineEdit);
    movieDetailsLayout->addRow("Genre", this->genreLineEdit);
    movieDetailsLayout->addRow("Year of release", this->yearLineEdit);
    movieDetailsLayout->addRow("Number of likes", this->likesLineEdit);
    movieDetailsLayout->addRow("Trailer", this->trailerLineEdit);
    layout->addLayout(movieDetailsLayout);

    auto* buttonsLayout = new QGridLayout{};
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->removeButton, 0, 1);
    buttonsLayout->addWidget(this->updateButton, 0, 2);
    buttonsLayout->addWidget(this->undoButton, 1, 0);
    buttonsLayout->addWidget(this->redoButton, 1, 2);

    layout->addLayout(buttonsLayout);

}

AdminGUI::~AdminGUI() = default;

void AdminGUI::populateList() {
    this->movieListWidget->clear();
    std::vector<Movie> allMovies = this->service.getAllService();
    for(Movie& movie: allMovies)
        this->movieListWidget->addItem(QString::fromStdString(movie.getTitle()));
}

void AdminGUI::connectSignalsAndSlots() {
    QObject::connect(this->movieListWidget, &QListWidget::itemSelectionChanged, [this]() {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return ;
        Movie movie = this->service.getAllService()[selectedIndex];
        this->titleLineEdit->setText(QString::fromStdString(movie.getTitle()));
        this->genreLineEdit->setText(QString::fromStdString(movie.getGenre()));
        this->yearLineEdit->setText(QString::fromStdString(std::to_string(movie.getYear())));
        this->likesLineEdit->setText(QString::fromStdString(std::to_string(movie.getNumberOfLikes())));
        this->trailerLineEdit->setText(QString::fromStdString(movie.getTrailer()));
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminGUI::addMovie);
    QObject::connect(this->removeButton, &QPushButton::clicked, this, &AdminGUI::removeMovie);
    QObject::connect(this->updateButton, &QPushButton::clicked, this, &AdminGUI::updateMovie);
    QObject::connect(this->undoButton, &QPushButton::clicked, this, &AdminGUI::undoGUI);
    QObject::connect(this->redoButton, &QPushButton::clicked, this, &AdminGUI::redoGUI);

    QObject::connect(this->shortcutUndo, &QShortcut::activated, this, &AdminGUI::undoGUI);
    QObject::connect(this->shortcutRedo, &QShortcut::activated, this, &AdminGUI::redoGUI);
}

void AdminGUI::addMovie() {
    std::string title = this->titleLineEdit->text().toStdString();
    std::string genre = this->genreLineEdit->text().toStdString();
    std::string yearS = this->yearLineEdit->text().toStdString();
    std::string likeS = this->likesLineEdit->text().toStdString();
    std::string trailer = this->trailerLineEdit->text().toStdString();
    int year, likes;

    try {
        this->validator.validateTitle(title);
        this->validator.validateGenre(genre);
        this->validator.validateYearString(yearS);
        year = std::stoi(yearS);
        this->validator.validateYear(year);
        this->validator.validateLikesString(likeS);
        likes = std::stoi(likeS);
        this->validator.validateYear(likes);
        this->validator.validateTrailer(trailer);
        this->service.addService(title, genre, year, likes, trailer);
        this->titleLineEdit->clear();
        this->genreLineEdit->clear();
        this->yearLineEdit->clear();
        this->likesLineEdit->clear();
        this->trailerLineEdit->clear();
        this->populateList();
    }
    catch (ValidationException &ve)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ve.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepositoryException& re) {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at adding movie!");
        error->exec();
    }
}

void AdminGUI::removeMovie()
{
    try{
        std::string title = this->titleLineEdit->text().toStdString();
        this->validator.validateTitle(title);
        this->service.removeService(title);
        this->populateList();
    }
    catch (ValidationException &ve)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ve.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepositoryException& re) {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at deleting movie!");
        error->exec();
    }
}

void AdminGUI::updateMovie()
{
    int index = this->getSelectedIndex();
    try
    {
        if(index < 0)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText("No movie selected!");
            error->setWindowTitle("Selection error!");
            error->exec();
        }
        else
        {
            std::string oldTitle = this->service.getAllService()[index].getTitle();
            std::string newTitle = this->titleLineEdit->text().toStdString();
            std::string newGenre = this->genreLineEdit->text().toStdString();
            std::string yearS = this->yearLineEdit->text().toStdString();
            std::string likeS = this->likesLineEdit->text().toStdString();
            int year, likes;
            std::string newTrailer = this->trailerLineEdit->text().toStdString();
            this->validator.validateTitle(oldTitle);
            this->validator.validateTitle(newTitle);
            this->validator.validateGenre(newGenre);
            this->validator.validateYearString(yearS);
            year = stoi(yearS);
            likes = stoi(likeS);
            this->validator.validateYear(year);
            this->validator.validateYearLikes(likes);
            this->validator.validateTrailer(newTrailer);
            this->service.updateService(oldTitle, newTitle, newGenre, year, likes, newTrailer);
            this->populateList();
        }
    }
    catch (ValidationException &ve)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ve.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    }
    catch (RepositoryException& re) {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error at deleting movie!");
        error->exec();
    }
}

int AdminGUI::getSelectedIndex() {
    QModelIndexList selectedIndexes = this->movieListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->titleLineEdit->clear();
        this->genreLineEdit->clear();
        this->yearLineEdit->clear();
        this->likesLineEdit->clear();
        this->trailerLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void AdminGUI::undoGUI()
{
    try {
        this->service.undoLastAction();
        this->populateList();
    } catch (RepositoryException& re) {
        QMessageBox::critical(this, "Error", re.what());
    }
}

void AdminGUI::redoGUI() {
    try {
        this->service.redoLastAction();
        this->populateList();
    } catch (RepositoryException &re) {
        QMessageBox::critical(this, "Error", re.what());
    }
}

void GUI::showUser()
{
    auto* user = new UserGUI(this, this->service, this->userService, this->movieValidator);
    user->show();
}


UserGUI::UserGUI(QWidget *parent, Service &serv, UserService &userserv, MovieValidator &validator1): service{serv}, userService{userserv}, validator{validator1}
{
    this->titleWidget = new QLabel(this);
    this->movieListWidget = new QListWidget{};
    this->playListWidget = new QListWidget{};
    this->titleLineEdit = new QLineEdit{};
    this->genreLineEdit = new QLineEdit{};
    this->yearLineEdit = new QLineEdit{};
    this->likeLineEdit = new QLineEdit{};
    this->trailerLineEdit = new QLineEdit{};
    this->filterLineEdit = new QLineEdit{};
    this->removeLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add to the playlist");
    this->nextButton = new QPushButton("Next movie");
    this->removeButton = new QPushButton("Remove from playlist");
    this->filterButton = new QPushButton("Filter");
    this->openListButton = new QPushButton("Open file");
    this->tableViewButton = new QPushButton("Table View");
    this->csvButton = new QRadioButton("CSV");
    this->htmlButton = new QRadioButton("HTML");

    this->repoTypeSelected = false;
    this->filtered = false;
    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initUserGUI();
    this->populateMovieList();
    this->connectSignalsAndSlots();
}

UserGUI::~UserGUI() = default;

void UserGUI::initUserGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#0b303f>USER MODE <br> Select the type of file you want for saving your movies!</font></p>");
    titleFont.setBold(true);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    auto* radioButtonsLayout = new QGridLayout(this);
    radioButtonsLayout->addWidget(this->csvButton, 0, 0);
    radioButtonsLayout->addWidget(this->htmlButton, 1, 0);
    radioButtonsLayout->addWidget(this->openListButton, 0, 1);
    layout->addLayout(radioButtonsLayout);

    auto* listLayout = new QGridLayout(this);
    listLayout->addWidget(this->movieListWidget, 0, 0);
    listLayout->addWidget(this->playListWidget, 0, 1);
    layout->addLayout(listLayout);

    auto * movieDetailsLayout = new QFormLayout{};
    movieDetailsLayout->addRow("Title", this->titleLineEdit);
    movieDetailsLayout->addRow("Genre", this->genreLineEdit);
    movieDetailsLayout->addRow("Year of release", this->yearLineEdit);
    movieDetailsLayout->addRow("Number of likes", this->likeLineEdit);
    movieDetailsLayout->addRow("Trailer", this->trailerLineEdit);
    movieDetailsLayout->addRow(this->nextButton);
    movieDetailsLayout->addRow(this->addButton);
    movieDetailsLayout->addRow(this->tableViewButton);
    layout->addLayout(movieDetailsLayout);

    auto* removeLayout = new QHBoxLayout{};
    removeLayout->addWidget(this->removeButton);
    auto* removeLabel = new QLabel("Like?");
    removeLayout->addWidget(removeLabel);
    removeLayout->addWidget(this->removeLineEdit);


    layout->addLayout(removeLayout);

    auto *filterTitle = new QLabel("<p style='text-align:center'><br>Filter the available movies by genre</font></p>");
    layout->addWidget(filterTitle);

    auto *  filterDetailsLayout = new QFormLayout{};
    filterDetailsLayout->addRow("Genre", this->filterLineEdit);
    filterDetailsLayout->addRow(this->filterButton);
    layout->addLayout(filterDetailsLayout);

}

void UserGUI::createTable() {
    if(!this->repoTypeSelected)
    {
        QMessageBox::critical(this, "Error", "Please select the file type!");
        return;
    }
    this->playlistWindow = new QWidget{};
    auto* playlistWindowLayout = new QVBoxLayout(this->playlistWindow);
    this->playlistTable = new QTableView{};

    this->playlistTableModel = new MovieTableModel(this->userService.getAllUsersService());
    this->playlistTable->setModel(this->playlistTableModel);
    this->playlistTable->resizeColumnsToContents();
    this->playlistTable->resizeRowsToContents();
    playlistWindowLayout->addWidget(this->playlistTable);
    this->playlistWindow->resize(840, 720);
    this->playlistWindow->show();
}

void UserGUI::populateMovieList() {
    this->movieListWidget->clear();
    std::vector<Movie> allMovies = this->service.getAllService();
    for (Movie& movie: allMovies)
        this->movieListWidget->addItem(QString::fromStdString(movie.getTitle()));
}

int UserGUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->movieListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->titleLineEdit->clear();
        this->genreLineEdit->clear();
        this->yearLineEdit->clear();
        this->likeLineEdit->clear();
        this->trailerLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void UserGUI::connectSignalsAndSlots() {
    QObject::connect(this->movieListWidget, &QListWidget::itemClicked, [this]() {
        std::string movieName = this->movieListWidget->selectedItems().at(0)->text().toStdString();
        int index = this->service.findByTitleService(movieName);
        Movie movie = this->service.getAllService()[index];
        this->titleLineEdit->setText(QString::fromStdString(movie.getTitle()));
        this->genreLineEdit->setText(QString::fromStdString(movie.getGenre()));
        this->yearLineEdit->setText(QString::fromStdString(std::to_string(movie.getYear())));
        this->likeLineEdit->setText(QString::fromStdString(std::to_string(movie.getNumberOfLikes())));
        this->trailerLineEdit->setText(QString::fromStdString(movie.getTrailer()));
        ShellExecuteA(NULL, NULL, "chrome.exe", movie.getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
    });

    QObject::connect(this->csvButton, &QRadioButton::clicked, [this]() {
        this->userService.repositoryType("csv");
        this->repoTypeSelected = true;
    });

    QObject::connect(this->htmlButton, &QRadioButton::clicked, [this]() {
        this->userService.repositoryType("html");
        this->repoTypeSelected = true;
    });

    QObject::connect(this->openListButton, &QPushButton::clicked, [this]() {
        if (!this->repoTypeSelected) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Warning);
            error->setText("Please select the type of file you want!");
            error->setWindowTitle("File type warning!");
            error->exec();
        } else {
            std::string link = std::string("start ").append(this->userService.getFileService());
            system(link.c_str());
        }
    });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &UserGUI::addMovie);
    QObject::connect(this->filterButton, &QPushButton::clicked, this, &UserGUI::filterMovie);
    QObject::connect(this->nextButton, &QPushButton::clicked, this, &UserGUI::next);
    QObject::connect(this->removeButton, &QPushButton::clicked, this, &UserGUI::removeMovie);

    QObject::connect(this->tableViewButton, &QPushButton::clicked, this, &UserGUI::createTable);
}

void UserGUI::populatePlayList() {
    this->playListWidget->clear();
    std::vector<Movie> allMovies = this->userService.getAllUsersService();
    for (Movie& movie: allMovies)
        this->playListWidget->addItem(QString::fromStdString(movie.getTitle()));
}

void UserGUI::addMovie() {
    if (!this->repoTypeSelected) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Warning);
        error->setText("Please select the type of file you want!");
        error->setWindowTitle("File type warning!");
        error->exec();
    }
    else
    {
        std::string title = this->titleLineEdit->text().toStdString();
        std::string genre = this->genreLineEdit->text().toStdString();
        std::string yearS = this->yearLineEdit->text().toStdString();
        std::string likeS = this->likeLineEdit->text().toStdString();
        std::string trailer = this->trailerLineEdit->text().toStdString();
        int year, likes;
        try
        {
            this->validator.validateTitle(title);
            this->validator.validateGenre(genre);
            this->validator.validateYearString(yearS);
            year = stoi(yearS);
            this->validator.validateYear(year);
            this->validator.validateLikesString(likeS);
            likes = stoi(likeS);
            this->validator.validateYearLikes(likes);
            this->validator.validateTrailer(trailer);
            Movie movie = Movie(title, genre, year, likes, trailer);
            this->userService.addUserService(movie);
            if (!this->filtered)
                this->populateMovieList();
            else
                this->playListWidget->addItem(this->movieListWidget->takeItem(this->getSelectedIndex()));
            this->populatePlayList();
        }
        catch (ValidationException& exc) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(exc.what());
            error->setWindowTitle("Invalid input!");
            error->exec();
        } catch (RepositoryException& re) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(re.what());
            error->setWindowTitle("Error at adding movie!");
            error->exec();
        }
        catch(UserException& ue)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(ue.what());
            error->setWindowTitle("Error adding movie!");
            error->exec();

        }
    }
}

void UserGUI::filterMovie(){
    try {
        std::string genreFilter = this->filterLineEdit->text().toStdString();
        if (genreFilter.empty()) {
            this->filtered = false;
            this->populateMovieList();
        } else {
            this->validator.validateString(genreFilter);
            std::vector<Movie> validMovies;
            this->service.getFiltered(validMovies, genreFilter);
            if (validMovies.empty()) {
                std::string error;
                error += std::string("The list of valid movies is empty!");
                if(!error.empty())
                    throw UserException(error);
            } else {
                this->filtered = true;
                this->movieListWidget->clear();
                for (Movie& movie: validMovies)
                    this->movieListWidget->addItem(QString::fromStdString(movie.getTitle()));
                this->titleLineEdit->setText(QString::fromStdString(validMovies.begin()->getTitle()));
                this->genreLineEdit->setText(QString::fromStdString(validMovies.begin()->getGenre()));
                this->yearLineEdit->setText(QString::fromStdString(std::to_string(validMovies.begin()->getYear())));
                this->likeLineEdit->setText(QString::fromStdString(std::to_string(validMovies.begin()->getNumberOfLikes())));
                this->trailerLineEdit->setText(QString::fromStdString(validMovies.begin()->getTrailer()));
                ShellExecuteA(NULL, NULL, "chrome.exe", validMovies.begin()->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
            }
        }
    } catch (ValidationException& ve) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ve.what());
        error->setWindowTitle("Validation error!");
        error->exec();
    } catch (UserException& ue) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ue.what());
        error->setWindowTitle("Filter error!");
        error->exec();
    }
}

void UserGUI::next()
{

    std::string genreFilter = this->filterLineEdit->text().toStdString();
    std::vector<Movie> validMovies;
    int goodIndex;

    std::string title = this->titleLineEdit->text().toStdString();
    std::string genre = this->genreLineEdit->text().toStdString();
    std::string yearS = this->yearLineEdit->text().toStdString();
    std::string likeS = this->likeLineEdit->text().toStdString();
    std::string trailer = this->trailerLineEdit->text().toStdString();
    int year, likes;

    try {

        this->validator.validateTitle(title);
        this->validator.validateGenre(genre);
        this->validator.validateYearString(yearS);
        year = stoi(yearS);
        this->validator.validateYear(year);
        this->validator.validateLikesString(likeS);
        likes = stoi(likeS);
        this->validator.validateYearLikes(likes);
        this->validator.validateTrailer(trailer);
        if (genreFilter.empty()) {
            validMovies = this->service.getAllService();
            title = this->titleLineEdit->text().toStdString();
            for (int index = 0; index < validMovies.size(); index++) {
                if (validMovies[index].getTitle() == title) {
                    goodIndex = index;
                    break;
                }
            }
            if (validMovies.size() - 1 == goodIndex)
                goodIndex = 0;
            else
                goodIndex++;

            this->titleLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTitle()));
            this->genreLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getGenre()));
            this->yearLineEdit->setText(QString::fromStdString(std::to_string(validMovies[goodIndex].getYear())));
            this->likeLineEdit->setText(
                    QString::fromStdString(std::to_string(validMovies[goodIndex].getNumberOfLikes())));
            this->trailerLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTrailer()));
            ShellExecuteA(NULL, NULL, "chrome.exe", validMovies[goodIndex].getTrailer().c_str(), NULL,
                          SW_SHOWMAXIMIZED);

        } else {

            this->service.getFiltered(validMovies, genreFilter);
            if (validMovies.empty()) {
                validMovies = this->service.getAllService();
                title = this->titleLineEdit->text().toStdString();
                for (int index = 0; index < validMovies.size(); index++) {
                    if (validMovies[index].getTitle() == title) {
                        goodIndex = index;
                        break;
                    }
                }
                if (validMovies.size() - 1 == goodIndex)
                    goodIndex = 0;
                else
                    goodIndex++;

                this->titleLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTitle()));
                this->genreLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getGenre()));
                this->yearLineEdit->setText(QString::fromStdString(std::to_string(validMovies[goodIndex].getYear())));
                this->likeLineEdit->setText(
                        QString::fromStdString(std::to_string(validMovies[goodIndex].getNumberOfLikes())));
                this->trailerLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTrailer()));
                ShellExecuteA(NULL, NULL, "chrome.exe", validMovies[goodIndex].getTrailer().c_str(), NULL,
                              SW_SHOWMAXIMIZED);

            } else {
                title = this->titleLineEdit->text().toStdString();
                for (int index = 0; index < validMovies.size(); index++) {
                    if (validMovies[index].getTitle() == title) {
                        goodIndex = index;
                        break;
                    }
                }
                if (validMovies.size() - 1 == goodIndex)
                    goodIndex = 0;
                else
                    goodIndex++;

                this->titleLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTitle()));
                this->genreLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getGenre()));
                this->yearLineEdit->setText(QString::fromStdString(std::to_string(validMovies[goodIndex].getYear())));
                this->likeLineEdit->setText(
                        QString::fromStdString(std::to_string(validMovies[goodIndex].getNumberOfLikes())));
                this->trailerLineEdit->setText(QString::fromStdString(validMovies[goodIndex].getTrailer()));
                ShellExecuteA(NULL, NULL, "chrome.exe", validMovies[goodIndex].getTrailer().c_str(), NULL,
                              SW_SHOWMAXIMIZED);
            }
        }
    }
    catch (ValidationException& exc) {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(exc.what());
        error->setWindowTitle("Invalid input!");
        error->exec();
    } catch (RepositoryException& re) {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(re.what());
        error->setWindowTitle("Error removing movie!");
        error->exec();
    }
    catch(UserException& ue)
    {
        auto* error = new QMessageBox();
        error->setIcon(QMessageBox::Critical);
        error->setText(ue.what());
        error->setWindowTitle("Error removing movie!");
        error->exec();

    }
}


void UserGUI::removeMovie() {
    if (!this->repoTypeSelected) {
        auto *error = new QMessageBox();
        error->setIcon(QMessageBox::Warning);
        error->setText("Please select the type of file you want!");
        error->setWindowTitle("File type warning!");
        error->exec();
    }
    else {
        std::string title = this->titleLineEdit->text().toStdString();
        std::string genre = this->genreLineEdit->text().toStdString();
        std::string yearS = this->yearLineEdit->text().toStdString();
        std::string likeS = this->likeLineEdit->text().toStdString();
        std::string trailer = this->trailerLineEdit->text().toStdString();
        std::string rate = this->removeLineEdit->text().toStdString();
        int year, likes;
        try {
            this->validator.validateTitle(title);
            this->validator.validateGenre(genre);
            this->validator.validateYearString(yearS);
            year = stoi(yearS);
            this->validator.validateYear(year);
            this->validator.validateLikesString(likeS);
            likes = stoi(likeS);
            this->validator.validateYearLikes(likes);
            this->validator.validateTrailer(trailer);
            this->validator.validateString(rate);
            Movie movie = Movie(title, genre, year, likes, trailer);
            bool isInPlaylist = false;
            for(auto& m: this->userService.getAllUsersService())
            {
                if(m == movie) {
                    if(rate == "Yes")
                    {
                        int index = this->service.findByTitleService(title);
                        int oldNumberOfLikes = this->service.getAllService()[index].getNumberOfLikes();
                        this->service.getAllService()[index].setNumberOfLikes(oldNumberOfLikes + 1);
                        this->service.writeToFileService();
                        this->userService.removeUserService(title);
                        this->populatePlayList();
                        this->populateMovieList();
                        this->removeLineEdit->clear();
                    }
                    else if(rate == "No")
                    {
                        this->userService.removeUserService(title);
                        this->populatePlayList();
                        this->removeLineEdit->clear();
                    }
                    else
                    {
                        auto *error = new QMessageBox();
                        error->setIcon(QMessageBox::Warning);
                        error->setText("Input Yes/No!");
                        error->setWindowTitle("Error removing movie");
                        error->exec();
                    }
                    isInPlaylist = true;
                }
            }
            if(!isInPlaylist)
            {
                auto *error = new QMessageBox();
                error->setIcon(QMessageBox::Warning);
                error->setText("The movie you want to delete is not in the playlist!");
                error->setWindowTitle("Error removing movie");
                error->exec();
            }
        }
        catch (ValidationException& exc) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(exc.what());
            error->setWindowTitle("Invalid input!");
            error->exec();
        } catch (RepositoryException& re) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(re.what());
            error->setWindowTitle("Error removing movie!");
            error->exec();
        }
        catch(UserException& ue)
        {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText(ue.what());
            error->setWindowTitle("Error removing movie!");
            error->exec();

        }
    }
}



