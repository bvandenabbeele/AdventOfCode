#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


vector<string> readFile(string fileName) {
  string line;
  std::ifstream in(fileName);
  vector<string> data;

  if (in.is_open()) {
    while (getline(in, line)) {
      data.push_back(line);
    }
    in.close();
  }
  else {
    cout << "Unable to open file";
  }
  return data;
}


int decimal(string binary) {
  int dec = 0;
  for (int i=0; i<binary.size(); i++) {
    int n = binary.size() - i - 1;
    int bit = binary[i] - 48;
    dec += bit * pow(2, n);
  }
  return dec;
}


int mostCommonBit(vector<string> &data, int &index) {
  int zeros = 0;
  int ones = 0;

  for (int j=0; j<data.size(); j++) {

    int digit = data[j][index] - 48;

    switch (digit) {
      case 0:
        zeros++;
        break;
      case 1:
        ones++;
        break;
    }
  }
  if (ones > zeros) {
    return 1;
    }
  else if (ones < zeros) {
    return 0;
    }
  else {
    return -1;
  }
}


int leastCommonBit(vector<string> &data, int &index) {
  int commonB = mostCommonBit(data, index);
  switch (commonB) {
    case 0:
      return 1;
    case 1:
      return 0;
    case -1:
      return -1;
  }
  return 2;
}


void part_1(vector<string> &data, string &gamma, string &epsilon) {
  for (int i=0; i<data[0].size(); i++) {

    int d = mostCommonBit(data, i);
    if (d == 1) {
      gamma.append("1");
      epsilon.append("0");
    }
    else {
      gamma.append("0");
      epsilon.append("1");
    }
  }
}


void cleanVector(vector<string> &data, int &index, int &bit) {
  for (int i=data.size()-1; i>-1; i--) {
    if ((int)data[i][index] - 48 != bit) {
      data.erase(data.begin() + i);
    }
  }
}


void part_2(vector<string> &data, string &oxy, string &co2) {
  vector<string> oxy_vec = data;
  vector<string> co2_vec = data;

  for (int i=0; i<data[0].size(); i++) {
      if (oxy_vec.size() > 1) {
        int b = mostCommonBit(oxy_vec, i);
        if (b == -1) {
          b = 1;
        }
        cleanVector(oxy_vec, i, b);

      }
      if (co2_vec.size() > 1) {
        int b = leastCommonBit(co2_vec, i);
        if (b == -1) {
          b = 0;
        }
        cleanVector(co2_vec, i, b);
      }
  }
  oxy = oxy_vec[0];
  co2 = co2_vec[0];
}


int main() {
  vector<string> data = readFile("input.txt");

  std::string gamma;
  std::string epsilon;
  part_1(data, gamma, epsilon);

  int d_gamma = decimal(gamma);
  int d_epsilon = decimal(epsilon);

  cout << d_gamma * d_epsilon << endl;

  std::string oxy;
  std::string co2;
  part_2(data, oxy, co2);

  int d_oxy = decimal(oxy);
  int d_co2 = decimal(co2);

  cout << d_oxy * d_co2 << endl;

  return 0;
}