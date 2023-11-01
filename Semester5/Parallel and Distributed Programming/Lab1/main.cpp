#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <thread>
#include <mutex>
#include <random>
#include <chrono>

using namespace std;

typedef struct
{
    int serialNumber;
    int amount;
    int sourceId;
    int destinationId;
} Operation;

typedef struct
{
    int accountId;
    int initialBalance;
    int currentBalance;
    mutex *mtx;
    vector<Operation> log;
} Account;

const string ACCOUNTS_FILE_PATH = "accounts.txt";

int currentSerialNumber = 0;
int threadsCount;
unordered_map<int, Account> accounts;
vector<int> accountIds;
vector<Operation> operations;

bool checkPassed = true;
mutex checkMutex;

void readAccountsFromFile(string filePath)
{
    ifstream inputFile(filePath);

    if (!inputFile.is_open())
    {
        cerr << "Error: Unable to open the file " << filePath << endl;
        return;
    }

    while (inputFile)
    {
        int accountId, balance;
        inputFile >> accountId >> balance;

        if (!inputFile.fail())
        {
            Account account;
            account.accountId = accountId;
            account.initialBalance = balance;
            account.currentBalance = balance;
            account.mtx = new mutex;
            accounts[accountId] = account;

            accountIds.push_back(accountId);
        }
    }

    inputFile.close();
}

int generateRandomNumberInRange(int min, int max)
{
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}

int getRandomAccount()
{
    return accountIds[generateRandomNumberInRange(0, accounts.size() - 1)];
}

int getRandomAmount()
{
    return generateRandomNumberInRange(10, 30);
}

void generateRandomOperations(int size)
{
    for (int i = 0; i < size; i++)
    {
        Operation operation;

        int sourceId = getRandomAccount();
        int destinationId = getRandomAccount();
        while (sourceId == destinationId)
        {
            destinationId = getRandomAccount();
        }
        int amount = getRandomAmount();

        operation.sourceId = sourceId;
        operation.destinationId = destinationId;
        operation.amount = amount;
        operation.serialNumber = ++currentSerialNumber;

        operations.push_back(operation);
    }
}

void performConsistencyCheck()
{
    for (auto &entry : accounts)
    {
        entry.second.mtx->lock();

        Account &account = entry.second;
        int calculatedBalance = account.initialBalance;

        for (const auto &operation : account.log)
        {
            if (operation.sourceId == account.accountId)
            {
                calculatedBalance -= operation.amount;
            }
            else if (operation.destinationId == account.accountId)
            {
                calculatedBalance += operation.amount;
            }
        }

        if (calculatedBalance != account.currentBalance)
        {
            checkMutex.lock();
            checkPassed = false;
            checkMutex.unlock();
        }

        entry.second.mtx->unlock();
    }
}

void threadHandler(int threadId)
{
    int segmentSize = operations.size() / threadsCount;
    int startIndex = threadId * segmentSize;
    int endIndex = (threadId == threadsCount - 1) ? operations.size() : startIndex + segmentSize;

    for (int i = startIndex; i < endIndex; i++)
    {
        // update first account balance
        accounts[operations[i].sourceId].mtx->lock();
        if (accounts[operations[i].sourceId].currentBalance - operations[i].amount < 0)
        {
            accounts[operations[i].sourceId].mtx->unlock();
            continue;
        }
        accounts[operations[i].sourceId].currentBalance -= operations[i].amount;
        accounts[operations[i].sourceId].log.push_back(operations[i]);
        accounts[operations[i].sourceId].mtx->unlock();

        // update second account balance
        accounts[operations[i].destinationId].mtx->lock();
        accounts[operations[i].destinationId].currentBalance += operations[i].amount;
        accounts[operations[i].destinationId].log.push_back(operations[i]);
        accounts[operations[i].destinationId].mtx->unlock();

        if (i % 11 == 0)
        {
            performConsistencyCheck();
        }
    }
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        cerr << "Usage: " << argv[0] << " <threads_count> <operations_count>" << endl;
        return 1;
    }

    threadsCount = atoi(argv[1]);
    int operationsCount = atoi(argv[2]);

    readAccountsFromFile(ACCOUNTS_FILE_PATH);
    generateRandomOperations(operationsCount);

    auto start = chrono::high_resolution_clock::now();

    vector<thread> threads;
    for (int i = 0; i < threadsCount; i++)
    {
        threads.push_back(thread(threadHandler, i));
    }

    for (auto &t : threads)
    {
        t.join();
    }

    performConsistencyCheck();

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;

    for (auto &entry : accounts)
    {
        cout << "Account ID: " << entry.first << ", Balance: " << entry.second.currentBalance << endl;
        cout << "Number of operations performed: " << entry.second.log.size() << endl;
        delete entry.second.mtx;
    }

    if (checkPassed)
    {
        cout << endl
             << "All consistency checks passed!" << endl;
    }
    else
    {
        cout << "Consistency check did not pass!" << endl;
    }

    cout << "Execution Time: " << duration.count() << " seconds" << endl;

    return 0;
}