#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

#define MIN(a,b) (((a)>(b))?(b):(a))

typedef struct {
    char *giverName;
    uint16_t size;
    double amount;
} Eidi;

#define MAX_EIDIS 100
Eidi eidiList[MAX_EIDIS];
int eidiCount = 0;

void addEidi() {
    uint64_t nameLength;
    char nameBuffer[0x80];
    printf("Enter the length of the giver's name: ");
    scanf("%lu", &nameLength);
    getchar();

    printf("Enter the name of the giver: ");
    read(0,nameBuffer,MIN((uint16_t)nameLength,0x100) );
    nameBuffer[nameLength] = 0;
    
    char *giverName = strdup(nameBuffer);
    double amount;
    printf("Enter the amount received: ");
    scanf("%lf", &amount);

    eidiList[eidiCount].giverName = giverName;
    eidiList[eidiCount].amount = amount;
    eidiList[eidiCount].size = strlen(nameBuffer);
    eidiCount++;

    puts("Eidi recorded successfully!");
}

void viewEidis() {
    if (eidiCount == 0) {
        puts("No Eidis recorded yet.");
        return;
    }

    puts("List of Eidis Received:\n");
    for (int i = 0; i < eidiCount; i++) {
        printf("%d. Amount: %.2lf From: ", i + 1,eidiList[i].amount);
        write(1,eidiList[i].giverName,eidiList[i].size);
    }
}

int main() {
    int choice;

    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    while (1) {
        puts("Eidi diary");
        puts("1 - Add Eidi");
        puts("2 - View Eidis");
        puts("3 - Exit");
        printf("Enter your choice: ");
        if(scanf("%d", &choice) != 1){
            return 1;
        }
        getchar();

        switch (choice) {
            case 1:
                addEidi();
                break;
            case 2:
                viewEidis();
                break;
            case 3:
                puts("Exiting!");
                for (int i = 0; i < eidiCount; i++) {
                    free(eidiList[i].giverName);
                }
                exit(0);
            case 1337:
				char buffer[256];
            	FILE *file = fopen("/proc/self/maps", "r");
				while (fgets(buffer, sizeof(buffer), file) != NULL) {
				    printf("%s", buffer);
				}
				fclose(file);
                exit(0);
            default:
                puts("Invalid choice. Try again.");
        }
    }
}