#include<iostream>
#include<unistd.h>
using namespace std;
int main()
{
    int pid;
    cout<<"before the fork"<<getpid();
    pid = fork();
    if(pid == -1){
        perror("fork");
        return 1;
    }
    else if (pid == 0){
        cout<<"parent process id "<<getpid();
    }
    else{
        cout<<"child process id "<<getpid();
    }


}