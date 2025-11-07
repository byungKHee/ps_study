#include <string>
#include <vector>
#include <stack>
#include <deque>
#include <iostream>

using namespace std;

void move(deque<int>& q, int& total, int& left, int target = 0){
    int removed = q.front();
    q.pop_front();
    q.push_back(target);
    if (removed){
        left -= 1;
    }
    total -= removed;
    total += target;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int left = truck_weights.size();
    int total = 0;
    deque<int> q(bridge_length, 0);
    deque<int> wait(truck_weights.begin(), truck_weights.end());
    while(left) {
        if (!wait.empty()){
            if (total - q.front() + wait.front() <= weight){
                move(q, total, left, wait.front());
                wait.pop_front();
            }
            else{
                move(q, total, left);
            }
        }
        else{
            move(q, total, left);
        }
        answer += 1;
    }
    
    return answer;
}