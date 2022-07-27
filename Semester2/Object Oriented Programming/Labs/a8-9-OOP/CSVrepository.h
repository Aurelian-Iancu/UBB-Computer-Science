#include "userRepository.h"

class CSVRepo: public UserRepository{
public:
    CSVRepo(const std::vector<Movie>& playlist, const std::string& userFilename);

    std::vector<Movie>& getAllUsersRepo() override;

    unsigned int getSize() override;

    unsigned int getCapacity() override;

    void addUserRepo(const Movie& movie) override;

    void removeUserRepo(unsigned int index) override;

    ///Function used to find a Movie by its title in the repository
    int findByTitle(const std::string &title) override;

    void writeToFile() override;

    std::string& getFilename() override;

    ~CSVRepo();
};

