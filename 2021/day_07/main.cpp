#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>


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

int fuel_to_constant(vector<int> &pos, int target) {
  int fuel = 0;
  for (int i=0; i<pos.size(); i++) {
    fuel += abs(pos[i] - target);
  }
  return fuel;
}

int fuel_to_increasing(vector<int> pos, int target) {
  int fuel = 0;
  for (int i=0; i<pos.size(); i++) {
    int dist = abs(pos[i] - target);
    fuel += dist*(dist+1)/2;
  }
  return fuel;
}

int min_element(vector<int> vec) {
  int m = 1e8;
  for (int i=0; i<vec.size(); i++) {
    if (vec[i] < m) {
      m = vec[i];
    }
  }
  return m;
}

int max_element(vector<int> vec) {
  int m = 0;
  for (int i=0; i<vec.size(); i++) {
    if (vec[i] > m) {
      m = vec[i];
    }
  }
  return m;
}

int part_1(vector<int> pos) {
  int iteration_fuel;

  int min_pos = min_element(pos);
  int max_pos = max_element(pos);

  int min_fuel = max_pos * pos.size();

  for (int i=min_pos; i<=max_pos; i++) {
    iteration_fuel = fuel_to_constant(pos, i);
    if (iteration_fuel < min_fuel) {
      min_fuel = iteration_fuel;
    }
  }
  return min_fuel;
}

int part_2(vector<int> pos) {
  int iteration_fuel;

  int min_pos = min_element(pos);
  int max_pos = max_element(pos);

  int min_fuel = max_pos * pos.size() * pos.size();

  for (int i=min_pos; i<=max_pos; i++) {
    iteration_fuel = fuel_to_increasing(pos, i);
    if (iteration_fuel < min_fuel) {
      min_fuel = iteration_fuel;
    }
  }
  return min_fuel;
}

int main() {
  vector<int> positions = readFile("input.txt");
  int fuel1 = part_1(positions);
  cout << fuel1 << endl;
  int fuel2 = part_2(positions);
  cout << fuel2 << endl;
  return 0;
}