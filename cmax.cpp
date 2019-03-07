#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    int n=3; // Ilosc zadan
    int m=3; // Ilosc maszyn
    m++;
    int p_number=0;
    srand (time(NULL));
    //Tablica zadan
    int taskarray[n][m];
 
    //Generowanie losowych czasow zadan
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            if (j==0)
            {
                taskarray[i][j]=i+1;
            }
            else
            {
                taskarray[i][j]=rand()%9+1;
            }
        }
    }
    //Wypisanie tablicy zadan
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            cout << taskarray[i][j] << ' ';
        }
        cout << endl;
    }
    // Tablica do permutacji
  int myints[n];
  for (int i=0;i<n;i++)
  {
      myints[i]=i+1;
  }

  std::sort (myints,myints+n);

  cout << "Permutacje kolejnosci zadan:\n";
  do {
      int machine1=0;
      int machine2=0;
      int machine3=0;
      p_number++;
    cout << "Permutacja " << p_number << ": ";
        for (int i=0;i<n;i++)
         {
            cout << myints[i] << " ";          
            machine1 += taskarray[i][1];
            if (i==0)
            {
                machine2 = taskarray[i][1] + taskarray[i][2];
                machine3 = taskarray[i][2] + taskarray[i][3];
            }  
            else
            {
                if (machine1<=machine2)
                {
                    machine2 += taskarray[i][2];
                }
                else
                {
                    machine2 = machine1 + taskarray[i][2];
                }     

                if (machine2<=machine3)
                {
                    machine3 += taskarray[i][3];
                }
                else
                {
                    machine3 = machine2 + taskarray[i][3];
                }            
            }
            
         }
    cout << "\n";
    cout << "Maszyna 1 konczy po: " << machine1 << endl;
    cout << "Maszyna 2 konczy po: " << machine2 << endl;
    cout << "Makespan: " << machine3 << endl;
  } while ( std::next_permutation(myints,myints+n) );



    return 0;
}
