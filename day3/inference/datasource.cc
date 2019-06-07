/* Functions for getting test data for TensorFlow Lite evaluation

   Reference: https://www.geeksforgeeks.org/csv-file-management-using-c/
*/
#include "datasource.h"

#include <string>
#include <sstream>
#include <fstream>

const char* kTestDataFile = "test.csv";

using namespace std;

namespace datasource {

vector<float> GetData(int offset, int rows)
{
    vector<float> result;

    fstream fin;
    fin.open(kTestDataFile, fstream::in);

    string line;

    while (fin >> line && offset-- > 0); // skip rows

    while (fin >> line && rows-- > 0) {
        stringstream s(line);
        string word;

        while(getline(s, word, ',')) {
            result.push_back(stof(word));
        }
    }

    return result;
}

}
