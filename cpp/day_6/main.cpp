#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

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

vector<int> readFile(string fileName) {
  string line;
  std::ifstream in(fileName);
  vector<int> out;

  if (in.is_open()) {
    getline(in, line);
    tokenize(line, ',', out);
    in.close();
  }
  else {
    cout << "Unable to open file";
  }
  return out;
}

unsigned long int propagate_one(int days, int &start) {
  map<int, unsigned long int> population {{start, 1}};
  unsigned long int zeroes;
  for (int i=0; i<days; i++) {
    zeroes = population[0];
    for (int j=0; j<8; j++) {
      population[j] = population[j+1];
      if (population[j] < 0) {
        cout << "overflow" << i << endl;
      }
    }
    population[6] += zeroes;
    population[8] = zeroes;
  }
  unsigned long int total = 0;
  for (int j=0; j<population.size(); j++) {
    total += population[j];
  }
  if (total < 0) {
    cout << "overflow" << total << endl;
  }
  return total;
}

unsigned long int part_1(vector<int> &start, int days) {
  unsigned long int p = 0;
  for (int i=0; i<start.size(); i++) {
    p += propagate_one(days, start[i]);
  }
  return p;
}

int main() {
  vector<int> start = readFile("input.txt");

  unsigned long int p1 = part_1(start, 80);
  cout << p1 << endl;

  unsigned long int p2 = part_1(start, 256);
  cout << p2 << endl;

  return 0;
}
