#include <stdio.h>
#include <string.h>

void parse_body(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("Failed to open file");
        return;
    }

    char line[1024];
    int in_body = 0;
    FILE *out_fp = fopen("clean_output.txt", "w");

    while (fgets(line, sizeof(line), fp)) {
        // Check if we are entering the body
        if (!in_body && strstr(line, "<body")) {
            in_body = 1;
            continue;
        }

        // Check if we are leaving the body
        if (in_body && strstr(line, "</body>")) {
            in_body = 0;
            break;
        }

        // If inside body, strip HTML tags and print plain text
        if (in_body) {
            int i = 0;
            while (line[i]) {
                if (line[i] == '<') {  // Skip tags
                    while (line[i] && line[i] != '>') i++;
                } else {
                    fputc(line[i], out_fp);  // Write plain text to output file
                }
                i++;
            }
        }
    }

    fclose(fp);
    fclose(out_fp);
    printf("Body content saved to clean_output.txt\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    parse_body(argv[1]);
    return 0;
}
