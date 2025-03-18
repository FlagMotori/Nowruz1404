// gcc -fno-stack-protector -g -no-pie ./chall.c -o ./chall && ./chall
#include <stdio.h>
#include <string.h>

#define TOTAL_SEENS 7

const char *seens[TOTAL_SEENS] = {"Sonbol", "Sabzeh", "Seer", "Seeb", "Senjed", "Samanu", "Serkeh"};
char guessed[TOTAL_SEENS][20];
int correct_guesses = 0;
int guessed_flags[TOTAL_SEENS] = {0};

void win(){
	char buf[0x100];
	int fd = open("/flag",0);
	buf[read(fd,buf,0x100)] = 0;
	puts(buf);
}

int main() {
    char input[20];

    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Let's play a game!");
    puts("Guess all 7 Seens and you'll win.");

    while (correct_guesses < TOTAL_SEENS) {
        printf("Enter a Seen: ");
        scanf("%100s",input);
        
        int found = 0;
        for (int i = 0; i < TOTAL_SEENS; i++) {
            if (strcasecmp(input, seens[i]) == 0 && !guessed_flags[i]) {
                guessed_flags[i] = 1;
                strcpy(guessed[correct_guesses], input);
                correct_guesses++;
                found = 1;
                printf("Correct! %d/%d guessed.\n", correct_guesses, TOTAL_SEENS);
                break;
            }
        }
        
        if (!found) {
            printf("Incorrect or already guessed. Try again.\n");
        }
    }
    
    puts("You guessed all 7 Seens! Nice job... but this is all you get.");
    return 0;
}
