// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


void tokenize(string &str, char delim, vector<string> &out)
{
	size_t start;
	size_t end = 0;

	while ((start = str.find_first_not_of(delim, end)) != string::npos)
	{
		end = str.find(delim, start);
		out.push_back(str.substr(start, end - start));
	}
}


void part_1 () {
  string line;

  int forward = 0;
  int depth = 0;

  ifstream f ("input.txt");

  char del = ' ';

  if (f.is_open())
  {
    while ( getline (f, line) )
    {
      vector<string> v;
      tokenize(line, del, v);

      if (v[0] == "forward") {
        forward += std::stoi(v[1]);
      }
      else if (v[0] == "up") {
        depth -= std::stoi(v[1]);
      }
      else if (v[0] == "down") {
        depth += std::stoi(v[1]);
      }

    }
    f.close();

    cout << forward << endl;
    cout << depth << endl;
    cout << forward * depth << endl;
  }

  else cout << "Unable to open file";
}

void part_2 () {
  string line;

  int long forward = 0;
  int long aim = 0;
  int long depth = 0;

  ifstream f ("input.txt");

  char del = ' ';

  if (f.is_open())
  {
    while ( getline (f, line) )
    {
      vector<string> v;
      tokenize(line, del, v);

      if (v[0] == "forward") {
        int int_x = std::stoi(v[1]);
        forward += int_x;
        depth += aim * int_x;
      }
      else if (v[0] == "up") {
        aim -= std::stoi(v[1]);
      }
      else if (v[0] == "down") {
        aim += std::stoi(v[1]);
      }

    }
    f.close();

    cout << forward << endl;
    cout << aim << endl;
    cout << depth << endl;
    cout << forward * depth << endl;
  }

  else cout << "Unable to open file";
}

int main() {
  part_1();
  part_2();

  return 0;
}