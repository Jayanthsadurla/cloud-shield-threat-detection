#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Order {
    int arrivalTime;
    int processingTime;
    int isPriority;
};

// Comparator for priority queue
struct CompareOrders {
    bool operator()(const Order &first, const Order &second) const {
        // Priority customers get served first
        if (first.isPriority != second.isPriority)
            return first.isPriority < second.isPriority;
        // Among same priority, earlier arrivals first
        if (first.arrivalTime != second.arrivalTime)
            return first.arrivalTime > second.arrivalTime;
        // If tied, shorter processing time first
        return first.processingTime > second.processingTime;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int totalOrders;
    cin >> totalOrders;

    vector<Order> orders(totalOrders);
    for (int i = 0; i < totalOrders; i++) {
        cin >> orders[i].arrivalTime >> orders[i].processingTime >> orders[i].isPriority;
    }

    // Sort by arrival time first
    sort(orders.begin(), orders.end(), [](const Order &a, const Order &b) {
        return a.arrivalTime < b.arrivalTime;
    });

    priority_queue<Order, vector<Order>, CompareOrders> serviceQueue;

    int nextOrderIdx = 0;
    int clockTime = 0;
    int currentQueueSize = 0;
    int peakQueueSize = 0;

    while (nextOrderIdx < totalOrders || !serviceQueue.empty()) {
        // Fast-forward time if queue is empty
        if (serviceQueue.empty() && clockTime < orders[nextOrderIdx].arrivalTime) {
            clockTime = orders[nextOrderIdx].arrivalTime;
        }

        // Enqueue all orders that have arrived by current time
        while (nextOrderIdx < totalOrders && orders[nextOrderIdx].arrivalTime <= clockTime) {
            serviceQueue.push(orders[nextOrderIdx]);
            currentQueueSize++;
            peakQueueSize = max(peakQueueSize, currentQueueSize);
            nextOrderIdx++;
        }

        // Service the next order in queue
        if (!serviceQueue.empty()) {
            Order currentOrder = serviceQueue.top();
            serviceQueue.pop();
            currentQueueSize--;
            clockTime += currentOrder.processingTime;
        }
    }

    cout << peakQueueSize << "\n";
    return 0;
}
