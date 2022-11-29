#include <stdio.h>
#include <math.h>


int main(){
	double temp=0;
	double sum=0;
	double n=-1;
	int l=0;
	char idx;

	
	while (temp != -999){
		if ((temp >=0) && (temp <=4 )){
			sum += temp;
			n += 1;
			scanf("%lf", &temp);
			if ((temp >= 3.00) && (temp >=0) && (temp <=4)){
				l+=1;
				}
			}
			else {
			scanf("%lf", &temp);
			}
		
		}
		
	double avg = sum/n;
	if (avg == 4.00){
		idx = 'A';
		}
	else if (avg >= 3.00 && avg < 4.00){
		idx = 'B';
		}
	else if (avg >= 2.00 && avg < 3.00){
		idx = 'C';
		}
	else if (avg >= 1.00 && avg < 2.00){
		idx = 'D';
		}
	else if (avg >= 0.00 && avg < 1.00){
		idx = 'E';
		}

	if (n == 0){
		printf("Tidak ada data\n");
	} else {
		printf("Jumlah mahasiswa yang lulus = %d\n", l);
		printf("Nilai rata-rata = %.2f\n",avg);
		printf("Indeks akhir kelas = %c\n", idx);
	}
	
	return 0;
}
