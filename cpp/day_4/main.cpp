#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


void tokenize(string &str, char delim, vector<int> &out)
{
	size_t start;
	size_t end = 0;

	while ((start = str.find_first_not_of(delim, end)) != string::npos)
	{
		end = str.find(delim, start);
		out.push_back(stoi(str.substr(start, end - start)));
	}
}

vector<int> parseFixedWidth(string &str, int width) {
  vector<int> out;
  for (int i=0; i<=str.size()/width; i++) {
    out.push_back(stoi(str.substr(width*i, width)));
  }
  return out;
}

void readFile(string fileName, vector<int> &numbers, vector<vector<vector<int>>> &bingos) {
  string line;
  std::ifstream in(fileName);

  getline(in, line);
  tokenize(line, ',', numbers);

  if (in.is_open()) {
    int i = 0;
    vector<vector<int>> bingo(5, vector<int>(5));

    while (getline(in, line)) {
      if (line != "") {
        bingo[i%5] = parseFixedWidth(line, 3);

        i++;
        if (i%5 == 0) {
          bingos.push_back(bingo);
        }
      }
  }
    in.close();
  }
  else {
    cout << "Unable to open file";
  }
}

vector<int> slice(vector<int>& arr, int X, int Y)
{

    // Starting and Ending iterators
    auto start = arr.begin() + X;
    auto end = arr.begin() + Y + 1;

    // To store the sliced vector
    vector<int> result(Y - X + 1);

    // Copy vector using copy function()
    copy(start, end, result.begin());

    // Return the final sliced vector
    return result;
}

bool checkLine(vector<int> &line, vector<int> &numbers) {
  int matches = 0;
  for (int i=0; i<numbers.size(); i++) {
    matches += count(line.begin(), line.end(), numbers[i]);
  }
  return matches == 5;
}

vector<bool> checkRows(vector<vector<int>> &bingo, vector<int> &numbers) {
  vector<bool> matches(bingo.size(), false);
  for (int i=0; i<bingo.size(); i++) {
    matches[i] = checkLine(bingo[i], numbers);
  }
  return matches;
}

vector<int> getColumn(vector<vector<int>> &bingo, int index) {
  vector<int> col(bingo[0].size());
  for (int i=0; i<bingo.size(); i++) {
    col[i] = bingo[i][index];
  }
  return col;
}

vector<bool> checkColumns(vector<vector<int>> &bingo, vector<int> &numbers) {
  vector<bool> matches(bingo[0].size(), false);
  for (int j=0; j<bingo[0].size(); j++) {
    vector<int> col = getColumn(bingo, j);
    matches[j] = checkLine(col, numbers);
  }

  return matches;
}

int getTrueIndex(vector<bool> v)
{
    auto it = find(v.begin(), v.end(), true);

    // If element was found
    if (it != v.end())
    {

        // calculating the index
        // of K
        int index = it - v.begin();
        return index;
    }
    else {
        // If the element is not
        // present in the vector
        return -1;
    }
}

vector<int> checkBingo(vector<vector<int>> &bingo, vector<int> &numbers) {
  vector<bool> row_match = checkRows(bingo, numbers);
  vector<bool> col_match = checkColumns(bingo, numbers);

  {
    int index = getTrueIndex(row_match);
    int a = 1;
    if (index > -1) {
      return bingo[index];
    }
  }
  {
    int index = getTrueIndex(col_match);
    if (index > -1) {
      vector<int> col = getColumn(bingo, index);
    return col;
  }
  }

  return vector<int>(5, -1);
}

void part_1(vector<vector<vector<int>>> &bingos, vector<int> &numbers, vector<vector<int>> &winner, vector<int> &used_numbers) {
  vector<int> inums;
  for (int i=4; i<numbers.size(); i++) {
    inums = slice(numbers, 0, i);
    for (int i=0; i<bingos.size(); i++) {
      vector<int> line = checkBingo(bingos[i], inums);
      if (line[0] != -1) {
        winner = bingos[i];
        used_numbers = inums;
        return;
      }
    }
  }
}

void part_2(vector<vector<vector<int>>> &bingos, vector<int> &numbers, vector<vector<int>> &loser, vector<int> &used_numbers) {
  vector<int> inums;
  for (int i=4; i<numbers.size(); i++) {
    inums = slice(numbers, 0, i);
    for (int i=bingos.size()-1; i>-1; i--) {
      vector<int> line = checkBingo(bingos[i], inums);
      if (line[0] != -1) {
        if (bingos.size() == 1) {
          loser = bingos[0];
          used_numbers = inums;
          return;
        }
        else {
          bingos.erase(bingos.begin() + i);
        }

      }
    }
  }
}

int sumOfUnmarked(vector<vector<int>> &bingo, vector<int> &numbers) {
  int s = 0;
  for (int i=0; i<bingo.size(); i++) {
    for (int j=0; j<bingo[0].size(); j++) {
      if (find(numbers.begin(), numbers.end(), bingo[i][j]) == numbers.end()) {
        s += bingo[i][j];
      }
    }
  }
  return s;
}

int main(){
  vector<int> numbers;
  vector<vector<vector<int>>> bingos;
  readFile("input.txt", numbers, bingos);

  {
    vector<vector<int>> winner;
    vector<int> used_numbers;
    part_1(bingos, numbers, winner, used_numbers);

    cout << sumOfUnmarked(winner, used_numbers) * used_numbers.back() << endl;
  }

  {
    vector<vector<int>> loser;
    vector<int> used_numbers;
    part_2(bingos, numbers, loser, used_numbers);

    cout << sumOfUnmarked(loser, used_numbers) * used_numbers.back() << endl;
  }

  return 0;
}