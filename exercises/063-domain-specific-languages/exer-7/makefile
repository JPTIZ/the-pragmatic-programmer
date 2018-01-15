all: timestamp

timestamp.tab.c: timestamp.y
	bison -d $^

lex.yy.c: timestamp.l
	flex $^

timestamp: timestamp.tab.c lex.yy.c
	g++ -o timestamp $^ -lfl
