#include<iostream>
#include<unistd.h>
#include<cstdlib>
#include<sys/wait.h>
using namespace std;
int  main(){
    pid_t pid;
    cout<<"executing excelp"<<endl;
    pid = fork();
    if(pid == -1){
        perror("fork");
        return 1;
    }
    else if (pid ==0){
        execlp("ls","ls","-l",nullptr);
        perror("execlp");
        exit(1);
    }
    else{
        wait(nullptr);
        cout<<"child process finished"<<endl;
    }
    return 0;
}