#include <iostream>
#include <vector> 
#include <ctime> 
#include <queue>

using namespace std;
int ID_COUNTER;
int PROCESS_COUNT;

// ----------------------------------
class Process {       
public:             
  int pid;
  int arrival_t;
  int burst_t;
  int compl_t;
  int turnar_t;
  int waiting_t;
  int response_t;

  Process(int &osid){
    this->pid= osid;
    this->arrival_t= rand()%100;
    this->burst_t= rand()%100;
    printf("Process Created : id=%-2d AT=%-3dBT=%-3d \n",this->pid, arrival_t, burst_t  );
    osid+=1;
  }
};


// ----------------------------------
class Process_creator{//Create Processes and send them to Scheduler
public:
  queue<Process> jobQueue;
  Process_creator(int count){
    for (int i = 0; i < count; i++) {
      jobQueue.push(Process(ID_COUNTER));
    };
  }
};

// ----------------------------------
class Scheduler{
public:
  queue<Process> jobQueue;
  Scheduler(){
    this->jobQueue =Process_creator(PROCESS_COUNT).jobQueue;
  }

  void startFCFS(){
    printf("starting fcfs\n");

  }
};

// -------------- MAIN --------------------

int main() {
  srand((unsigned) time(0));

  ID_COUNTER=0;
  PROCESS_COUNT= 10;

  Scheduler myscheduler= Scheduler();
  myscheduler.startFCFS();
  
  cout<< myscheduler.jobQueue.front().pid << endl;
  return 0;

} 