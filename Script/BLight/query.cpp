#include "blight.h"
#include <iomanip> 
#include <iostream>
#include <fstream>
#include <string>
#include<stdio.h>
#include<string.h>
#include<string>
#include <cstdlib>



using namespace std;



int main(int argc, char** argv) {
	
	//INDEX ON DISK
	
	
	//Load an index previously wrote on the disk
	kmer_Set_Light blight_index_2("blight_index_input.gz");
	
	int count = 0;
	float sc{5.0f};
	int len;
	vector <string>input;
	vector <string>output;

	ifstream i;
	//input.txt : Path of FASTA files to request
	i.open("input.txt",ios::in);
	ifstream o;
	//output.txt : Jaccard index output files path
	o.open("output.txt",ios::in);
	if (i.is_open()){   //checking whether the file is open
	     string tp;
	      while(getline(i, tp)){
	     	input.push_back(tp);
	       }
	 }
	 cout << "input read ok" << "\n";
	 i.close();
	 if (o.is_open()){   //checking whether the file is open
	      string tp;
	      while(getline(o, tp)){
	      	output.push_back(tp);
	     	}
    }
	o.close();
	cout << "output read ok" <<"\n";
	
	for(int k(0);k<input.size();++k){
        ofstream myfile;
		myfile.open(output[k],ios::out);
		ifstream newfile;
		newfile.open(input[k],ios::in);
			if (newfile.is_open()){   //checking whether the file is open
    			string tp;
				while(getline(newfile, tp)){ //read data from file object and put it into string.
    				char s = tp[0];
					if (s!='>'){
    					vector<bool> presence_vector(blight_index_2.get_presence_query(tp));
    						for(int i(0);i<presence_vector.size();++i){
    							if(presence_vector[i]){
    								count = count + 1;
								}
							}
						len = presence_vector.size();
						sc = (float(count)/len)*100;
						myfile<<sc<<"\n";
						count = 0;
					}
				}
			}
        newfile.close(); //close the file object.
		myfile.close();
		cout << "JC ok"<< "\n";
	}
}
