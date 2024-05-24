#include <iostream>
#include <dirent.h>
using namespace std;
int main(int argc, char* argv[]) {
    // Check if directory path is provided
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <directory>" << endl;
        return 1;
    }
    // Open the directory
    DIR* dir = opendir(argv[1]);
    if (dir == nullptr) {
        cout << "Error: Could not open directory " << argv[1] <<endl;
        return 1;
    }
    // Read the first three entries
    struct dirent* entry;
    for (int i = 0; i < 3; ++i) {
        entry = readdir(dir);
        if (entry == nullptr) {
            cout << "Error: Could not read directory entry" << endl;
            closedir(dir);
            return 1;
        }
    }
    // Print the results
    cout << "Opened directory: " << argv[1] << endl;
   cout << "The third entry in the directory is: " << entry->d_name <<endl;

    // Close the directory
    closedir(dir);
    return 0;
}
