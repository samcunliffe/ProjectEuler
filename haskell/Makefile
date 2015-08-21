
COMPILE=ghc
SOURCES=$(wildcard *.hs)
OBJECTS= $(patsubst %.hs, %.o, $(SOURCES))
INTERFA= $(patsubst %.hs, %.hi, $(SOURCES))
EXECUTA= $(patsubst %.hs, %, $(SOURCES))

all: $(EXECUTA)

$(EXECUTA): $(SOURCES)
	ghc -o $@ $@

make info:
	$(SOURCES) $(OBJECTS) $(EXECUTA)

make clean:
	rm -rf $(OBJECTS) $(INTERFA) $(EXECUTA)
