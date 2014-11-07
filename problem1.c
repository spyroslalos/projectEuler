/*
 * Author:      Spyros Lalos
 *              mail: spyroslal@gmail.com
 *
 * Purpose: 	Find sum of all multiples of 3 || 5    
 *              below 1000.          	
 *           
 *
 * Language:    C
 *
 */
#include <stdio.h>

// find greatest multiple of a
// which is less than l
int g_mlt ( int a, int l);

int main (void) {

    int an, bn, cn;
    int a1 = 3;
    int b1 = 5;
    int c1 = 15;
    int s3 = 0;
    int s5 = 0;
    int s15 = 0;
    
    an = g_mlt ( a1, 1000 );
    bn = g_mlt ( b1, 1000 );
    cn = g_mlt ( c1, 1000 );
    
    s3 = ( (an/3)*(3+an) )/2;
    s5 = ( (bn/5)*(5+bn) )/2;
    s15 = ( (cn/15)*(15+cn) )/2;

//  printf ( "Sum of 3-seq is %d\nSum of 5-seq is %d\nSum of 15-seq is %d\n", s3, s5, s15 );
    printf ( "Final sum is %d\n", (s3 + s5) -s15 );

    return 0;

}

// for number k we have step k
// so to find upper limit below 1000
// we just need to search max-k values back
int g_mlt ( int a, int l) {
    
    int i, j;
    for ( i = l-1, j = 0 ; j <a; j++ ) {
	 //printf ("%d\n", i-j);
    	 if ( !( (i - j)%a ) ) {
    		printf ( "The max multiplier of %d below 1000 is %d\n", a, i-j );
	  	return i-j;
    	}
    } 

    return -1;
}
