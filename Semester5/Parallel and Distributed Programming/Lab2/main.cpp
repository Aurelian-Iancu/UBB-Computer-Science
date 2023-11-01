#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <random>
#include <queue>

std::vector<int> v1 = {1, 2, 3, 4, 5};
std::vector<int> v2 = {1, 2, 3, 4, 5};
std::vector<int> products;

bool producerReady = false;
bool producerDone = false;
std::condition_variable conditionVariable;
std::mutex mtx;

void producer()
{
    for (int i = 0; i < v1.size(); i++)
    {
        std::unique_lock<std::mutex> lock(mtx);
        int result = v1[i] * v2[i];
        products.push_back(result);
        producerReady = true;
        if (i == v1.size() - 1)
            producerDone = true;
        std::cout << "Producer " << i << ": " << result << std::endl;

        conditionVariable.notify_one();
    }
}

void consumer()
{
    int scalarProduct = 0;
    for (int i = 0; i < v1.size(); i++)
    {
        std::unique_lock<std::mutex> lock(mtx);
        conditionVariable.wait(lock, []
                               { return producerReady || producerDone; });
        scalarProduct += products[i];
        producerReady = false;
        std::cout << "Consumer " << i << ": " << products[i] << std::endl;
    }
    std::cout << "Scalar product: " << scalarProduct << std::endl;
}

int main(int argc, char *argv[])
{
    std::thread producerThread(producer);
    std::thread consumerThread(consumer);

    producerThread.join();
    consumerThread.join();

    return 0;
}