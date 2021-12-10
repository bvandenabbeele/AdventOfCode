#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;


vector<vector<int>> readFile(string fileName) {
  string line;
  std::ifstream in(fileName);
  vector<vector<int>> out;

  if (in.is_open()) {
    while (getline(in, line)) {

      vector<int> v_line;
      for (const char &c: line) {
        int x = c- 48;
        v_line.push_back(x);
      }
      out.push_back(v_line);
    }

    in.close();
  }
  else {
    cout << "Unable to open file";
  }
  return out;
}


bool is_bottom(int pos, vector<int> &surrounding) {
  bool bottom = true;
  for (vector<int>::iterator it = surrounding.begin(); it != surrounding.end(); it++) {
    bottom *= (pos < *it);
  }
  return bottom;
}


int part_1(vector<vector<int>> &field) {
  int risk = 0;
  for (int i=0; i<field.size(); i++) {
    for (int j=0; j<field[i].size(); j++) {
      vector<int> surrounding;
      if ( (i == 0) & (j == 0) ) {
        surrounding = {field[i+1][j], field[i][j+1]};
      }
      else if ( (i == field.size() - 1) & (j == 0) ) {
        surrounding = {field[i-1][j], field[i][j+1]};
      }
      else if ( (i == 0) & (j == field[i].size() - 1) ) {
        surrounding = {field[i+1][j], field[i][j-1]};
      }
      else if ( (i == field.size() - 1) & (j == field[i].size() - 1) ) {
        surrounding = {field[i-1][j], field[i][j-1]};
      }
      else if ( i == 0) {
        surrounding = {field[i][j-1], field[i][j+1], field[i+1][j]};
      }
      else if ( i == field.size() - 1) {
        surrounding = {field[i][j-1], field[i][j+1], field[i-1][j]};
      }
      else if ( j == 0) {
        surrounding = {field[i-1][j], field[i+1][j], field[i][j+1]};
      }
      else if ( j == field[i].size() - 1) {
        surrounding = {field[i-1][j], field[i+1][j], field[i][j+1]};
      }
      else {
        surrounding = {field[i-1][j], field[i+1][j], field[i][j-1], field[i][j+1]};
      }
      if (is_bottom(field[i][j], surrounding)) {
        risk += field[i][j] + 1;
      }
    }
  }
  return risk;
}


vector<vector<int>> binary_conversion(vector<vector<int>> &field) {
  vector<vector<int>> binary_field(field.size(), vector<int>(field[0].size()));
  for (int i=0; i<field.size(); i++) {
    for (int j=0; j<field[i].size(); j++) {
      if (field[i][j] == 9) {
        binary_field[i][j] = 1;
      }
      else {
        binary_field[i][j] = 0;
      }
    }
  }
  return binary_field;
}


vector<vector<int>> find_surrounding(vector<vector<int>> &field, vector<vector<int>> &basin) {
  vector<vector<int>> surrounding;
  for (int i=0; i<basin.size(); i++) {
    vector<int> v = basin[i];
    vector<vector<int>> surr = {{v[0] - 1, v[1]}, {v[0] + 1, v[1]}, {v[0], v[1] - 1}, {v[0], v[1] + 1}};
    for (int j=0; j<surr.size(); j++) {
      if ((0 <= surr[j][0]) & (surr[j][0] < field.size()) &
          (0 <= surr[j][1]) & (surr[j][1] < field[0].size()) &
          (find(surrounding.begin(), surrounding.end(), surr[j]) == surrounding.end())) {

        surrounding.push_back(surr[j]);
      }
    }
  }
  return surrounding;
}

void grow_basin(vector<vector<int>> &basin, vector<vector<int>> &surrounding, vector<vector<int>> &field) {
  for (int i=0; i<surrounding.size(); i++) {
    vector<int> c = surrounding[i];
    if ((field[c[0]][c[1]] == 0) & (find(basin.begin(), basin.end(), c) == basin.end())) {
      basin.push_back(c);
    }
  }
}

void mark_basin(vector<vector<int>> &basin, vector<vector<int>> &field) {
  for (int i=0; i<basin.size(); i++) {
    field[basin[i][0]][basin[i][1]] = 2;
  }
}


void find_basin(vector<vector<int>> &field, vector<vector<int>> &basin) {
  int start_size = basin.size();
  vector<vector<int>> surrounding = find_surrounding(field, basin);
  grow_basin(basin, surrounding, field);
  if (basin.size() > start_size) {
    find_basin(field, basin);
  }
  else {
    mark_basin(basin, field);
    return;
  }
}


int max_element_index(vector<int> v) {
  int m = 0;
  int n;
  for (int i=0; i<v.size(); i++) {
    if (v[i] > m) {
      m = v[i];
      n = i;
    }
  }
  return n;
}


int part_2(vector<vector<int>> field) {
  vector<vector<int>> binary_field = binary_conversion(field);
  vector<int> basin_sizes;
  for (int i=0; i<field.size(); i++) {
    for (int j=0; j<field[i].size(); j++) {
      if (binary_field[i][j] == 0) {
        vector<vector<int>> basin = {{i, j}};
        find_basin(binary_field, basin);
        basin_sizes.push_back(basin.size());
      }
    }
  }
  int sol = 1;
  for (int i=0; i<3; i++) {
    int n = max_element_index(basin_sizes);
    int m = basin_sizes[n];
    sol *= m;
    basin_sizes.erase(basin_sizes.begin() + n);
  }
  return sol;
}


int main() {
  vector<vector<int>> field = readFile("input.txt");
  int risk = part_1(field);
  cout << risk << endl;
  int sol = part_2(field);
  cout << sol << endl;
  return 0;
}