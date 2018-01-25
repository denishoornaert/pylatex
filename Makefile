all : main

lex :
	flex src/lexer/lex.flex

main : lex
	g++ -std=c++14 main.cpp -o main

clean :
	rm lex.yy.c
	rm main
