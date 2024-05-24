#include<iostream>
#include<unistd.h>
#include<sys/types.h>
using namespace std;
int main(){
    int p;
    p = fork();
    if (p==0){
        cout<<"\n child process"<<getpid();
        sleep(12);
        cout<<"\n parent process"<<getpid();
    }
    else{
        cout<<"\n child process"<<getpid();
        cout<<"\n parent process"<<getpid();
    }
    

}
