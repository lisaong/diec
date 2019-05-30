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

vector<vector<float>> GetData(int rows)
{
    vector<std::vector<float>> result;

    fstream fin;
    fin.open(kTestDataFile, fstream::in);

    vector<float> row;
    string line, word, temp;

    fin >> temp; // skip the header
    int count = 0;

    while (fin >> temp && count < rows) {
        row.clear();

        getline(fin, line);

        stringstream s(line);

        while(getline(s, word, ',')) {
            row.push_back(stof(word));
        }

        result.push_back(row);
        count++;
    }

    return result;
}

}
