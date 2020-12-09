#include <stdio.h>
#include <stdlib.h>
void stampaseq(int seq[], int dim);


void main(){
	int seq[30], sottoseq[30];
	int dim, i, j, z;
	printf("Inserisci numero elementi della sequenza\n");
	scanf("%d", &dim);
	printf("Inserisci i numeri:\n");
	for(i=0; i<dim; i++){
		scanf("%d", &seq[i]);
	};
	stampaseq(seq, dim);
	for(i=0; i<dim; i++){
		sottoseq[0]=seq[i];
		for(j=i+1, z=1; j<dim; j++){
			if(seq[j]<sottoseq[z-1]){
				sottoseq[z]=seq[j];
				z++;
				stampaseq(sottoseq, z);
			};
		};
	};
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return;
};


void stampaseq(int seq[], int dim){
	int i;
	printf("\t[");
	for(i=0; i<dim; i++){
		printf("%d,", seq[i]);
	};
	printf("]\n");
};
