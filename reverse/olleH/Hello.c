#include <stdio.h>
#include <string.h>

int main() {
    unsigned char key[] = "Nowruz";
    unsigned char flag[100];
    unsigned char expected[] = {
        0x08, 0x22, 0x34, 0x26, 0x33, 0x01, 0x06, 0x5C, 
        0x1B, 0x1E, 0x45, 0x25, 0x3C, 0x5C, 0x01, 0x41, 
        0x07, 0x09, 0x7D, 0x30, 0x44, 0x1C, 0x12, 0x25, 
        0x7E, 0x17, 0x42, 0x45, 0x16, 0x07
    };
    
    int key_len = strlen((char *)key);
    int expected_len = sizeof(expected);
    
    printf("Enter your flag: ");
    scanf("%99s", flag);
    
    int flag_len = strlen((char *)flag);
    
    if (flag_len != expected_len) {
        printf("Try again! (Flag length should be %d characters)\n", expected_len);
        return 0;
    }
    
    // XOR the input with the key
    for (int i = 0; i < flag_len; i++) {
        flag[i] = flag[i] ^ key[i % key_len];
    }
    
    // Check if the XORed input matches the expected value
    int correct = 1;
    for (int i = 0; i < expected_len; i++) {
        if (flag[i] != expected[i]) {
            correct = 0;
            break;
        }
    }
    
    if (correct) {
        printf("Victory! You found the correct flag!\n");
    } else {
        printf("Try again!\n");
    }
    
    return 0;
}