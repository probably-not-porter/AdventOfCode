// Compile with `g++ day2_1.cpp -o day2_1`
#include <iostream>  
#include <string>  
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;  

int MAX_GREEN = 13;
int MAX_RED = 12;
int MAX_BLUE = 14;

vector<string> splitString(const string input, const char& delimiter) {
    vector<string> elements;
    stringstream stream(input);
    string element;
    while (getline(stream, element, delimiter)) {
        elements.push_back(element);
    }
    return elements;
}

string getSubString(const string& strValue, const char& startChar, const char& endChar)
{
    string subString = "";
    size_t startPos = strValue.find(startChar);
    size_t endPos = strValue.find(endChar);
    if( startPos != string::npos && endPos != string::npos)
    {
        subString = strValue.substr(startPos + 1, endPos - startPos - 1);
    }
    return subString;
}

int main() 
{
    int gameSum = 0;
    ifstream input( "input.txt" ); // get input file
    for( string line; getline( input, line ); ) // loop over each line in the file
    {
        int gameNum = stoi(getSubString(line, ' ', ':')); // get game number from string
        vector games = splitString(line,';');
        cout << "========= GAME: " << gameNum << " ==========" << endl;
        int best_g = 0;
        int best_r = 0;
        int best_b = 0;

        for(string game : games) // loop over each game in the line
        {
            string gameString = game;
            if (game.find("Game") != std::string::npos) // remove "Game: " from string
            {
                vector splitGame = splitString(game,':');
                gameString = splitGame[1];
            }
            vector colors = splitString(gameString,',');
            for(string color : colors) // loop over each color in the game
            {
                if (color.find("red") != std::string::npos)
                {
                    int val = stoi(getSubString(color, ' ', 'r'));
                    if (val > best_r)
                        best_r = val;
                }
                if (color.find("green") != std::string::npos) 
                {
                    int val = stoi(getSubString(color, ' ', 'g'));
                    if (val > best_g)
                        best_g = val;
                }
                if (color.find("blue") != std::string::npos)
                {
                    int val = stoi(getSubString(color, ' ', 'b'));
                    if (val > best_b)
                        best_b = val;
                }
            }
        }
        cout << "   Best Red: " << best_r << ", ";
        cout << "best Green: " << best_g << ", ";
        cout << "best Blue: " << best_b << endl;
        if (MAX_BLUE >= best_b && MAX_GREEN >= best_g && MAX_RED >= best_r)
        {
            gameSum += gameNum;
            cout << "   Result: POSSIBLE!" << endl;
        }
        else
        {
            cout << "   Result: IMPOSSIBLE!" << endl;
        }
        cout << endl;
    }
    cout << endl << "====> SUM: " << gameSum << endl;
    return 0;
}
// Answer is 2727