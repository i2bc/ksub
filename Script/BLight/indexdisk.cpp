#include "blight.h"



using namespace std;



int main(int argc, char** argv) {
	


	//SOME VARIABLES TO PLAY WITH
	int kmer_size(31);
	int core_number(18);
	string input_fasta_file("graphs_input.fa.unitigs.fa");

	//INDEX INITIZALIZATION
		
	//Index Initialization allowing the use  of multiple thread for faster construction and queries (default is 1)
	kmer_Set_Light blight_index_2(kmer_size, core_number);
	
	//INDEX CONSTRUCTION
	
	//Construct the index from an input FASTA file, temporary files are put in folder wdir that MUST exist (!)
	blight_index_2.construct_index(input_fasta_file, "wdir");
	//Blight handles .gz and .lz4 files but do not handle FASTQ or multiline FASTA
	
	//INDEX ON DISK
	
	//Write the index as a file on the disk
	blight_index_2.dump_disk("blight_index.gz");
	
	}
